FROM node:9

ENV NPM_CONFIG_LOGLEVEL warn

ADD ./ /home/

WORKDIR /home

RUN npm install -g

CMD npm run start

EXPOSE 3000
