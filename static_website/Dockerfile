FROM node:10 as node-build
WORKDIR /build
COPY . .
RUN npm install
RUN npm build
FROM node:10
WORKDIR /opt/website
COPY --from=node-build /build/build .
RUN npm install -g serve
ENTRYPOINT ["/usr/local/bin/serve", "-l", "8089"]
