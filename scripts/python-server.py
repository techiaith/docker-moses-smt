#!/usr/bin/env python
import os
import sys
import threading
import subprocess
import cherrypy
import json
import itertools
import logging
import time
import re
import xmlrpclib
import math
from threading import Timer

def popen(cmd):
    cmd = cmd.split()
    logger = logging.getLogger('translation_log.popen')
    logger.info("executing: %s" %(" ".join(cmd)))
    return subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def pclose(pipe):
    def kill_pipe():
        pipe.kill()
    t = Timer(5., kill_pipe)
    t.start()
    pipe.terminate()
    t.cancel()

def init_log(filename):
    logger = logging.getLogger('translation_log')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.DEBUG)
    logformat = '%(asctime)s %(thread)d - %(filename)s:%(lineno)s: %(message)s'
    formatter = logging.Formatter(logformat)
    fh.setFormatter(formatter)
    logger.addHandler(fh)


class Filter(object):

    def __init__(self, remove_newlines=True, collapse_spaces=True):
        self.filters = []
        if remove_newlines:
            self.filters.append(self.__remove_newlines)
        if collapse_spaces:
            self.filters.append(self.__collapse_spaces)
	
    def filter(self, s):
        for f in self.filters:
            s = f(s)
        return s

    def __remove_newlines(self, s):
        s = s.replace('\r\n',' ')
        s = s.replace('\n',' ')
        return s

    def __collapse_spaces(self, s):
        s=re.sub('\s\s+', ' ', s)
	s=re.sub('\s([\',.])',r'\1',s)
	return s


def json_error(status, message, traceback, version):
    err = {"status":status, "message":message, "traceback":traceback, "version":version}
    return json.dumps(err, sort_keys=True, indent=4)


class ExternalProcessor(object):

    """ wraps an external script and does utf-8 conversions, is thread-safe """
    def __init__(self, cmd):
        self.cmd = cmd
        if self.cmd != None:
            self.proc = popen(cmd)
            self._lock = threading.Lock()

    def process(self, line):
        if self.cmd == None: return line
        u_string = u"%s\n" %line
        u_string = u_string.encode("utf-8")
        result = u_string  #fallback: return input
        with self._lock:
            self.proc.stdin.write(u_string)
            self.proc.stdin.flush()
            result = self.proc.stdout.readline()
        return result.decode("utf-8").strip()
        # should be rstrip but normalize_punctiation.perl inserts space
        # for lines starting with '('


