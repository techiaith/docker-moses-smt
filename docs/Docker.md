# Moses-SMT gyda Docker

Mae Docker yn dechnoleg pecynnu meddalwedd a hwyluso gosod ar gyfer Linux.  
Rydym wedi llwytho ein system Moses-SMT i gronfa docker.com er mwyn ei gwneud
hi'n haws i chi berfformio cyfieithu peirianyddol rhwng y Gymraeg a'r Saesneg. 

Byddwch angen fersiwn mwy diweddar na 1.0.1 o Docker ar eich system Linux. Bydd 
hefyd angen Boot2Docker arnoch os hoffwch redeg eich peiriant ar gyfrifiadur 
Windows neu Mac OS X. 

## Moses-SMT o docker.com
Bydd y gorchymyn canlynol yn gosod popeth:

```sh
docker pull techiaith/moses-smt
```

A dyma enghraifft o sut mae defnyddio Moses-SMT er mwyn rhedeg peiriant CofnodYCynulliad, sy'n 
cyfieithu o'r Saesneg i'r Gymraeg :

```sh
docker run --name moses-smt-cofnodycynulliad-en-cy -p 8008:8008 -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

Bydd modd mynd at http://127.0.0.1:8008 er mwyn gweld y peiriant ar waith.

# Moses-SMT with Docker

Docker is a software packaging and installation facilitator for Linux. 
We have loaded our Moses-SMT to docker.com in order to make it easier for
you to perform machine translation between Welsh and English.
You will need a version of Docker more recent than 1.0.1 on your Linux system.
You will also need Boot2Docker if you want to run your engine on a Windows or 
Mac OS X computer. 

## Moses-SMT from docker.com
The following command will install everything: 

```sh
docker pull techiaith/moses-smt
```

Here's an example of how to use Moses-SMT to run the engine CofnodYCynulliad, 
which is set to translate from English to Welsh :

```sh
docker run --name moses-smt-cofnodycynulliad-en-cy -p 8008:8008 -p 8080:8080 techiaith/moses-smt start -e CofnodYCynulliad -s en -t cy
```

To see the engine working, go to http://127.0.0.1:8008