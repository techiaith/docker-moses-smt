# Creu Peiriannau Moses-SMT

## Hyfforddi gyda data corpora gan yr Uned Technolegau Iaith

Os hoffwch chi hyfforddi gan ddefnyddio data gan yr Uned Technolegau Iaith, sy'n dod o ffynonellau megis 
Cofnod y Cynulliad a'r corpws Ddeddfwriaeth, yna mae tri gorchymyn syml i'w defnyddio. 

Yn gyntaf mae angen estyn y data rydym yn bwriadu ei ddefnyddio:

``` sh
moses@ubuntu:~/moses-smt$ make run 
# python moses.py fetchcorpus -e CofnodYCynulliad
```
Pwrpas yr ail orchymyn yw hyfforddi a dynodi'r cyfeiriad cyfieithu (e.e. o Gymraeg i Saesneg, neu o Saesneg i'r Gymraeg). 
Byddwch angen cyfrifiadur gyda dros 4Gb o gof. Bydd y broses yn cymryd rhai oriau i gwblhau.

I hyfforddi peiriant cyfieithu gan ddefnyddio data CofnodYCynulliad i gyfieithu o Saesneg i'r Gymraeg:

``` sh
# python moses.py train -e CofnodYCynulliad -s en -t cy
```

Ac yna i'w gychwyn:

``` sh
# python moses.py start -e CofnodYCynulliad -s en -t cy
```

[Gweler y dudalen canlynol](RhedegMoses.md) am rhagor ar sut gellir rhedeg Moses-SMT


## <a name="CorporaEichHun"></a>Hyfforddi gyda data corpora eich hun

Rhaid gosod eich testun fel ffeiliau testun cyfochrog o fewn is-ffolder sydd 
wedi ei henwi ar ôl enw eich peiriant newydd;

e.e. os yw'r data yn dod o hen gyfieithiadau 'Marchnata', yna defnyddiwch y gorchymyn canlynol :

```sh
# mkdir -p moses-models/Marchnata/corpus
```

Rhowch y ffeil Cymraeg o fewn ffeil gyda enw'r corpws a'r estyniad '.cy'. 

Rhowch y data Saesneg o fewn ffeil gyda enw'r corpws a'r estyniad '.en'. 

```sh
# ls moses-models/Marchnata/corpus
Marchnata.cy  Marchnata.en
```

Mae'r broses hyfforddi yn debyg i'r camau ochod, gweler :

``` sh
# python moses.py train -e Marchnata -s en -t cy
```

Ac yna i'w chychwyn:

``` sh
# python moses.py start -e Marchnata -s en -t cy
```


