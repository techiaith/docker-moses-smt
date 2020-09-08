# Moses-SMT hefo Docker

[>> English README](README_en.md)

Os yw Docker wedi ei osod ar eich cyfrifiadur [Get Started with Docker](https://docs.docker.com/windows/) yna dyma modd hwylus iawn i chi osod a ddefnyddio cyfieithu peirianyddol Cymraeg gyda Moses-SMT . 

Dim ond 2 orchymun sydd ei angen.

### Gorchymyn 1 : Gosod Moses-SMT 

```
 $ docker pull techiaith/moses-smt
```

Bydd hyn yn llwytho ac yn gosod isadeiledd cyfieithu peirianyddol o fewn eich system Docker.

### Gorchymun 2 : Cychwyn Peiriant Cyfieithu o’ch Ddewis

Mae’r Uned Technolegau Iaith wedi creu peiriannau cyfieithu ar sail hyfforddi gyda data rydym wedi’i gasglu o ffynonellau agored a chyhoeddus, megis Cofnod y Cynulliad a’r Ddeddfwriaeth ar-lein.

Mae gan y peiriannau enwau a chyfeiriadau cyfieithu penodol. Yr enw ar y peiriant a hyfforddwyd gyda chofnodion y Cynulliad yw ‘CofnodYCynulliad’ a’r enw ar gyfer peiriant y corpws deddfwriaeth yw ‘Deddfwriaeth’.

Dyma’r ail orchymyn, gan ddewis peiriant ‘CofnodYCynulliad’ a’i osod i gyfieithu o’r Saesneg i’r Gymraeg :

```
 $ docker run --name moses-smt-cofnodycynulliad-en-cy -p 8080:8080 -p 8008:8008 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Bydd y system yn llwytho ffeil i lawr (tua 3Gb mewn maint yn achos peiriant CofnodYCynulliad) cyn iddo gadarnhau ei fod yn barod i dderbyn ceisiadau i’w cyfieithu.

Os agorwch chi eich porwr a mynd at [http://localhost:8008](http://localhost:8008), dylai ffurflen syml ymddangos er mwyn i chi wirio a yw’r peiriant yn gweithio ai peidio.


# Gosod a rhedeg o GitHub

Mae modd i chi llwytho i lawr o GitHub ac addasu'r adnoddau hyn:

```sh
 $ git clone https://github.com/porthtechnolegauiaith/moses-smt
 $ cd moses-smt
 $ make
```

ac yna i redeg peiriant cyfieithu parod:

```sh
 $ make run
 $ python moses.py start -e moses-smt-cofnodycynulliad -e CofnodYCynulliad -s en -t cy
```

Bydd y rhith weinydd Docker yn ymateb i geisiadau JSON ar borth 8008 yn ogystal i XMLRPC ar borth 8080.

# Hyfforddi Modelau Cyfieithu Newydd 

Mae modd hyfforddi peiriannau cyfieithu Moses-SMT eich hunain una ai gan ddefnyddio data gan yr Uned Technolegau Iaith, neu gyda'ch eich data eich hun.

Gall hyfforddi eich peiriant eich hun gynnig y cyfle i greu peiriant cyfieithu sy'n adlewyrchu eich anghenion arbenigol chi o fewn pau benodol. Er enghraifft, os ydych yn gweithio ym maes cyllid, byddai'n bosib hyfforddi'r peiriant i fod yn arbennig o effeithiol wrth gyfieithu cywair yn y maes hwn, gan gynnwys termau a chystrawen arbenigol y maes. 

Gweler [Creu Peiriannau Moses-SMT](https://github.com/PorthTechnolegauIaith/moses-smt/blob/master/docs/Hyfforddi.md)
