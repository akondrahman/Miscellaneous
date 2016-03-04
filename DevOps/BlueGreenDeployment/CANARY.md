##Canary Release and Analysis

 1. We used another bash script 'scripts/canary.sh' to check if the first isntance is running properly. We performed this check using the *curl* command to get a HTTP response and check if the deployed application is running. 
 2. Using the same script we triggered another instance with all the necessary dependencies and the environment if the status from step-1 was 'OK'. The canary deployment is shown below as a screenshot. 
   ![canary2](canary-2.png?raw=true=400x300)  
       

