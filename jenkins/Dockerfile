FROM jenkins/jenkins:latest
USER root
VOLUME /var/run/docker.sock /var/run/docker.sock
RUN apt-get update
RUN apt-get install curl
RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh
RUN usermod -aG docker jenkins
USER jenkins
