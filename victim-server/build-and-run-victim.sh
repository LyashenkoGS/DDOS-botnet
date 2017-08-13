#!/usr/bin/env bash
#Builds and run a web server, requires $JAVA_HOME pointing to an Oracle JDK
cd /home/vagrant/victim-server
#disable a firewall
sudo systemctl stop
nohup ./mvnw spring-boot:run &> /home/vagrant/nohup.out &