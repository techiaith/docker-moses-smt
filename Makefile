default: build

build:
	docker build --rm -t techiaith/moses-smt .
clean: 
	docker rmi techiaith/moses-smt

run-CofnodYCynulliad-en-cy:
	docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 -v $(HOME)/moses-models/:/home/moses/moses-models techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy

