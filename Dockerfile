FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get -y install git python3 python3-pip wget tar

RUN wget https://github.com/errata-ai/vale/releases/download/v2.28.0/vale_2.28.0_Linux_64-bit.tar.gz
RUN mkdir -p bin && tar -xvzf vale_2.28.0_Linux_64-bit.tar.gz -C bin
RUN export PATH=./bin:"$PATH"

WORKDIR /

RUN git clone https://github.com/railwayapp/docs.git

COPY . /railway-docs-exporter

WORKDIR /railway-docs-exporter

RUN pip3 install -r requirements.txt
# RUN python3 -m nltk.downloader punkt

CMD python3 exporter.py   