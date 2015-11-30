#!/usr/bin/env bash
canaryDir=canaryForDeployment
address=http://54.200.68.130:8080/simple/
canaryAddress=http://54.200.19.164:8080/simple/
response=`curl -Is $address | head -1`



if [ -z "$response" ] ; then
   echo "Primary canary not working ";
else 
   echo "Our web application is running is just fine on $address . See response below: ";
   echo $repsonse;
   echo "Time to deploy another canary ! ";  
   # another vagrant to run
   cd ../$canaryDir
       vagrant up --provider=aws
       vagrant reload --provision
       vagrant up --provider=aws
       vagrant ssh
   cd ..
   canaryResponse=`curl -Is $canaryAddress | head -1`
    if [ -z "$canaryResponse" ] ; then
       echo "Secondary canary not working ";
    else 
       echo "Our web application is running is just fine on $canaryAddress . See response below: ";
       echo $canaryResponse ;
    fi   
fi