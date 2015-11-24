
# Moses SMT
## Cyfieithu Peirianyddol Cymraeg <> Saesneg 
(Welsh <> English Machine Translation) 

[scroll down for english](#welsh--english-machine-translation)

## Cyflwyniad

Mae'r project yma yn cynnwys cod, sgriptiau a dogfennaeth i'ch galluogi i greu a defnyddio peiriannau cyfieithu Cymraeg<>Saesneg Moses-SMT eich hunain. 

Mae'r sgriptiau yn hwyluso'n benodol :

 * gosod Moses-SMT o docker.com
 * gosod Moses-SMT yn uniongyrchol ar gyfrifiaduron/weinyddion Linux 
 * llwytho i lawr a rhedeg peiriannau cyfieithu'r Uned Technolegau Iaith 
 * creu peiriannau eich hunain ar sail casgliadau cyfieithiadau eich hunain, neu gorpora cyfochrog gan yr Uned Technolegau Iaith o ffynonellau cyhoeddus, megis Cofnod y Cynulliad a'r Ddeddfwriaeth.

Crëwyd y project yma diolch i nawdd gan Lywodraeth Cymru a CyfieithuCymru - rhaglen gyfieithu gyflawn "yn y cwmwl" ar gyfer cyfieithu rhwng y Gymraeg a’r Saesneg yw CyfieithuCymru a drwyddedir yn fasnachol gan Brifysgol Bangor.

Am ragor o wybodaeth ynghylch cyfieithu peirianyddol ac adnoddau eraill ewch i dudalennau cyfieithu Porth Technolegau Iaith Cenedlaethol Cymru - [techiaith.cymru/cyfieithu](http://techiaith.cymru/cyfieithu)

## Docker
Mae Docker yn dechnoleg pecynnu meddalwedd a hwyluso gosod ar gyfer Linux, Mac OS X a Windows. 

Bydd y gorchymyn canlynol gyda Docker yn gosod Moses-SMT ar eich cyfrifiadur:

```sh
docker pull techiaith/moses-smt
```

Dyma enghraifft o sut mae defnyddio'r Moses-SMT o fewn Docker er mwyn rhedeg peiriant cyfieithu (ar sail corpws cyfochrog `CofnodYCynulliad`), sy'n cyfieithu o'r Saesneg i'r Gymraeg :

```sh
docker run --name moses-smt-cofnodycynulliad-en-cy -p 8008:8008 -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```


### Strwythur y Project

* **docs** - yn cynnwys dogfennaeth ar sut i ddefnyddio'r sgriptiau. Yn benodol:
  * sut mae gosod Moses-SMT o docker.com a llwytho peiriannau cyfieithu'r Uned Technolegau Iaith i lawr - [cliciwch yma...](docs/Docker.md)
  * sut mae gosod Moses-SMT ar gyfrifiadur arferol - [cliciwch yma...](docs/GosodiadArferol.md)
  * rhedeg Moses-SMT ar gyfrifiadur arferol - [cliciwch yma...](docs/RhedegMoses.md) 
  * sut mae hyfforddi Moses-SMT a chreu eich peiriannau eich hunain - [cliciwch yma...](docs/Hyfforddi.md)
  
* **get** - yn cynnwys y sgriptiau a ddefnyddir i baratoi a gosod Moses-SMT yn hwylus ar gyfrifiaduron Linux
* **mtdk** - yn cynnwys sgriptiau sy'n hwyluso nodweddion hyfforddi Moses-SMT 

### Ffeiliau'r Project

* **moses.py** - cod Python ar gyfer defnyddio holl nodweddion Moses-SMT ar gyfrifiaduron Linux. 
* **python-server.py** - cod Python ar gyfer darparu gweinydd cyfieithu syml ar gyfer y we.
* **docker/Dockerfile** - y ffeil a ddefnyddir i adeiladu delweddau docker
* **docker/moses.py** - cod Python ar gyfer rhedeg Moses o fewn Docker


# Welsh <> English Machine Translation 

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
