# Debian/Ubuntu 
set -e # exit on failure
sudo apt-get update
sudo apt-get install -y make g++ git mercurial python-pip autotools-dev automake libtool zlib1g-dev libbz2-dev libboost-all-dev libxmlrpc-core-c3-dev zip
# libxmlrpc-c3-dev on Ubuntu 12.04, libxmlrpc-c++8-dev on Ubuntu 14.04
sudo apt-get install -y libxmlrpc-c3-dev || sudo apt-get install -y libxmlrpc-c++8-dev
sudo pip install cherrypy==7.1.0
sudo locale-gen cy_GB.UTF-8 en_US.UTF-8
sudo dpkg-reconfigure locales

cd $HOME
git clone https://github.com/PorthTechnolegauIaith/moses-smt.git

cd $HOME/moses-smt
./get/install-moses-smt.sh

