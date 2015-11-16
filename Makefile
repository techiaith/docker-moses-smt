default: build

build-base-moses-smt:
	docker build --rm -t techiaith/moses-smt-base docker/dockerfiles/moses-smt-base

build-techiaith-moses-smt:
	cp mtdk/mt_download_engine.sh dockerfiles/moses-smt
	cp python-server.py dockerfiles/moses-smt
	cp docker-moses.py dockerfiles/moses-smt 
	docker build --rm -t techiaith/moses-smt dockerfiles/moses-smt

build:
	docker build --rm -t techiaith/moses-smt .

clean: 
	docker rmi techiaith/moses-smt

run-CofnodYCynulliad-en-cy:
	docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 -v $(HOME)/moses-models/:/home/moses/moses-models techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy

run-Meddalwedd-en-cy:
	docker run --name moses-smt-meddalwedd-en-cy -p 8080:8080 -p 8008:8008 techiaith/moses-smt start -e Meddalwedd -s en -t cy
