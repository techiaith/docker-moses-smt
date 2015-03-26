[scroll down for english](#moses-smt-welsh--english-machine-translation)

# Cyfieithu Peirianyddol Cymraeg <> Saesneg Moses-SMT

Mae'r project yma yn cynnwys cod, sgriptiau a dogfennaeth gysylltiedig sy'n hwyluso defnydd Moses-SMT ar gyfer y Gymraeg. 

### Strwythur y Project

* **docs** - yn cynnwys dogfennaeth ar sut i ddefnyddio'r sgriptiau. Yn benodol:
  * sut mae gosod Moses-SMT o docker.com a llwytho peiriannau cyfieithu'r Uned Technolegau Iaith i lawr - [cliciwch yma...](docs/Docker.md)
  * sut mae gosod Moses-SMT ar gyfrifiadur arferol - [cliciwch yma...](docs/GosodiadArferol.md)
  * rhedeg Moses-SMT ar gyfrifiadur arferol - [cliciwch yma...](docs/RhedegMoses.md) 
  * sut mae hyfforddi Moses-SMT a chreu eich peiriannau eich hunain - [cliciwch yma...](docs/Hyfforddi.md)
  
* **get** - yn cynnwys y sgriptiau a ddefnyddir i baratoi a gosod Moses-SMT yn hwylus ar gyfrifiaduron Linux
* **mtdk** - yn cynnwys sgriptiau sy'n hwyluso nodweddion hyfforddi Moses-SMT 

### Ffeiliau'r Project

* **Dockerfile** - y ffeil a ddefnyddir i adeiladu delweddau docker
* **docker-moses.py** - cod Python ar gyfer hwyluso rhedeg Moses o fewn Docker
* **moses.py** - cod Python ar gyfer hwyluso defnyddio holl nodweddion Moses ar gyfrifiaduron Linux. 
* **server.py** - cod Python sy'n darparu tudalen we syml a dirprwy at weinydd XMLRPC Mosesserver.

# Moses-SMT Welsh <> English Machine Translation 

This project contains the code, scripts and related documentation which facilitates the use of Moses-SMT for Welsh.  

### The Project Structure

* **docs** - contains documentation on how to use the scripts. Specifically, how to: 
  * install Moses-SMT from docker.com and download the Language Technologies Unit's translation packages [click here...](docs/Docker.md)
  * install Moses-SMT on a normal computer - [click here...](docs/GosodiadArferol.md)
  * run Moses-SMT on a normal computer - [click here...](docs/RhedegMoses.md) 
  * train Moses-SMT and create your own engines - [click here...](docs/Hyfforddi.md)
  
* **get** - contains scripts that are necessary to prepare and install Moses-SMT on a Linux computer
* **mtdk** - containts the scripts that support Moses-SMT's training features

### The Project Files

* **Dockerfile** - the file that is used to create docker images
* **docker-moses.py** - the Python code used to enable running Moses within Docker
* **moses.py** - Python code for enabling the use of all of Moses' features on a Linux computers. 
* **server.py** - Python code for providing a simple web page and a proxy XMLRPC Mosesserver server.
