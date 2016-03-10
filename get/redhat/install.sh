set -e # exit on failure
sudo yum update
sudo yum group install "Development Tools" "Additional Development"
sudo yum install git wget zlib-devel python-devel boost-devel
sudo yum install xmlrpc-c-devel
sudo yum install rpmdevtools
