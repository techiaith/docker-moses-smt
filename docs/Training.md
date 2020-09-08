
# Create Moses-SMT machines

## Training with data from mthe Language Technology Unit

The Language Technologies Unit has data from sources like the Proceedings of the National Assembly and the Legislation corpus, that you can use with three simple commands to train your own translation engine:

First, you need to fetch the data that we will be using: 

``` sh
moses@ubuntu:~/moses-smt$ make run
# python moses.py fetchcorpus -e CofnodYCynulliad
```

The second command is to train and state the direction that the translation will take (i.e. Welsh to English or English to Welsh). 
You will need a computer that has at least more than 4GB of memory. The entire process will take a few hours to complete. 

In order to train a translation machine using the CofnodYCynulliad (the Proceedings of the National Assembly corpus) data that can translate from English to Welsh, you will need:

``` sh
# python moses.py train -e CofnodYCynulliad -s en -t cy
```

And then to start it:

``` sh
# python moses.py start -e CofnodYCynulliad -s en -t cy
```

[See the following page](RhedegMoses.md) for more on how to run Moses-SMT

## <a name="YourOwnCorpora"></a>Training with your own corpus data
 You will need to set out your text as paralell files in a sub-folder which is named after your new machine; 

For example, if you have data from old translations of 'Marketing', then create :

```sh
moses@ubuntu:~/moses-smt$ make run
# mkdir -p moses-models/Marchnata/corpus
```

Place the Welsh file in a file with the corpus' name, and the extension'.cy'. Then, place the English data in a file which also has the corpus' name, but with the extension '.en'. 

```sh
# ls moses-models/Marchnata/corpus
Marchnata.cy  Marchnata.en
```

To train your own machine :

``` sh
# python moses.py train -e Marchnata -s en -t cy
```

To start it :

``` sh
# python moses.py start -e Marchnata -s en -t cy
```
