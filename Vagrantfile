# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.hostname = "skeletons"
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.synced_folder ".", "/home/vagrant/skeletons"

  #config.vm.network :forwarded_port, guest: 80, host: 7000
  config.vm.network :private_network, ip: "192.168.123.11"

  # Give root user access to your ssh forward agent keys
  config.vm.provision :shell do |shell|
    shell.inline = "touch $1 && chmod 0440 $1 && echo $2 > $1"
    shell.args = %q{/etc/sudoers.d/root_ssh_agent "Defaults    env_keep += \"SSH_AUTH_SOCK\""}
  end

  # Allow pulling from private repos: https://help.github.com/articles/generating-ssh-keys
  #
  # - Make sure key added: `ssh-add -L`
  # If not: `ssh-add -k ~/.ssh/id_rsa`
  #
  # - or Add following to ~/.ssh/config:
  #   Host vagrant.*
  #   ForwardAgent yes
  #
  # Verify within Vagrant: `ssh -T git@github.com`
  config.ssh.forward_agent = true

  config.vm.provider "virtualbox" do |vb|
    vb.name = "skeletons"
    vb.memory = 512
    vb.customize ["modifyvm", :id, "--cpus", "2"]
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "deployment/provisioning/vagrant.yml"
    ansible.inventory_path = "deployment/provisioning/hosts-vagrant"
    ansible.verbose = false
  end

end
