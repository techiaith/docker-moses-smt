# Gosod Moses-SMT ar Linux
Bydd y cyfarwyddiadau yma yn eich cynorthwyo i osod meddalwedd cyfieithu peiranyddol
Moses yn uniongyrchol ar systemau Linux; gan gynnwys Debian, Ubuntu, CentOS a RedHat. 

Bydd gosodiad llawn o Moses yn eich caniatau i greu peiriannau cyfieithu eich hunain
ar sail hyfforddi gyda'ch data eich hunain neu corpora a gasglwyd eisoes gan Uned
Technolegau Iaith. Bydd modd hefyd eu rhedeg i'w defnyddio at dibenion eich
gwaith cyfieithu.

Rydym wedi symleiddio'r broses o osod Moses yn ddau gam syml iawn. 

## Cam 1: Paratoi'r gweinydd
Mae angen hawliau gweinyddwr ar eich system Linux. Mae'r cyfarwyddiadau canlynol 
yn canolbwyntio ar system Debian fel Ubuntu. 
Mae angen addasiadau bach ar gyfer CentOS/RedHat. 

Yn gyntaf, bydd rhaid i chi greu defnyddiwr 'moses' ar gyfer eich peiriant. 

``` sh
$ sudo adduser --home /home/moses moses
$ sudo adduser moses sudo
```
All-gofnodwch, ac yna ail-fewngofnodwch fel eich defnyddiwr 'moses' newydd.

Bydd angen gosod 'curl' er mwyn dechrau'r proses gosod:

``` sh
moses@ubuntu:~$ sudo apt-get install curl
```
## Cam 2: Gosod Moses

Dim ond un gorchymyn syml sydd ei hangen i chi osod Moses : 

```sh
moses@ubuntu:~$ curl http://techiaith.org/moses/get/debian/install.sh | sh
```

Bydd hyn yn achosi i lwyth o negeseuon ymddangos ar y sgrîn am gyfnod estynedig o amser.
Ond bydd modd wedyn i chi un'ai

 - hyfforddi gyda data corpora yr Uned Technolegau Iaith
 - hyfforddi gyda data corpora cyfochrog eich hunain
 - [rhedeg peiriant gan yr Uned Technolegau Iaith](RhedegMoses.md)
 
## Welsh English Machine Translation Moses-SMT

These instructions will allow you to install Moses SMT on Linux systems; including Ubuntu, CentOS, RedHat and Raspberry Pi. They will describe how to
create machines by training them with your own data, or using the corpora already collected by Bangor's Language Technologies Unit. They will also describe how to run your machine, and how to use it for translation.

We have simplified the installation process into two very easy steps.

## Step 1: Preparing the Server
You will need admin priviledges on your Linux system. The following instructions were written for the Debian system; which includes Ubuntu, Raspberry Pi a Mint. Small changes are needed for CentOS/RedHat.

First, you will need to create a 'moses' user for your machine.

``` sh
$ sudo adduser --home /home/moses moses
$ sudo adduser moses sudo
```

Log out, then login again using your new 'moses' user .

You'll need to enter a 'curl' in order to begin the installation process.

``` sh
moses@ubuntu:~$ sudo apt-get install curl
```

Many messages will appear on the screen for a short period.

## Installing Moses-SMT

You only need one simple command to install Moses :

```sh
moses@ubuntu:~$ curl http://techiaith.org/moses/get/debian/install.sh | sh
```

Many messages will appear on the screen for some time.
But you will then be able to either: 

 - train with the Language Technologies Unit's corpus data 
 - train with the your own parallel corpus data
 - [run a machine created by the Language Technologies Unit](RhedegMoses.md)