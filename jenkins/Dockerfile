FROM jenkins/jenkins:latest
USER root
RUN apt-get update
RUN apt-get install curl
RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh
RUN usermod -aG docker jenkins
USER jenkins
