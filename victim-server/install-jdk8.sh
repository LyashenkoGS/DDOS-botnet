#!/usr/bin/env bash
#Install JDK 1.8
yum update -y
yum install -y  wget
cd /tmp/
wget --progress=bar:force -c --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm
sudo yum  install -y jdk-8u131-linux-x64.rpm
echo "export JAVA_HOME=/usr/java/jdk1.8.0_131" >> ~/.bashrc
source ~/.bashrc
