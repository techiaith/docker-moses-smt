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
 $ cd moses-smt/docker
 $ docker build --rm -t techiaith/moses-smt .
```

ac yna:

```
 $ docker run --name moses-smt-cofnodycynulliad -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Bydd y rhith weinydd Docker yn ymateb i geisiadau JSON ar porth 8008 yn ogystal i XMLRPC ar porth 8080 cyfieithiadau ar http://localhost:8080/RPC2 y brif gyfrifiadur. 

