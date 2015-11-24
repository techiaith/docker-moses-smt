default: build

build:
	docker build --rm -t techiaith/moses-smt docker

clean: 
	docker rmi techiaith/moses-smt

run-CofnodYCynulliad-en-cy:
	docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 start -e CofnodYCynulliad -s en -t cy

