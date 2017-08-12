# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello"

  config.vm.define "victim" do |victim|
    victim.vm.box = "centos/7"
    victim.vm.network "private_network", ip: "172.0.0.1"
#TODO install Java 1.8, install a Spring-Boot app
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
     user.vm.network "private_network", ip: "172.0.0.4"i
 end

end
