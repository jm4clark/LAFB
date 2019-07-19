
FROM node:10

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 9017
ENTRYPOINT [ "node", "server.js" ]
