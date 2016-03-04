#!/usr/bin/env bash

#install JDK
echo "Hello World !";
appName=simple
ROOT_PATH_OF_AWS=/home/ubuntu
VERSION=1.8.0_40
JDK_TARBALL=$ROOT_PATH_OF_AWS/Downloads/jdk-8u40-linux-x64.gz
INSTALL_DIR=$ROOT_PATH_OF_AWS/java
JAVA_HOME=$INSTALL_DIR/jdk$VERSION
TELEMETRY_1=javamelody.jar
TELEMETRY_2=jrobin-x.jar
sudo mkdir -p $INSTALL_DIR
sudo tar -zxvf $JDK_TARBALL -C $INSTALL_DIR
sudo echo "export JAVA_HOME=$JAVA_HOME">/etc/profile.d/jdk.sh
sudo echo 'export PATH=$PATH:$JAVA_HOME/bin'>>/etc/profile.d/jdk.sh

sudo echo "Defaults env_keep+=JAVA_HOME">>/etc/sudoers

echo "JDK installation was successful !";
# install tomcat

TOMCAT_TARBALL=$ROOT_PATH_OF_AWS/Downloads/apache-tomcat-8.0.21.tar.gz
INSTALL_DIR=$ROOT_PATH_OF_AWS/tomcat
CATALINA_HOME=$INSTALL_DIR/apache-tomcat-8.0.21
sudo mkdir -p $INSTALL_DIR
tar -zxvf $TOMCAT_TARBALL -C $INSTALL_DIR
sudo echo "export CATALINA_HOME=$CATALINA_HOME">/etc/profile.d/catalina.sh 

echo "Tomcat installation was successful !";
#install apache 


sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install -y apache2
sudo apt-get install -y libapache2-mod-proxy-html libxml2-dev
sudo apt-get install libapache2-mod-proxy-html a2enmod mod_proxy
sudo apt-get install sysv-rc-conf
echo "Apache installation was successful !";

# mod_proxy stuff 

sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_ajp
sudo a2enmod rewrite
sudo a2enmod deflate
sudo a2enmod headers
sudo a2enmod proxy_balancer
sudo a2enmod proxy_connect
sudo a2enmod proxy_html

service apache2 restart

# copy application in tomcat directory
sudo cp $ROOT_PATH_OF_AWS/JavaWebApplication/$appName.war $CATALINA_HOME/webapps/$appName.war
#sudo cp $ROOT_PATH_OF_AWS/telemetry/$TELEMETRY_1 $ROOT_PATH_OF_AWS/telemetry/$TELEMETRY_1/$TELEMETRY_2  $CATALINA_HOME/webapps/$appName/WEB-INF/lib
#cd $CATALINA_HOME/webapps/$appName/WEB-INF/lib
echo `ls -al`
cd $ROOT_PATH_OF_AWS 
# at last we are done 
echo "Mod proxy was enabled sucessfully " ;
echo "AWS EC2 Instance is ready for Apache, Tomcat, and Mod proxy !!" ;
echo "Author: Akond Rahman, akond.rahman.buet@gmail.com" ;