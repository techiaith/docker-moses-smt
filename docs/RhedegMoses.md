# Rhedeg Moses-SMT
Ar ôl i'r broses osod gwblhau'n lwyddianus, bydd modd i chi ddefnyddio Moses-SMT 
drwy ddefnyddio un script cyffredinol rydym wedi ei ddatblygu er mwyn hwyluso
defnyddio ei holl nodweddion. Lleolir y script yn ~/moses-smt:

``` sh
moses@ubuntu:~$ cd ~/moses-smt
moses@ubuntu:~/moses-smt$ python moses.py
usage: moses.py [-h] {fetchcorpus,fetchengine,train,start} ...
moses.py: error: too few arguments
```

## Rhedeg Peirianau'r Uned Technolegau Iaith
Un o'r nodweddion y script yw estyn peiriant sydd wedi ei hyfforddi eisoes gan 
yr Uned a'i chychwyn. Y peiriannau (a'r data) sydd ar gael gan yr Uned i 
gyfieithu'n beirianyddol gyda Moses-SMT yw :

 * CofnodYCynulliad
 * Deddfwriaeth
 
Felly er mwyn estyn peiriant parod, sy'n cyfieithu o Saesneg i Gymraeg, defnyddiwch
i'r is-orchymun 'fetchengine'. Dyma manylion 'fetchengine' 

```sh
moses@ubuntu:~/moses-smt$ python moses.py fetchengine
usage: moses.py fetchengine [-h] -e ENGINE_NAME -s SOURCE_LANG -t TARGET_LANG
moses.py fetchengine: error: argument -e/--engine is required
```

Felly, er mwyn estyn peiriant 'CofnodYCynulliad' yr Uned, sy'n cyfieithu o Saesneg
i'r Gymraeg, mae modd rhedeg y canlynol:

```sh
moses@ubuntu:~/moses-smt$ python moses.py fetchengine -e CofnodYCynulliad -s en -t cy
```

Ac yna i'w gychwyn:

``` sh
moses@ubuntu:~/moses-smt$ python moses.py start -e CofnodYCynulliad -s en -t cy
```

Bydd hyn yn achosi i weinydd Moses-SMT redeg gan ddisgwyl am negeseuon XMLRPC-C ar 
borth 8080.

## Gweinydd Dirprwyo HTTP
Os rydych angen cyfathrebu gyda'r weinydd Moses-SMT o porwr (ac HTTP) yna bydd 
angen cychwyn weinydd dirprwyo:

```sh
moses@ubuntu:~/moses-smt$ python server.py
```

Bydd modd mynd at http://127.0.0.1:8008 er mwyn gweld y peiriant ar waith.

# Running Moses-SMT
Once the installation process has been completed successfully, it will be 
possible for you to use Moses-SMT using a single general script that we've 
developed in order to make using all of its features easier. 
The script is located in ~/moses-smt:

``` sh
moses@ubuntu:~$ cd ~/moses-smt
moses@ubuntu:~/moses-smt$ python moses.py
usage: moses.py [-h] {fetchcorpus,fetchengine,train,start} ...
moses.py: error: too few arguments
```
## Running the Unit's machine translation engines 
One feature of the script is the ability to fetch and start a machine that 
has already been trained by the Unit. The engines (and data) available from
the Unit to machine translate with Moses-SMT are :

 * CofnodYCynulliad
 * Deddfwriaeth
 
So in order to fetch a ready made engine, which can translate from English to
Welsh, use the sub-command 'fetchengine'. Here are the details for 'fetchengine' 

```sh
moses@ubuntu:~/moses-smt$ python moses.py fetchengine
usage: moses.py fetchengine [-h] -e ENGINE_NAME -s SOURCE_LANG -t TARGET_LANG
moses.py fetchengine: error: argument -e/--engine is required
```

So, in order to fetch the unit's engine 'CofnodYCynulliad' which translates
from Welsh to English, you can run the following: 

```sh
moses@ubuntu:~/moses-smt$ python moses.py fetchengine -e CofnodYCynulliad -s en -t cy
```

And to start it:

``` sh
moses@ubuntu:~/moses-smt$ python moses.py start -e CofnodYCynulliad -s en -t cy
```

This will cause the Moses-SMT server to run while listening out for messages 
from XMLRPC-C on port 8080.

## HTTP Delegation Server 
If you need to communicate with the Moses-SMT server from a browser (and HTTP) then you will need to start a 
delegation server. 

```sh
moses@ubuntu:~/moses-smt$ python server.py
```

It should be possible to go to http://127.0.0.1:8008 in order to see the machine at work.
