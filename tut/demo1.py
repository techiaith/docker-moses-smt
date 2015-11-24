#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from urllib import request
    from urllib.parse import urlencode
except ImportError:
    import urllib2 as request
    from urllib import urlencode

try:
    # python2
    input = raw_input
except NameError:
    # python3
    input = input

import json

# ==============================
# = GOSODIADAU / USER SETTINGS =
# ==============================
# Eich allwedd API - o https://api.techiaith.org
# Your API Key - from https://api.techiaith.org
# Cewch hefyd gadael hyn yn wag, a cadw'ch allwedd API mewn ffeil 'API_KEY'
# You can also leave this empty and keep your API key in a file called 'API_KEY'
API_KEY = ""

# Gellir defnyddio 'cy' neu 'en' ar gyfer iaith yr API
# Api lang parameter can be either 'cy' or 'en'
API_LANG = 'cy'

API_URL = "https://api.techiaith.org/translate/v1/translate/?"

# ==============
# = Cod / Code =
# ==============

if not API_KEY:
    # ceisio darllen yr API key o ffeil
    import os
    if os.path.exists("API_KEY"):
        with open("API_KEY", 'rb') as a:
            API_KEY = a.read().decode('utf-8').strip()

if API_KEY == "":
    print("""
=================
***GWALL/ERROR***
=================

RHAID gosod eich allwedd API in gwiriwr.py yn gyntaf. Gwelwch https://api.techiaith.org
You MUST set your API Key in gwiriwr.py first. See https://api.techiaith.org
""")
    import sys
    sys.exit(1)



def get_translations(source,engine,sourcelang,targetlang):
    """
    Galw'r API ar gyfer cyfieithu  un llinell
    Call the API to check the spelling for one line
    """
    params = {
        'api_key': API_KEY.encode('utf-8'),
        'source': sourcelang.encode('utf-8'),
	'target': targetlang.encode('utf-8'),
	'engine':engine.encode('utf-8'),
        'q': source.encode('utf-8')
    }
    url = API_URL + urlencode(params)
    
    response = request.urlopen(url)
    response = json.loads(response.read().decode('utf-8'))
    if not response['success']:
        # Gwall gyda'r galwad API
        # something went wrong with the API call
        translations = u'\n'.join(response['translations'])
        raise ValueError(translations)
    
    return response['translations']


def cyfieithu_testun(testun, peiriant, iaithffynhonnell, iaithtarged):
    """
    Cyfieithu un llinell ar y tro
    Translates one line at a time
    """
    translations = get_translations(testun, peiriant, iaithffynhonnell, iaithtarged)

    if not len(translations):
        return testun
   
    return translations[0]['translatedText']
 

if __name__ == '__main__':

	import sys, argparse
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-e', help="enw'r peiriant cyfieithu", action='store', dest='engine', required=True)
	parser.add_argument('-s', help="iaith ffynhonnell",action='store',dest='sourcelang',required=True)
	parser.add_argument('-t', help="iaith targed",action='store',dest='targetlang',required=True)
	parser.add_argument('-f', help='ffeil ar gyfer cyfieithu', dest='sourcefile')

	args = parser.parse_args(sys.argv[1:])

	if args.sourcefile:
		with open(sourcefile,'rb') as f:
			testun = f.read().decode('utf-8')
	else:
		testun = ""
		while not testun.strip():
			testun = input(u"Ysgrifennwch testun i'w gyfieithu:\n")
		if sys.version_info[0]==2:
			testun = testun.decode('utf-8')

	llinellau = testun.split(u"\n")

	for llinell in llinellau:
		 print cyfieithu_testun(llinell, args.engine, args.sourcelang, args.targetlang)
		
