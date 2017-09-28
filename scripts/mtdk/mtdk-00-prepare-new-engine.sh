#!/bin/bash

usage() { echo "Usage: $0 -h <path to mosesmodels home> 
			  -e <model or engine name>
			  -u <url for the parallel corpus data" 1>&2; exit 1; }

while getopts ":h:e:u:" o; do
	case "${o}" in
		h) 
			MOSESMODELS_HOME=${OPTARG}
			echo "MosesModel will be generated in : ${MOSESMODELS_HOME}"  
			;;
		e)
			NAME=${OPTARG}		
			echo "Name of model/engine : ${NAME}" 
			;;
		u)
			DATA_URL=${OPTARG}		
			echo "Will fetch parallel corpus data from : ${DATA_URL}" 
			;;
		*)
			usage	
			;;
	esac
done  
shift $((OPTIND-1))

if [ -z "${MOSESMODELS_HOME}" ] || [ -z "${NAME}" ] || [ -z "${DATA_URL}" ]; then
    usage
fi

mkdir -p ${MOSESMODELS_HOME}/${NAME}/corpus
mkdir -p ${MOSESMODELS_HOME}/${NAME}/lm

cd ${MOSESMODELS_HOME}/${NAME}/corpus
wget -O - ${DATA_URL} | tar -zxf -
cd -