class Root(object):

    def __init__(self, moses_home, moses_url, recaser_url, slang, tlang, pretty=False, verbose=0, timeout=-1): 
        
	self.filter = Filter(remove_newlines=True, collapse_spaces=True)
        self.moses_url = moses_url
	self.recaser_url = recaser_url
        self.pretty = bool(pretty)
        self.timeout = timeout
        self.verbose = verbose

        tokenizer = ['perl',os.path.join(moses_home,"mosesdecoder","scripts","tokenizer","tokenizer.perl"),"-b","-X","-l",slang,'-a']
        detokenizer = ['perl',os.path.join(moses_home,"mosesdecoder","scripts","tokenizer","detokenizer.perl"),"-b","-l",tlang]
	detruecaser = ['perl',os.path.join(moses_home,"mosesdecoder","scripts","recaser","detruecase.perl"),"-b"]
	
	self._tokenizer = map(ExternalProcessor, [u' '.join(tokenizer)])
 	self._detokenizer = map(ExternalProcessor,[u' '.join(detokenizer)])
	self._detruecaser = map(ExternalProcessor,[u' '.join(detruecaser)])

	self.tokenize = self._exec(self._tokenizer)
	self.detokenize = self._exec(self._detokenizer)
	self.detruecase = self._exec(self._detruecaser)

    def _exec(self, procs):
        def f(line):
            for proc in procs:
                line = proc.process(line)
            return line
        return f

    def _timeout_error(self, q, location):
        errors = [{"originalquery":q, "location" : location}]
        message = "Timeout after %ss" %self.timeout
        return {"error": {"errors":errors, "code":400, "message":message}}

    def _dump_json(self, data):
        if self.pretty:
            return json.dumps(data, indent=2) + "\n"
        return json.dumps(data) + "\n"

    def _load_json(self, string):
        return json.loads(string)

    def tokenize(self, sentence):
	sentence_tokenized = self.tokenize(sentence)
	return sentence_tokenized

    def detokenize(self, sentence):
	sentence_detokenized = self.detokenize(sentence)
	return sentence_detokenized

    def _translate(self, source):
        """ wraps the actual translate call to mosesserver via XMLPRC """
        proxy = xmlrpclib.ServerProxy(self.moses_url)
        params = {"text":source}
        return proxy.translate(params)

    def _recaser(self, sentence):
	proxy=xmlrpclib.ServerProxy(self.recaser_url)
  	params = {"text":sentence}
	return proxy.translate(params)

    @cherrypy.expose
    def translate(self, **kwargs):
        response = cherrypy.response
        response.headers['Content-Type'] = 'application/json'

        q = self.filter.filter(kwargs["q"])
        callback = kwargs["callback"]

        raw_src = q
        self.log("The server is working on: %s" %repr(raw_src))
        self.log_info("Request before preprocessing: %s" %repr(raw_src))
        translationDict = {"sourceText":raw_src.strip()}
       
	lower_src = raw_src.lower() 
	tokenized_src = self.tokenize(lower_src)
        
	translation = ''

        # query MT engine
	self.log_info("Requesting translation for %s" % repr(tokenized_src))
        result = self._translate(tokenized_src)
        if 'text' in result:
            translation = result['text']
        else:
            return self._timeout_error(tokenized_src, 'translation')
	self.log_info("Received translation: %s" % repr(translation))

	#
	recased_result = self._recaser(translation)
	if 'text' in recased_result:
		recased_trans=recased_result['text']
	else:
		recased_trans=translation
	
	detokenized_trans = self.detokenize(recased_trans)
	detruecased_trans = self.detruecase(detokenized_trans)
	translatedText = self.filter.filter(detruecased_trans)

	translationDict = {"translatedText":translatedText}

        data = {"data" : {"translations" : [translationDict]}}
        self.log("The server is returning: %s" %self._dump_json(data))

        if callback:
            return callback + "(" + self._dump_json(data) + ");"
        else:
	    return self._dump_json(data)


    def log_info(self, message):
        if self.verbose > 0:
            self.log(message, level=logging.INFO)

    def log(self, message, level=logging.INFO):
        logger = logging.getLogger('translation_log.info')
        logger.info(message)


    @cherrypy.expose
    def index(self):
	return """
<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.4.2/angular.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.4.2/angular-resource.js"></script>
<script>
var app = angular.module("MosesApp", ["ngResource"]);
app.controller('MosesCtrl', function($scope, $http) {
	$scope.loading = false;
	$scope.translate = function(engine, sourcelanguage, targetlanguage) {		
		$scope.loading=true;
		$translatedText="";
		$http.jsonp('http://localhost:' + location.port + '/translate?callback=JSON_CALLBACK', {
			params: {
					q:$scope.sourceText 							
				}
			})
			.success(function(response){
				$scope.translatedText=response.data.translations[0].translatedText;
				$scope.loading=false;
			})
			.error(function(response){
				$scope.loading=false;
				console.log("Error");
		});
		
  	};
});
</script>
<style>
.logos {
 	background-color: #333333;
    	height: 90px;
}

.uti {
    float: left;
    padding-left: 32px;
    padding-top: 12px;
}

.pb {
    float: right;
    padding-right: 24px;
    padding-top: 12px;
}
h1, p, textarea {
 	font-family: "Vectora W02_55 Roman","Voces";
}

</style>
</head>
<body>
<div class="logos">
	<div class="uti"><a href="http://www.bangor.ac.uk"><img src="http://geiriadur.bangor.ac.uk/skins/GeiriadurBangor/images/pb.jpg"></a></div>
	<div class="pb"><a href="http://techiaith.bangor.ac.uk"><img src="http://geiriadur.bangor.ac.uk/skins/GeiriadurBangor/images/uti.jpg"></a></div>
</div>

<h1>DEMO CYFIEITHU PEIRIANYDDOL ~ MACHINE TRANSLATION DEMO</h1>

<div ng-app="MosesApp">
	<div ng-controller="MosesCtrl">
		<table width="100%" style="margin:auto"><tr>
		<td width="45%">
	        	<textarea ng-model="sourceText" style="width:100%" rows=5 placeholder="Testun i'w gyfieithu"></textarea>	
		</td>
		<td width="10%" style="vertical-align:top">
	                <button ng-click="translate()">Cyfieithu ~ Translate >> </button>
			<img ng-show="loading" src="http://techiaith.cymru/wp-content/uploads/2015/11/ripple.gif"/>
		</td>
		<td width="45%" style="vertical-align:top">                	        	
                	<p ng-bind="translatedText" style="font-size:2em;"></p>                	
		</td></tr></table>				
	</div>    
</div>

"""

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', help='server ip to bind to, default: localhost', default="127.0.0.1")
    parser.add_argument('-port', action='store', help='server port to bind to, default: 8080', type=int, default=8080)
    parser.add_argument('-nthreads', help='number of server threads, default: 8', type=int, default=8)
    parser.add_argument('-mosesurl', dest="moses_url", action='store', help='url of mosesserver', required=True)
    parser.add_argument('-recaserurl', dest="recaser_url", action='store', help='url of moses recaser', required=True)
    parser.add_argument('-moseshome', dest="moses_home", action='store', help='path to mosesdecoder installation', required=True)
    parser.add_argument('-timeout', help='timeout for call to translation engine, default: unlimited', type=int)
    parser.add_argument('-pretty', action='store_true', help='pretty print json')
    parser.add_argument('-slang', help='source language code')
    parser.add_argument('-tlang', help='target language code')
    parser.add_argument('-logprefix', help='logfile prefix, default: write to stderr')
    parser.add_argument('-verbose', help='verbosity level, default: 0', type=int, default=0)

    args = parser.parse_args(sys.argv[1:])

    if args.logprefix:
        init_log("%s.trans.log" %args.logprefix)

    cherrypy.config.update({'server.request_queue_size' : 1000,
                            'server.socket_port': args.port,
                            'server.thread_pool': args.nthreads,
                            'server.socket_host': args.ip})
    cherrypy.config.update({'error_page.default': json_error})
    cherrypy.config.update({'log.screen': True})

    if args.logprefix:
        cherrypy.config.update({'log.access_file': "%s.access.log" %args.logprefix,
                                'log.error_file': "%s.error.log" %args.logprefix})

    cherrypy.quickstart(Root(args.moses_home,
			     args.moses_url, args.recaser_url,
                             slang = args.slang, tlang = args.tlang,
                             pretty = args.pretty,
                             verbose = args.verbose))

