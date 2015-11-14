#!/bin/bash

usage() { echo "Usage: $0 -m <path to moses installation>
		          -h <path to mosesmodels home> 
			  -e <model or engine name> 
			  -s <machine translation source language - en or cy>
			  -t <machine translation target language - en or cy>" 1>&2; exit 1; }

while getopts ":m:h:e:s:t:" o; do
	case "${o}" in
		m)	MOSES_HOME=${OPTARG}
			;;
		h) 
			MOSESMODELS_HOME=${OPTARG}
			;;
		e)
			NAME=${OPTARG}		
			;;
		s)
			SOURCE_LANG=${OPTARG}		
			;;		
		t)
			TARGET_LANG=${OPTARG}		
			;;
		*)
			usage	
			;;
	esac
done  
shift $((OPTIND-1))

if [ -z "${MOSES_HOME}" ] || [ -z "${MOSESMODELS_HOME}" ] || [ -z "${NAME}" ] || [ -z "${SOURCE_LANG}" ] || [ -z "${TARGET_LANG}" ]; then
    usage
fi

cd ${MOSESMODELS_HOME}/${NAME}/${SOURCE_LANG}-${TARGET_LANG}

echo "##### COMPACTING PHRASE TABLE #####"
echo ""
echo "Marcin Junczys-Dowmunt: Phrasal Rank-Encoding: Exploiting Phrase Redundancy and Translational Relations for Phrase Table Compression, Proceedings of the Machine Translation Marathon 2012, The Prague Bulletin of Mathematical Linguistics, vol. 98, pp. 63-74, 2012. (http://ufal.mff.cuni.cz/pbml/98/art-junczys-dowmunt.pdf)"
echo ""
echo "${MOSES_HOME}/mosesdecoder/bin/processPhraseTableMin -in engine/model/phrase-table.gz  -nscores 4 -threads 4 -out engine/model/phrase-table"
${MOSES_HOME}/mosesdecoder/bin/processPhraseTableMin -in engine/model/phrase-table.gz  -nscores 4 -threads 4 -out engine/model/phrase-table

echo "##### REORDERING TABLE #####"
gunzip engine/model/reordering-table.wbe-msd-bidirectional-fe.gz
cat engine/model/reordering-table.wbe-msd-bidirectional-fe | LC_ALL=C sort | ${MOSES_HOME}/mosesdecoder/bin/processLexicalTable -out engine/model/reordering-table.wbe-msd-bidirectional-fe

echo "##### UPDATING MOSES.INI #####"
python mt_update_compress_moses_ini.py ${MOSESMODELS_HOME}/${NAME}/${SOURCE_LANG}-${TARGET_LANG}/engine/model/moses.ini ${MOSESMODELS_HOME}/${NAME}/${SOURCE_LANG}-${TARGET_LANG}/engine/model/moses.ini.tmp

cd -

cd ${MOSESMODELS_HOME}/${NAME}/${SOURCE_LANG}-${TARGET_LANG}/engine/model

mv moses.ini moses.ini.orig
mv moses.ini.tmp moses.ini

cd -
 
