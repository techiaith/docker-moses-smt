#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
import subprocess as sub
from server import MosesHandler
import time
import BaseHTTPServer

# host/port to hose this server (for access thru browsers)
HOST = ''
PORT = 8008

DEFAULT_TRAINING_DATA_URL = "http://techiaith.org/corpws/Moses"
DEFAULT_ENGINES_URL = "http://techiaith.org/moses/3.0"

MOSES_HOME = "/home/moses"
MOSESMODELS_HOME = os.path.join(MOSES_HOME, "moses-models")

DESCRIPTION = """Sgript llwytho a chychwyn system cyfieithu peirianyddol Moses
© Uned Technolegau Iaith, Prifysgol Bangor University
"""

class MosesRunError(Exception):
	pass

def run_commands(cmds):
	for cmd in cmds:
		cmd = u" ".join(cmd)
		print("Rhedeg %s" % cmd)
		returncode = os.system(cmd)
		if returncode != 0:
			exception_str = ["Problem yn rhedeg y gorchymyn:", "      %s" % cmd]
			raise MosesRunError(u"\n".join(exception_str))

def spawn_commands(cmds):
	for cmd in cmds:
		cmd = u" ".join(cmd)
		print("Rhedeg %s" % cmd)
		pid = sub.Popen(cmd, shell=True).pid
		print (pid)

def script_path(script):
	if not os.path.exists(script):
		raise MosesRunError("Nid yw'r path '%s' yn bodoli.\nYdych chi wedi gosod y ffeiliau i gyd yn iawn?" % script)
	return script

def fetchengine(engine_name, source_lang, target_lang, **args):
	"""Lawrlwytho peiriant cyfieithu o techiaith.org / Download a translation engine from techiaith.org"""

	download_engine_cmd = [script_path("./mt_download_engine.sh"),"-m", MOSES_HOME, "-h", MOSESMODELS_HOME, "-e", engine_name, "-s", source_lang, "-t", target_lang] 

	run_commands([download_engine_cmd])



def start(engine_name, source_lang, target_lang, **args):
	"""Cychwyn y gweinydd Moses / Start the Moses Server"""
	source_target_lang = "%s-%s" % (source_lang, target_lang)
	if not os.path.exists(os.path.join(MOSESMODELS_HOME, engine_name, source_target_lang)):
		print("Mae angen llwytho'r peiriant i lawr....")
		fetchengine(engine_name, source_lang, target_lang, **args)
	
	cmd = [os.path.join(MOSES_HOME, "mosesdecoder", "bin", "mosesserver"), "-f", os.path.join(MOSESMODELS_HOME, engine_name, source_target_lang, "engine", "model", "moses.ini")]
	spawn_commands([cmd])

	start_http_proxy()
	

def start_http_proxy():
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST, PORT), MosesHandler)
        print time.asctime(), "Server Starts / Ewch i - http://%s:%s o fewn eich porwr" % (HOST, PORT)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                pass
        httpd.server_close()
        print time.asctime(), "Server Stops - %s:%s" % (HOST, PORT)


if __name__ == "__main__":
	
	parser = ArgumentParser(description=DESCRIPTION)
	subparsers = parser.add_subparsers(title="Is-gorchmynion", description="Is-gorchmynion dilys", help="a ddylid llwytho, hyfforddi ynte cychwyn y peiriant")

	fetchengineparser = subparsers.add_parser('fetchengine')
	fetchengineparser.add_argument('-e','--engine', dest="engine_name", required=True, help="enw i'r peiriant cyfieithu benodol")
	fetchengineparser.add_argument('-s', '--sourcelang', dest="source_lang", required=True, help="iaith ffynhonnell")
	fetchengineparser.add_argument('-t', '--targetlang', dest="target_lang", required=True, help="iaith targed")
	fetchengineparser.set_defaults(func=fetchengine)
	
	
	startparser = subparsers.add_parser('start')
	startparser.add_argument('-e', '--engine', dest="engine_name", required=True, help="enw i'r peiriant cyfieithu benodol")
	startparser.add_argument('-s', '--sourcelang', dest="source_lang", required=True, help="iaith ffynhonnell")
	startparser.add_argument('-t', '--targetlang', dest="target_lang", required=True, help="iaith targed")
	startparser.set_defaults(func=start)
	
	args = parser.parse_args()
	try:
		args.func(**vars(args))
	except MosesRunError as e:
		print("\n**ERROR**\n")
		print(e)
