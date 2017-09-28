default: build

build:
	docker build --rm -t techiaith/moses-smt .

run:
	docker run --name moses-smt -it -p 8080:8080 -p 8008:8008 techiaith/moses-smt bash

stop:
	docker stop moses-smt

start:
	docker start moses-smt


reset: remove run

remove:
	docker rm moses-smt

clean: remove
	docker rmi techiaith/moses-smt

