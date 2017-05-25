# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

	config.vm.box = "ubuntu/trusty64"

	config.vm.provider "virtualbox" do |v|
		v.memory = 4096
	end

	config.vm.network :forwarded_port, guest: 15672, host: 15672, auto_correct: true
	config.vm.network :forwarded_port, guest: 4369, host: 4369,   auto_correct: true
	config.vm.network :forwarded_port, guest: 5672, host: 5672,   auto_correct: true
	config.vm.network :forwarded_port, guest: 1433, host: 1433,   auto_correct: true

	config.vm.network "private_network", ip: "192.168.50.4"

	#config.vm.provision "docker" do |d|
	#	d.pull_images "library/rabbitmq"
	#	d.run "library/rabbitmq",
	#		args: "-h rabbithost -p 0.0.0.0:5672:5672 -p 0.0.0.0:15672:15672"
	#end
	
	config.vm.provision :docker
	config.vm.provision :docker_compose, rebuild: true, run: "always", yml: "/vagrant/docker-compose.yml"

end
