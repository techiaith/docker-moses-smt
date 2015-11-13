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

echo  ${MOSESMODELS_HOME}/${NAME}
cd ${MOSESMODELS_HOME}/${NAME}

tar -zcvf ${NAME}-${SOURCE_LANG}-${TARGET_LANG}.tar.gz lm/*.${TARGET_LANG} lm/*.${TARGET_LANG}.gz recaser/${TARGET_LANG}/* ${SOURCE_LANG}-${TARGET_LANG}

cd -

