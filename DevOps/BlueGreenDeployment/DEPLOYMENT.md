#Deployment Step    

###Automatic Deployment Configuration
 1. We used Vagrant to create the deployment environment automatically. We created a vagrant file and used the *vagrant-aws-plugin* to automatically upload and connect Vagrant with the AWS instance.

###Deployment of Binaries
 1. Whenever the application passes the build the binaries were deployed to the AWS instance using the provisioned script.  
 2. We configured the vagrant file so that it syncronizes with the application folder and deploy the application in the AWS instance. 
 3. The vagrant file was also *provisioned* to run a bash script so taht it isntalls the necessary dependencies to run the required application. Please see *install.sh* for details.          

###Remote Deployment
 1. We used Amazon AWS instances to perform remote deployment. See attached screenshot ofour simple app deployed on AWS instance. 
    ![canary-1](canary-1.png?raw=true=400x300)    

