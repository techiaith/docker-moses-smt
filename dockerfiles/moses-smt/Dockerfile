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
FROM techiaith/moses-smt-base
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor / Language Technologies Unit, Bangor University <techiaith@bangor.ac.uk>

COPY mt_download_engine.sh /home/moses/moses-smt/mt_download_engine.sh 
COPY python-server.py /home/moses/moses-smt/python-server.py
COPY docker-moses.py /home/moses/moses-smt/moses.py

WORKDIR /home/moses/moses-smt

EXPOSE 8008
EXPOSE 8080

ENTRYPOINT ["python", "moses.py"]

