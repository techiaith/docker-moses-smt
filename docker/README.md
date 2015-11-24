```
docker pull techiaith/moses-smt
```

neu gwneud clone o GitHub a gwneud:
```
docker build --rm -t techiaith/moses-smt .
```

ac yna:

```
docker run --name moses-smt-cofnodycynulliad -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```




# Moses-SMT hefo Docker

(@todo : angen ei diweddaru.)

D.S. bydd angen gosod Docker ( >1.0.1) yn Linux neu Boot2Docker ar gyfer Windows/Mac OS X. 

Yn y pendraw, bydd modd estyn y system yn ei chyfanrwydd o docker.com fel hyn:
```
docker pull techiaith/moses-smt
```

Ond am y tro, bydd angen adeiladu delweddau eich hunain yn lleol drwy redeg:

```
docker build --rm -t techiaith/moses-smt .
```

Ar ôl llwyddo i adeiladu, bydd delwedd newydd o'r enw 'techiaith/moses-smt'  
yn eich docker, er mwyn cynnal a darparu peiriannau penodol gyda pharau a 
chyfeiriadau penodol. 

```
docker run --name moses-smt-cofnodycynulliad -t -i -p 8080:8080 techiaith/moses-smt
```

Yn y rhith weinydd newydd :

```
cd /home/moses/moses-smt
python moses.py fetchengine -e CofnodYCynulliad -s en -t cy
```

Bydd hyn yn llwytho i lawr peiriant sydd eisoes wedi ei hyfforddi gan yr Uned Technolegau
Iaith, ac ar gael o techiaith.org/moses. Mae'r ffeil yn ~3Gb mewn maint.

Ar ôl iddo orffen, mae modd ei gychwyn drwy:

```
python moses.py start -e CofnodYCynuliad -s en -t cy
```

Bydd rhith weinydd Docker yn ymateb i geisiadau XMLRPC am gyfieithiadau ar 
http://localhost:8080/RPC2 y brif gyfrifiadur. Mae modd datblygu cod syml i 
gysylltu'r gwasanaeth newydd gyda system gwe. e.e. 

https://github.com/leohacker/MosesSuite/blob/master/src/moses-suite-test/moses-server-xmlrpc-test.py

