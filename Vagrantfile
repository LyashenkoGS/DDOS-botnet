# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "victim" do |victim|
    victim.vm.box = "centos/7"
    victim.vm.network "private_network", ip: "172.0.0.1"
    # uncomment the line bellow during development and comment copying victim-server folder
    #Also, it requires vb-guest additions plugin
    #config.vm.synced_folder "victim-server/", "/victim-server"
    victim.vm.provision "shell", inline: "sudo systemctl stop firewalld"
    victim.vm.provision "shell", inline: "sudo systemctl disable firewalld"
    victim.vm.provision :file, source: 'victim-server/', destination: "/home/vagrant/victim-server"
    victim.vm.provision "shell", path: "victim-server/install-jdk8.sh"
    #start victim server on 8080 port
    victim.vm.provision "shell", path: "victim-server/build-and-run-victim.sh"
  end

  config.vm.define "attacker1" do |attacker1|
    attacker1.vm.box = "centos/7"
    attacker1.vm.network "private_network", ip: "172.0.0.2"
  end

 config.vm.define "attacker2" do |attacker2|
   attacker2.vm.box = "centos/7"
   attacker2.vm.network "private_network", ip: "172.0.0.3"
  end
  
 config.vm.define "user" do |user|
     user.vm.box = "centos/7"
     user.vm.network "private_network", ip: "172.0.0.4"
 end

end
