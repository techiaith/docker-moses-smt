#!/bin/bash

usage() { echo "Usage: $0 -m <moses installation home>
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

cd ${MOSESMODELS_HOME}/${NAME}/corpus

echo "##### PREPARING TRAINING CORPUS #####"
mkdir -p temp

echo "##### LOWER CASING #####"
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/lowercase.perl -l ${TARGET_LANG} < "${NAME}.${TARGET_LANG}" > "temp/${NAME}.lower.${TARGET_LANG}"
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/lowercase.perl -l ${SOURCE_LANG} < "${NAME}.${SOURCE_LANG}" > "temp/${NAME}.lower.${SOURCE_LANG}"


echo "##### TOKENIZATION ######"
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/tokenizer.perl -l ${TARGET_LANG} < "temp/${NAME}.lower.${TARGET_LANG}" > "temp/${NAME}.tok.${TARGET_LANG}" 
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/tokenizer.perl -l ${SOURCE_LANG} < "temp/${NAME}.lower.${SOURCE_LANG}" > "temp/${NAME}.tok.${SOURCE_LANG}" 

#echo "##### CLEANING #####"
${MOSES_HOME}/mosesdecoder/scripts/training/clean-corpus-n.perl "temp/${NAME}.tok" ${TARGET_LANG} ${SOURCE_LANG} "${NAME}.clean" 1 80

cd -
