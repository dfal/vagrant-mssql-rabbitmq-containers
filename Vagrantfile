# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

	config.vm.box = "ubuntu/xenial64"

	GB = 1024
	config.vm.provider "virtualbox" do |v|
		v.memory = 4*GB
	end

	config.vm.network :forwarded_port, guest: 15672, host: 15672, auto_correct: true
	config.vm.network :forwarded_port, guest: 4369, host: 4369,   auto_correct: true
	config.vm.network :forwarded_port, guest: 5672, host: 5672,   auto_correct: true
	config.vm.network :forwarded_port, guest: 1433, host: 1433,   auto_correct: true

	config.vm.network "private_network", ip: "192.168.50.4"

	config.vm.provision :docker
	config.vm.provision :docker_compose, rebuild: true, run: "always", yml: "/vagrant/docker-compose.yml"

end
