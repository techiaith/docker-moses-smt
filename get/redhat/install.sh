set -e # exit on failure
sudo yum update
sudo yum group install "Development Tools"
sudo yum install git wget zlib-devel python-devel boost-devel
