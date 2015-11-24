#!/bin/bash

usage() { echo "Usage: $0 -m <moses installation home>
			  -h <path to mosesmodels home> 
			  -e <model or engine name> 
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
		t)
			TARGET_LANG=${OPTARG}		
			;;
		*)
			usage	
			;;
	esac
done  
shift $((OPTIND-1))

if [ -z "${MOSES_HOME}" ] || [ -z "${MOSESMODELS_HOME}" ] || [ -z "${NAME}" ] || [ -z "${TARGET_LANG}" ]; then
    usage
fi

mkdir -p ${MOSESMODELS_HOME}/${NAME}/recaser
cd ${MOSESMODELS_HOME}/${NAME}/recaser 

echo "##### PREPARING RECASER MODEL #####"

echo "##### FILTER FOR MIXED CASE IN CORPUS #######"
python ${MOSES_HOME}/moses-smt/mtdk/mt_filter_for_mixedcase.py ${MOSESMODELS_HOME}/${NAME}/corpus/${NAME}.${TARGET_LANG} > "${NAME}.mixed.${TARGET_LANG}"

echo "##### TOKENIZATION ######"
${MOSES_HOME}/mosesdecoder/scripts/tokenizer/tokenizer.perl -l ${TARGET_LANG} < "${NAME}.mixed.${TARGET_LANG}" > "${NAME}.mixed.tok.${TARGET_LANG}" 

echo "##### TRAIN RECASER #####"
${MOSES_HOME}/mosesdecoder/scripts/recaser/train-recaser.perl --dir ${MOSESMODELS_HOME}/${NAME}/recaser/${TARGET_LANG} --corpus ${NAME}.mixed.tok.${TARGET_LANG} --train-script ${MOSES_HOME}/mosesdecoder/scripts/training/train-model.perl

cd -
