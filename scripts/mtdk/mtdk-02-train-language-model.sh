#!/bin/bash

usage() { echo "Usage: $0 -m <path to moses home>
			  -h <path to mosesmodels home> 
			  -e <model or engine name> 
			  -t <machine translation target language - en or cy>" 1>&2; exit 1; }

while getopts ":m:h:e:t:" o; do
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

echo "##### CREATING TARGET LANGUAGE MODEL #####"

export IRSTLM=${MOSES_HOME}/irstlm
cd ${MOSESMODELS_HOME}/${NAME}/lm

echo "##### INSERT START AND END BOUNDARIES #####"
echo "${MOSES_HOME}/irstlm/bin/add-start-end.sh < ../corpus/${NAME}.clean.${TARGET_LANG} > ${NAME}.sb.${TARGET_LANG}"
${MOSES_HOME}/irstlm/bin/add-start-end.sh < ../corpus/${NAME}.clean.${TARGET_LANG} > ${NAME}.sb.${TARGET_LANG}

if ! [ $? -eq 0 ] 
then
	echo "Failed"
	exit 1
fi

echo "##### BUILD LM DATA #####"
echo "${MOSES_HOME}/irstlm/bin/build-lm.sh -i ${NAME}.sb.${TARGET_LANG} -t ./tmp -p -s improved-kneser-ney -o ${NAME}.lm.${TARGET_LANG}" 
${MOSES_HOME}/irstlm/bin/build-lm.sh -i ${NAME}.sb.${TARGET_LANG} -t ./tmp -p -s improved-kneser-ney -o ${NAME}.lm.${TARGET_LANG} 

if ! [ $? -eq 0 ] 
then
	echo "Failed"
        exit 1
fi

echo "##### COMPILE LM #####"
echo "${MOSES_HOME}/irstlm/bin/compile-lm --text yes ${NAME}.lm.${TARGET_LANG}.gz ${NAME}.arpa.${TARGET_LANG}"
${MOSES_HOME}/irstlm/bin/compile-lm --text=yes ${NAME}.lm.${TARGET_LANG}.gz ${NAME}.arpa.${TARGET_LANG}  

if ! [ $? -eq 0 ] 
then
	echo "Failed"
        exit 1
fi

echo "##### BUILD BINARY LM #####"
echo "${MOSES_HOME}/mosesdecoder/bin/build_binary -i ${NAME}.arpa.${TARGET_LANG} ${NAME}.blm.${TARGET_LANG}"
${MOSES_HOME}/mosesdecoder/bin/build_binary -i ${NAME}.arpa.${TARGET_LANG} ${NAME}.blm.${TARGET_LANG}

if ! [ $? -eq 0 ] 
then
       echo "Failed"
       exit 1
fi 

cd -

exit 0
