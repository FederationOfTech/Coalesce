# develop stage
FROM node:14-alpine as develop-stage

WORKDIR /app
COPY package*.json ./
COPY . /app

RUN yarn global add @quasar/cli
RUN yarn

RUN npm rebuild node-sass # needed to run sass on alpine