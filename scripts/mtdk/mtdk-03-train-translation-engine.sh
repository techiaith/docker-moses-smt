#!/bin/bash

usage() { echo "Usage: $0 -m <path to moses installation>
			  -h <path to mosesmodels home> 
			  -e <model or engine name> 
			  -n <size for ngrams. Default = 3>
			  -s <machine translation source language - en or cy>
			  -t <machine translation target language - en or cy>" 1>&2; exit 1; }

while getopts ":m:h:e:n:s:t:" o; do
	case "${o}" in
		m)
			MOSES_HOME=${OPTARG}
			;;
		h) 
			MOSESMODELS_HOME=${OPTARG}
			;;
		e)
			NAME=${OPTARG}		
			;;
		n)
			NGRAMSIZE=${OPTARG}
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

if [ -z "${MOSES_HOME}" ] || [ -z "${MOSESMODELS_HOME}" ] || [ -z "${NAME}" ] || [ -z "${NGRAMSIZE}" ] || [ -z "${SOURCE_LANG}" ] || [ -z "${TARGET_LANG}" ]; then
    usage
fi

echo "##### TRAINING MACHINE TRANSLATION ENGINE FOR ${SOURCE_LANG} TO ${TARGET_LANG} #####"
echo "##### (this will take a *long time*, like hours!) #####"

mkdir -p ${MOSESMODELS_HOME}/${NAME}/${SOURCE_LANG}-${TARGET_LANG}
cd ${MOSESMODELS_HOME}/${NAME}/${SOURCE_LANG}-${TARGET_LANG}

echo "${MOSES_HOME}/mosesdecoder/scripts/training/train-model.perl -external-bin-dir ${MOSES_HOME}/external-bin-dir -root engine -corpus ${MOSESMODELS_HOME}/${NAME}/corpus/$NAME.clean -f ${SOURCE_LANG} -e ${TARGET_LANG} -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:${NGRAMSIZE}:${MOSESMODELS_HOME}/${NAME}/lm/${NAME}.blm.${TARGET_LANG}:8 > training.out c"
${MOSES_HOME}/mosesdecoder/scripts/training/train-model.perl -external-bin-dir ${MOSES_HOME}/external-bin-dir -root engine -corpus ${MOSESMODELS_HOME}/${NAME}/corpus/$NAME.clean -f ${SOURCE_LANG} -e ${TARGET_LANG} -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:${NGRAMSIZE}:${MOSESMODELS_HOME}/${NAME}/lm/${NAME}.blm.${TARGET_LANG}:8 > training.out c

if ! [ $? -eq 0 ]
then
        echo "Failed"
        exit 1
fi

cd -

exit 0
