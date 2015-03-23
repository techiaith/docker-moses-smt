#!/bin/bash

usage() { echo "Usage: $0 -m <moses installation home>
			  -h <path to mosesmodels home> 
			  -e <model or engine name>" 1>&2; exit 1; }

while getopts ":m:h:e:" o; do
	case "${o}" in
		m)	MOSES_HOME=${OPTARG}
			;;
		h) 
			MOSESMODELS_HOME=${OPTARG}
			;;
		e)
			NAME=${OPTARG} 
			;;
		*)
			usage	
			;;
	esac
done  
shift $((OPTIND-1))

if [ -z "${MOSES_HOME}" ] || [ -z "${MOSESMODELS_HOME}" ] || [ -z "${NAME}" ]; then
    usage
fi

cd ${MOSESMODELS_HOME}/${NAME}/corpus

echo "##### PREPARING TRAINING CORPUS #####"
mkdir -p temp

echo "##### LOWER CASING #####"
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/lowercase.perl -l cy < "${NAME}.cy" > "temp/${NAME}.lower.cy"
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/lowercase.perl -l en < "${NAME}.en" > "temp/${NAME}.lower.en"


echo "##### TOKENIZATION ######"
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/tokenizer.perl -l cy < "temp/${NAME}.lower.cy" > "temp/${NAME}.tok.cy" 
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/tokenizer.perl -l en < "temp/${NAME}.lower.en" > "temp/${NAME}.tok.en" 

#echo "##### CLEANING #####"
${MOSES_HOME}/mosesdecoder/scripts/training/clean-corpus-n.perl "temp/${NAME}.tok" cy en "${NAME}.clean" 1 80

cd -
