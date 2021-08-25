# The MIT License (MIT)

# Copyright (c) 2015 Prifysgol Bangor University

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Datblygwyr / Developers:
# Dewi Bryn Jones, Patrick Robertson
#
# Rhagor / Further Information:
# http://techiaith.cymru/cyfieithu/cyfieithu-peirianyddol/
#
FROM ubuntu:16.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor / Language Technologies Unit, Bangor University <techiaith@bangor.ac.uk>

#ARG DEBIAN_FRONTEND=noninteractive
#ENV TZ=Europe/London

RUN apt-get update && apt-get install -q -y --no-install-recommends \
	unzip \
	make \
	g++ \
	wget \
	git \
	locales \
	mercurial \
	bzip2 \
	autotools-dev \
	automake \
   	locales \
	libtool \
	zlib1g-dev \
	libbz2-dev \
	libboost-all-dev \
	libxmlrpc-core-c3-dev \
	libxmlrpc-c++8-dev \
        python3-pip \
	python3-setuptools \
	python3-dev \
	&& apt-get clean \ 
        && rm -rf /var/lib/apt/lists/*

RUN sed -i -e 's/# cy_GB.UTF-8 UTF-8/cy_GB.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# en_GB.UTF-8 UTF-8/en_GB.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=cy_GB.UTF-8

ENV LANG cy_GB.UTF-8

RUN pip3 install cherrypy==8.0.1
RUN pip3 install python-Levenshtein

RUN mkdir -p /home/moses
RUN mkdir -p /home/moses/moses-models
RUN mkdir -p /home/moses/moses-smt

ENV HOME /home/moses

ADD scripts/ /home/moses/moses-smt

WORKDIR /home/moses

# lawrlwytho/download snapshot RELEASE-3.0 moses
RUN wget https://github.com/moses-smt/mosesdecoder/archive/RELEASE-3.0.zip
RUN unzip RELEASE-3.0.zip
RUN rm RELEASE-3.0.zip
RUN mv mosesdecoder-RELEASE-3.0 mosesdecoder

RUN wget -O giza-pp.zip http://github.com/moses-smt/giza-pp/archive/228a39b94ff61f41f36a15ce0194dadc69dc0e36.zip 
RUN unzip giza-pp.zip
RUN rm giza-pp.zip
RUN mv giza-pp-228a39b94ff61f41f36a15ce0194dadc69dc0e36 giza-pp
WORKDIR /home/moses/giza-pp
RUN make

WORKDIR /home/moses

RUN mkdir external-bin-dir
RUN cp giza-pp/GIZA++-v2/GIZA++ external-bin-dir
RUN cp giza-pp/GIZA++-v2/snt2cooc.out external-bin-dir
RUN cp giza-pp/mkcls-v2/mkcls external-bin-dir

#RUN wget -O cmph-2.0.tar.gz http://downloads.sourceforge.net/project/cmph/cmph/cmph-2.0.tar.gz
RUN wget -O cmph-2.0.tar.gz http://techiaith.cymru/moses/downloads/cmph-2.0.tar.gz
RUN tar zxvf cmph-2.0.tar.gz

WORKDIR /home/moses/cmph-2.0
RUN ./configure
RUN make
RUN make install
WORKDIR /home/moses

#RUN wget -O irstlm-5.80.08.tgz http://downloads.sourceforge.net/project/irstlm/irstlm/irstlm-5.80/irstlm-5.80.08.tgz
RUN wget -O irstlm-5.80.08.tgz http://techiaith.cymru/moses/downloads/irstlm-5.80.08.tgz
RUN tar zxvf irstlm-5.80.08.tgz

WORKDIR /home/moses/irstlm-5.80.08/trunk
RUN /bin/bash -c "source regenerate-makefiles.sh"
RUN ./configure -prefix=/home/moses/irstlm
RUN make
RUN make install

WORKDIR /home/moses

# Adeiladu mosesdecoder
ENV IRSTLM /home/moses/irstlm
WORKDIR /home/moses/mosesdecoder

RUN ./bjam -a --with-irstlm=/home/moses/irstlm --serial --with-xmlrpc-c=/usr/ --with-cmph=/home/moses/cmph-2.0

WORKDIR /home/moses/moses-smt

EXPOSE 8008
EXPOSE 8080

