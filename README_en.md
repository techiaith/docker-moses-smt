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

# Hyfforddi Modelau Cyfieithu Newydd 

It's possible to train your onw Moses-SMT translation engines with data by the Language Technologies Unit or your own.

Training your own translation machine could be an opportunity to create a machine that can reflect your specific needs within the field in which you work. For example, if you worked in finance, it would be possible to train your machine to be particularly effective at translating the register of this domain, including the field's own particular terminology and syntax.

See [Create Moses-SMT Engines](https://github.com/PorthTechnolegauIaith/moses-smt/blob/master/docs/Training.md)






