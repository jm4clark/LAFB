# LAFB

## Project Briefing
The aim of this project was to convert a legacy project build into a more flexible format that allows for a modular interexchange of microservices. This was to be driven by a Continuous Integration pipeline, powered by Jenkins.

# Original Architecture
The original architecture used mlabs as the database, with four microservices packaged as a single monolith.

# New Architecture
The new architecture uses a mongo database, with the addition three new microservices, of which there are two versions. These are:
* A text generator which generates a random sequence of characters
* A number generator which generates a random sequence of numbers
* A prize generator which submits a different prize figure depending upon the result of a gamble

Small changes in our docker-compose.yaml file allows switching between the two variants.

# Jenkins Pipeline
The Jenkins Pipeline utilizes a webhook to the LAFB github repository (https://github.com/jm4clark/LAFB.git)
Any changes to the repository files are detected, activating the Jenkins script.
New builds are created, pushed up to the Dockerhub repository (https://hub.docker.com/u/jmclark) and called by the docker-compose.yaml file for deployment.

# Docker Swarm
Docker Swarm allows scalable deployment of our services across multiple virtual machines with little effort.
```
docker stack deploy --compose-file docker-compose.yaml LAFBdemo
```
