#!/usr/bin/env bash
canaryDir=./canaryForAWS/
address=http://54.69.80.87:8080/simple/
response=`curl -Is $address | head -1`
expectedResponse="HTTP/1.1 200 OK"
ROOT_PATH_OF_AWS=/home/ubuntu
INSTALL_DIR=$ROOT_PATH_OF_AWS/tomcat
CATALINA_HOME=$INSTALL_DIR/apache-tomcat-8.0.21




if [ -z "$response" ] ; then
   echo "Initially canary not working ";
else 
   echo "Our web application is running is just fine. ";
   echo "Time to deploy another canary ! ";  
   # another vagrant to run
   cd $canaryDir
       vagrant up --provider=aws
       vagrant reload --provision
       vagrant up --provider=aws
       vagrant ssh
           cd $CATALINA_HOME
              sudo ./bin/startup.sh
           cd $ROOT_PATH_OF_AWS   
       exit
   cd ..
fi