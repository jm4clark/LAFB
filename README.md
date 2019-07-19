# LAFB

## Project Briefing
The aim of this project was to convert a legacy project build into a more flexible format that allows for a modular interexchange of microservices. This was to be driven by a Continuous Integration pipeline, powered by Jenkins.

# Original Architecture
The original architecture used mlabs as the database, with four microservices packaged as a single monolith.
![Image of Yaktocat](/images/Architecture1.png)

# New Architecture
The new architecture uses a mongo database, with the addition three new microservices, of which there are two versions. These are:
* A text generator which generates a random sequence of characters
* A number generator which generates a random sequence of numbers
* A prize generator which submits a different prize figure depending upon the result of a gamble
![Image of Yaktocat](/images/Architecture2.png)
Small changes in our docker-compose.yaml file allows switching between the two variants.

# Jenkins Pipeline
The Jenkins Pipeline utilizes a webhook to the LAFB github repository (https://github.com/jm4clark/LAFB.git)
Any changes to the repository files are detected, activating the Jenkins script.
New builds are created, pushed up to the Dockerhub repository (https://hub.docker.com/u/jmclark) and called by the docker-compose.yaml file for deployment.

# Docker Swarm
Docker Swarm allows scalable deployment of our services across multiple virtual machines with little effort. A single docker-compose.yaml file organizes this for us.


## How To Deploy
In the Azure CLI, create a resource group and 3 or more virtual machines, Naming one "Manager" and the rest "Worker1", "Worker2"...
SSH into Manager and set it to the Master node with
```
docker swarm init
```
Copy the token printed by this command and paste it into the other two virtual machine shells to add them as worker nodes.

Back in the manager node, clone the project onto your machine using the command below:
```
git clone https://github.com/jm4clark/LAFB.git
```
Then once inside the LAFB folder, run the following:
```
docker stack deploy --compose-file docker-compose.yaml LAFBdemo
```
The IP address of the Manager node should take you to the website.

## Swapping Microservices/Images
Swapping between microservices simply requires a change in the docker-compose.yaml file.
![Image of Yaktocat](/images/Microservice%20Change%20Guide.png)
