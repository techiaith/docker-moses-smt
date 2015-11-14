
# Moses SMT
## Cyfieithu Peirianyddol Cymraeg <> Saesneg 
#### Welsh <> English Machine Translation 

[scroll down for english](#moses-smt-welsh--english-machine-translation)

## Cyflwyniad
Mae'r project yma yn cynnwys cod, sgriptiau a dogfennaeth i'ch galluogi creu a defnyddio peiriannau cyfieithu Cymraeg<>Saesneg Moses-SMT eich hunain. 

Mae'r sgriptiau yn hwyluso'n benodol :

 * gosod Moses-SMT o docker.com
 * gosod Moses-SMT yn uniongyrchol ar gyfrifiaduron/weinyddion Linux 
 * llwytho i lawr a rhedeg peiriannau cyfieithu'r Uned Technolegau Iaith 
 * creu peiriannau eich hunain ar sail casgliadau cyfieithiadau eich hunain, neu corpora cyfochrog gan yr Uned Technolegau Iaith o ffynonellau cyhoeddus, megis Cofnod y Cynulliad a'r Ddeddfwriaeth.


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
* **docker-moses.py** - cod Python ar gyfer rhedeg Moses o fewn Docker
* **moses.py** - cod Python ar gyfer defnyddio holl nodweddion Moses-SMT ar gyfrifiaduron Linux. 
* **python-server.py** - cod Python ar gyfer darparu weinydd cyfieithu syml ar gyfer y we.

 
# Welsh <> English Machine Translation 

This project contains code, scripts and documentation which enables you to create and use your own Welsh<>English Moses-SMT machine translation engines.  

This project in particular makes the following easier:
 
 * install Moses-SMT from docker.com
 * install Moses-SMT directly onto a Linux based computer/server
 * download and run machine translation engines created by the Language Technologies Unit at Bangor University
 * create your own machine translation engines with either your own translations, or the parallel corpora collected by the Language Technologies Unit from public sources, such as the Proceedings of the National Assembly for Wales and the  Legislature.
 
 
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
