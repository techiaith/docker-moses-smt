#Moses-SMT
## Welsh <> English Machine Translation 

This project contains code, scripts and documentation which enables you to create and use your own Welsh<>English Moses-SMT machine translation engines.  

## Introduction
This project in particular makes the following easier:
 
 * install Moses-SMT from docker.com
 * install Moses-SMT directly onto a Linux based computer/server
 * download and run machine translation engines created by the Language Technologies Unit at Bangor University
 * create your own machine translation engines with either your own translations, or the parallel corpora collected by the Language Technologies Unit from public sources, such as the Proceedings of the National Assembly for Wales and the  Legislature.

This project was created thanks to funding from the Welsh Government and CyfieithuCymru (TranslateWales) - a complete translation system "in the cloud" for translating between Welsh and English and which is licensed commercially by Bangor University. 

More information about machine translation and other resources are available at the Welsh National Language Technologies Portal - [langtech.wales/translation](http://langtech.wales/translation)

## Docker
Docker is a software packaging and installation facilitator for Linux, Mac OS X and Windows. 

The following Docker command will install Moses-SMT onto your computer: 

Dyma enghraifft o sut mae defnyddio'r Moses-SMT o fewn Docker er mwyn rhedeg peiriant cyfieithu (ar sail corpws cyfochrog CofnodYCynulliad), sy'n cyfieithu o'r Saesneg i'r Gymraeg :

```sh
docker pull techiaith/moses-smt
```

Here's an example of how to use the Dockerized Moses-SMT to download and run an engine (based on our National Assembly for Wales parallel corpus - named CofnodYCynulliad) for machine translating from English to Welsh: 

```sh
docker run --name moses-smt-cofnodycynulliad-en-cy -p 8008:8008 -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Then go to the machine translation engine's demo page in order to see it at work: http://localhost:8008


### The Project Structure

* **docs** - contains documentation on how to use the scripts. Specifically, how to: 
  * install Moses-SMT from docker.com and download the Language Technologies Unit's translation packages [click here...](docs/Docker.md)
  * install Moses-SMT on a normal computer - [click here...](docs/GosodiadArferol.md)
  * run Moses-SMT on a normal computer - [click here...](docs/RhedegMoses.md) 
  * train Moses-SMT and create your own engines - [click here...](docs/Hyfforddi.md)
  
* **get** - contains scripts that are necessary to prepare and install Moses-SMT on a Linux computer
* **mtdk** - containts the scripts that support Moses-SMT's training features

### The Project Files

* **moses.py** - Python code for enabling the use of all of Moses' features on a Linux computers. 
* **server.py** - Python code for providing a simple web page and a proxy XMLRPC Mosesserver server.
* **docker/Dockerfile** - the file that is used to create docker images
* **docker/moses.py** - the Python code used to enable running Moses within Docker
