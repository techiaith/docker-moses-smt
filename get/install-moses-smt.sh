#!/bin/sh
set -e # exit on failure

cd $HOME

if [ ! -d mosesdecoder ]
then
    wget https://github.com/moses-smt/mosesdecoder/archive/RELEASE-3.0.zip
    unzip RELEASE-3.0.zip
    rm RELEASE-3.0.zip
    mv mosesdecoder-RELEASE-3.0 mosesdecoder
fi

wget -O giza-pp.zip "http://github.com/moses-smt/giza-pp/archive/master.zip"
unzip giza-pp.zip
mv giza-pp-master giza-pp
cd giza-pp
make
cd ..

mkdir -p external-bin-dir
cp giza-pp/GIZA++-v2/GIZA++ external-bin-dir
cp giza-pp/GIZA++-v2/snt2cooc.out external-bin-dir
cp giza-pp/mkcls-v2/mkcls external-bin-dir

wget -O cmph-2.0.tar.gz "http://downloads.sourceforge.net/project/cmph/cmph/cmph-2.0.tar.gz?r=&ts=1426574097&use_mirror=cznic"
tar zxvf cmph-2.0.tar.gz
cd cmph-2.0
./configure
make
sudo make install
cd -

wget -O irstlm-5.80.08.tgz "http://downloads.sourceforge.net/project/irstlm/irstlm/irstlm-5.80/irstlm-5.80.08.tgz?r=&ts=1342430877&use_mirror=kent"
tar zxvf irstlm-5.80.08.tgz
cd irstlm-5.80.08/trunk
./regenerate-makefiles.sh
./configure -prefix=$HOME/irstlm
make
make install
cd ../../

export IRSTLM=$HOME/irstlm
cd mosesdecoder

num_proc=$(cat /proc/cpuinfo | grep ^processor | wc -l)
./bjam -j$num_proc -a --with-irstlm=$HOME/irstlm --serial --with-xmlrpc-c=/usr/ --with-cmph=/$HOME/cmph-2.0

cd ..
mkdir moses-models

cd -
