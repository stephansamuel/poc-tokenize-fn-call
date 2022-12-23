FROM python:3.7-slim

RUN apt update && apt install -y curl
RUN curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh
RUN bash /tmp/nodesource_setup.sh
RUN apt install -y nodejs
RUN npm install -g npm
RUN mkdir -p /opt/node
WORKDIR /opt/node
COPY ./package.json /opt/node/package.json
RUN cd /opt/node && npm update

#RUN apt update && apt install -y gcc python3-dev openssl
RUN apt update && apt install -y locales locales-all

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en_US
ENV LC_ALL en_US.UTF-8

CMD [ "node", "/opt/node/node_modules/nodemon/bin/nodemon.js", "./poc.py" ]
