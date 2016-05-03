
# Moses SMT
## Cyfieithu Peirianyddol Cymraeg <> Saesneg 

[click here for English README](README_en.md)

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

Yna, ewch i dudalen demo y peiriant er mwyn ei weld ar waith : http://localhost:8008 



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

