# Moses-SMT hefo Docker

(please scroll down for English)

Os mae Docker wedi ei osod ar eich cyfrifiadur [Get Started with Docker](https://docs.docker.com/windows/) yna mae modd hwylus iawn i chi osod a ddefnyddio cyfieithu peirianyddol. Dim 2 orchymun sydd ei angen.

## Gorchymyn 1 : Gosod Moses-SMT 

```
 $ docker pull techiaith/moses-smt
```

Bydd hyn yn llwytho ac yn gosod isadeiledd cyfieithu peirianyddol o fewn eich system Docker.

## Gorchymun 2 : Cychwyn Peiriant Cyfieithu o’ch Ddewis

Mae’r Uned Technolegau Iaith wedi creu peiriannau cyfieithu ar sail hyfforddi gyda data rydym wedi’i gasglu o ffynonellau agored a chyhoeddus, megis Cofnod y Cynulliad a’r Ddeddfwriaeth ar-lein.

Mae gan y peiriannau enwau a chyfeiriadau cyfieithu penodol. Yr enw ar y peiriant a hyfforddwyd gyda chofnodion y Cynulliad yw ‘CofnodYCynulliad’ a’r enw ar gyfer peiriant y corpws deddfwriaeth yw ‘Deddfwriaeth’.

Dyma’r ail orchymyn, gan ddewis peiriant ‘CofnodYCynulliad’ a’i osod i gyfieithu o’r Saesneg i’r Gymraeg :

```
 $ docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Bydd y system yn llwytho ffeil i lawr (tua 3Gb mewn maint yn achos peiriant CofnodYCynulliad) cyn iddo gadarnhau ei fod yn barod i dderbyn ceisiadau i’w cyfieithu.

Os agorwch chi eich porwr a mynd at [http://localhost:8008](http://localhost:8008), dylai ffurflen syml ymddangos er mwyn i chi wirio a yw’r peiriant yn gweithio ai peidio.

## Gosod a rhedeg o GitHub

Mae modd defnyddio'r adnoddau hyn o GitHub hefyd:

```sh
 $ git clone https://github.com/porthtechnolegauiaith/moses-smt
 $ cd moses-smt
 $ make
```

ac yna:

```sh
 $ make run
 $ python moses.py start -e moses-smt-cofnodycynulliad -e CofnodYCynulliad -s en -t cy
```

Bydd y rhith weinydd Docker yn ymateb i geisiadau JSON ar porth 8008 yn ogystal i XMLRPC ar porth 8080.



# Moses-SMT with Docker

If you have Docker installed on your computer [Get Started with Docker](https://docs.docker.com/windows/) then there is a very easy method by which you can install and use machine translation engines locally. There are only two commands involved. 

## Command 1 : Installing Moses-SMT 

```
 $ docker pull techiaith/moses-smt
```

This will download and install a Moses machine translation system within your Docker environment.


## Command 2 : Start a Machine Translation Engine of your Choice

The Language Technologies Unit have created machine translation engines that have been trained from bilingual data that we have collected from open and public sources, such as the Proceedings of the Welsh Assembly, the UK and Welsh Legislature website, as well as localisations of open source software. Each in turn provide domain specific machine translation capabilities. Each one is identified according to its Welsh name. Thus:

 - CofnodYCynulliad  : as trained from the Welsh Assembly Proceedings
 - Deddfwriaeth  : as trained from UK and Welsh legislature
 - Meddalwedd : as trained from localisations of various open source software projects. 
 
These names can be used in the second Docker command that will start (and fetch is necessary from the Welsh National Language Technologies Portal) an engine for a desired source and target language pairing:

```
 $ docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

In the case of CofnodYCynulliad, the engine may be a very large download - about 3Gb. 

Open your browser and browse to [http://localhost:8008](http://localhost:8008), where you should see a simple demo form that will help you check if the engine is working or not.

## Installing and Running from GitHub

To download and install from GitHub: 

```sh
 $ git clone https://github.com/porthtechnolegauiaith/moses-smt
 $ cd moses-smt
 $ make
```

and then: 

```sh
 $ make run
 $ python moses.py start -e CofnodYCynulliad -s en -t cy
```

The running Docker container will respond to JSON requests on port 8008 as well as XMLRPC on port 8080.


