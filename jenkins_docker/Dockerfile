FROM jenkins:1.609.1
MAINTAINER akondrahman

User root 
RUN apt-get update && apt-get install -y wget git curl zip

# loggging 
RUN mkdir /var/log/jenkins



# for main web interface 
EXPOSE 8080


# settign environment variables
ENV JAVA_OPTS="-Xmx8192m"
ENV JENKINS_OPTS="--handlerCountStartup=100 --handlerCountMax=300"


