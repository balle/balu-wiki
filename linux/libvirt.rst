#######
Libvirt
#######

Installation
============

.. code-block:: bash

  yum install libvirt libvirtd python-virtinst qemu-kvm

Create a machine
================

* Configure bridged interface br0
* Create a virtual machine with 20 gb disk and 512 mb ram

.. code-block:: bash

  virt-install --name="TestVM" --os-type=linux --os-variant=rhel6 --network bridge=br0,mac=aa:bb:cc:aa:bb:cc --ram=512 --disk path=test-vm.img,size=20 --pxe
  
Remove a machine
================

.. code-block:: bash

  virsh undefine <machine-name>
  
  
List all virtual machines
=========================

.. code-block:: bash

  virsh list

Start or stop a machine
=======================

.. code-block:: bash

  virsh start <machine-name>
  virsh shutdown <machine-name>
  virsh destroy <machine-name>

  
Troubleshooting
===============

* Intel VXE support must be activated
* Vbox modules must be unloaded
