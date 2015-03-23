#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xmlrpclib import ServerProxy, Transport
from httplib import HTTPConnection
import time
import BaseHTTPServer
import urllib

# how long the XMLRPC proxy should wait for a response
# (note: the browser's javascript engine may wait for more/less time)
DEFAULT_TIMEOUT = 60

# host/port to hose this server (for access thru browsers)
HOST = '127.0.0.1'
PORT = 8008

# host/post for your Moses XMLRPC server
MOSES_HOST = 'http://127.0.0.1'
MOSES_PORT = 8080

# HTML head
HEAD = """
<html>
<head>
<meta charset="utf-8" />
<title>Moses</title>
</head>
"""
# HTML body
BODY = """
<body>
<script type='text/javascript'>

var URL = "http://%(HOST)s:%(PORT)s/translate/"

function moses_translate() {
    try
    { 
	document.getElementById('target').value="yn cyfieithu....";

	var text = document.getElementById('source').value;
    	var xmlHttp = new XMLHttpRequest();

	xmlHttp.onreadystatechange=function()
	{
		//alert("xmlHttp ready state" + xmlHttp.readyState);
		if (xmlHttp.readyState==4 && xmlHttp.status==200)
		{
			document.getElementById('target').value=xmlHttp.responseText;
		}
	}
    	var get_url = URL + encodeURIComponent(text);
    	xmlHttp.open( "GET", get_url, true );
    	xmlHttp.send(null);
    }
    catch (err)
    {
	alert(err.message);
    }
}

</script>
<div>
<textarea style='width:500px;height:100px' id='source'></textarea>
</div>
<button style='margin:10px 0 40px 50px;' onclick='moses_translate();'>Cyfieithu</button>
<div>
<textarea style='width:500px;height:100px' id='target'></textarea>
</div>
</body>
""" % locals()
# HTML tail/footer
TAIL = """
</body>
</html>
"""


class TimeoutTransport(Transport):
    """
    A class used for adding a timeout to an XMLRPC ServerProxy object
    
    Pass a kwarg 'timeout' when creating an object, otherwise
    DEFAULT_TIMEOUT is used
    """
    def __init__(self, timeout=DEFAULT_TIMEOUT, *args, **kwargs):
        Transport.__init__(self, *args, **kwargs)
        self.timeout=timeout

    def make_connection(self, host):
        conn = HTTPConnection(host, timeout=self.timeout)
        return conn
        

class MosesHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def get_xmlrpc_proxy(self):
        """
        Returns a ServerProxy object that's connected to the Moses server
        """
        host = "%s:%s/RPC2" % (MOSES_HOST, MOSES_PORT)
        proxy = ServerProxy(host, transport=TimeoutTransport())
        return proxy


    def do_HEAD(self, headers={'Content-type': 'text/html; charset=utf-8'}):
        """
        Sets the HTTP status code and any necessary headers
        
        Default headers are Content-type: text/html; charset=utf-8
        Pass a dict for the kwarg 'headers' to change your headers
        """
        self.send_response(200)
        for keyword, value in headers.items():
            self.send_header(keyword, value)
        self.end_headers()


    def do_GET(self):
        """
        Respond to a GET request.
        """
        if '/translate/' in self.path:
            self.do_GET_TRANS()
            return
        self.do_HEAD()
        self.wfile.write(HEAD)
        self.wfile.write(BODY)
        self.wfile.write(TAIL)


    def do_GET_TRANS(self):
        """
        Respond to a GET request for translation
        
        Corresponds to the path /translate/
        """
        try:
            self.do_HEAD(headers={'Content-type': 'text/plain; charset=utf-8'})
            text = urllib.unquote(self.path.split("/translate/")[-1].decode('utf-8'))
            proxy = self.get_xmlrpc_proxy()
            response = proxy.translate({'text' : text})
            self.wfile.write(response['text'].encode('utf-8'))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST, PORT), MosesHandler)
    print time.asctime(), "Server Starts / Ewch i - http://%s:%s o fewn eich porwr" % (HOST, PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST, PORT)
