#######
Libvirt
#######

Installation
============

.. code-block:: bash

  yum install libvirt libvirtd python-virtinst qemu-kvm

Connect to a remote libvirtd via ssh
====================================

.. code-block:: bash

  virsh -c qemu+ssh://username@host/system

  
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


Info about a machine
====================

.. code-block:: bash

  virsh dominfo <machine-name>

  
Info about host system
======================

.. code-block:: bash

  virsh nodeinfo

  
Configure RAM
==============

.. code-block:: bash

  virsh setmem <machine-name> <kbyte>

Configure number of CPUs
========================

.. code-block:: bash

  virsh setvcpus <machine-name> <nr>

  
Update a machines config
========================

.. code-block:: bash

  virsh edit <machine-name>


Backup
======

* Save a machines CPU, RAM states

.. code-block:: bash

  virsh save <machine-name> <file>

* Take a snapshot (must be supported by disk image format)

.. code-block:: bash

  virsh snapshot-create <machine-name>
  
* Convert disk image

.. code-block:: bash

  qemu-img convert -f raw -O qcow2 yourdisk.img newdisk.qcow2

  
Migration
=========

* By default, migration only transfers in-memory state of a running domain (memory, CPU state, ...). Disk images are not transferred during migration but they need to be accessible at the same path from both hosts.
* Live migration needs shared network storage via NFS, iSCSI, GFS2 or Fibre Channel

.. code-block:: bash

  virsh migrate --live <machine-name> qemu://example.com/system


Performance overview
=====================

* Use ``virt-top``


Guest filesystem administration
===============================

* You can use ``guestfish`` to access a guests filesystem
* Mount / Umount filesystems
* Read / Write files
* Manage swap
* Configure partitions
* Execute commands on the shell etc


Scripting with Python2
======================

.. code-block:: python

  #! /usr/bin/env python2
  # -*- coding: utf-8 -*-
  import socket
  import sys
  import libvirt

  if (__name__ == "__main__"):
    conn = libvirt.open("qemu+ssh://xxx/system")
    print "Trying to find node on xxx"
    domains = conn.listDomainsID()

    for domainID in domains:
      domConnect = conn.lookupByID(domainID)
      print domConnect.name()


Troubleshooting
===============

* Intel virtualisation support must be activated in bios to use kvm
* Maybe Vbox modules should be unloaded
