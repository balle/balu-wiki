########
Vagrant
########

Installation
============

* Via RPM / Deb see http://downloads.vagrantup.com/
* Via GEM

.. code-block:: bash

  gem install Vagrant


Libvirt support
===============

* You need at least version 1.1
* Install libvirt plugin 

.. code-block:: bash

  vagrant plugin install vagrant-libvirt

* Edit Vagrantfile

.. code-block:: bash

  Vagrant.configure("2") do |config|
    config.vm.define :test_vm do |test_vm|
      test_vm.vm.box = "centos64"
      test_vm.vm.network :private_network, :ip => '10.20.30.40'
    end

    config.vm.provider :libvirt do |libvirt|
      libvirt.driver = "qemu"
      libvirt.host = "localhost"
      libvirt.connect_via_ssh = true
      libvirt.username = "root"
      libvirt.storage_pool_name = "default"
    end
  end

* To start it 

.. code-block:: bash

  vagrant up --provider=libvirt

* Make libvirt default

.. code-block:: bash

  export VAGRANT_DEFAULT_PROVIDER=libvirt


Create custom libvirt box
=========================

* https://github.com/pradels/vagrant-libvirt/tree/master/example_box


Get boxes
=========

* http://www.vagrantbox.es
