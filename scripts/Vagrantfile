Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.hostname = "devops-node"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.synced_folder "." , "/home/vagrant/devops-project"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision.yml"
  end
end
