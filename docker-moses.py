#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser

DEFAULT_TRAINING_DATA_URL = "http://techiaith.cymru/corpws/Moses"
DEFAULT_ENGINES_URL = "http://techiaith.cymru/moses/3.0"

MOSES_HOME = "/home/moses"
MOSESMODELS_HOME = os.path.join(MOSES_HOME, "moses-models")
SERVER_HOME = os.path.join(os.path.dirname(__file__))

# host/port to hose this server (for access thru browsers)
HOST = '127.0.0.1'
PORT = 8008

# host/post for your Moses XMLRPC server
MOSES_HOST = 'http://127.0.0.1'
MOSES_PORT = 8080
RECASER_PORT = 8081
MOSES_URL = MOSES_HOST + ":" + str(MOSES_PORT) + "/RPC2"
RECASER_URL = MOSES_HOST + ":" + str(RECASER_PORT) + "/RPC2"

DESCRIPTION = """Sgript rhedeg system cyfieithu peirianyddol Moses
© Prifysgol Bangor University
"""

class MosesRunError(Exception):
	pass

def run_commands(cmds):
	for cmd in cmds:
		print("cmd nesaf")
		cmd = u" ".join(cmd)
		print("Rhedeg %s" % cmd)
		returncode = os.system(cmd)
		if returncode != 0:
			exception_str = ["Problem yn rehedeg y gorchymyn:", "      %s" % cmd]
			raise MosesRunError(u"\n".join(exception_str))

def script_path(script):
	path = os.path.join(MTDK_HOME, script)
	if not os.path.exists(path):
		raise MosesRunError("Nid yw'r path '%s' yn bodoli.\nYdych chi wedi gosod y ffeiliau i gyd yn iawn?" % path)
	return path


def fetchengine(engine_name, source_lang, target_lang, **args):
	"""Lawrlwytho peiriant cyfieithu o techiaith.cymru / Download a translation engine from techiaith.cymru"""

	download_engine_cmd = [script_path("mt_download_engine.sh"),"-m", MOSES_HOME, "-h", MOSESMODELS_HOME, "-e", engine_name, "-s", source_lang, "-t", target_lang] 

	run_commands([download_engine_cmd])

def start(engine_name, source_lang, target_lang, **args):
	"""Cychwyn y gweinydd Moses / Start the Moses Server"""

	moses_recaser_server_cmd = [os.path.join(MOSES_HOME, "mosesdecoder","bin","mosesserver"), \
		"-f", os.path.join(MOSESMODELS_HOME, engine_name, "recaser", target_lang, "moses.ini"),\
		"--server-port",str(RECASER_PORT),\
		"&"]
	
	source_target_lang = "%s-%s" % (source_lang, target_lang)
	moses_server_cmd = [os.path.join(MOSES_HOME, "mosesdecoder", "bin", "mosesserver"), \
		"-f",\
		os.path.join(MOSESMODELS_HOME, engine_name, source_target_lang, "engine", "model", "moses.ini"),\
		"&"]

	#
	python_server_cmd = ["python", os.path.join(SERVER_HOME,"python-server.py"), \
		"-pretty",\
		"-verbose","1", \
		"-port",str(PORT),\
		"-ip",HOST,\
		"-slang",source_lang,\
		"-tlang",target_lang,\
		"-mosesurl","\"" + MOSES_URL + "\"",\
		"-recaserurl","\"" + RECASER_URL + "\"",\
		"-moseshome","\"" + MOSES_HOME + "\""]
					
	run_commands([moses_server_cmd, moses_recaser_server_cmd, python_server_cmd])


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
