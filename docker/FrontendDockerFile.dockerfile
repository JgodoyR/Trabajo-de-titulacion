FROM node:18-alpine as build

COPY . /app
WORKDIR /app
EXPOSE 8000

RUN npm install -g npm

RUN npm install

