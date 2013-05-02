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

* Via ISO file

.. code-block:: bash

  virt-install --name="TestVM" --os-type=linux --ram=512 --disk path=test-vm.img,size=20 --cdrom <path-to-iso-file>

* Using PXE

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

* To shutdown a machine it must have acpid running


Autostart a machine
===================

.. code-block:: bash

  virsh autostart <machine-name>


Info about a machine
====================

.. code-block:: bash

  virsh dominfo <machine-name>


Info about host system
======================

.. code-block:: bash

  virsh nodeinfo

Connect to a machine
====================

* ``virt-viewer`` or ``virt-manager``


Rename a machine
================

.. code-block:: bash

  virsh dumpxml <machine-name> > muh.xml
  <edit muh.xml, change the name>
  virsh undefine <machine-name>
  virsh define muh.xml


Attach a cdrom image
====================

.. code-block:: bash

  virsh attach-disk <machine-name> <iso-file> hdc --type cdrom --mode readonly

Update boot order
=================

* First dump machine settings as XML

.. code-block:: bash

  virsh dumpxml <machine-name> > blah.xml

* Edit XML file
* Update machine settings

.. code-block:: bash

  virsh define <machine-name> blah.xml


Configure RAM
==============

.. code-block:: bash

  virsh setmem <machine-name> <kbyte>

Configure number of CPUs
========================

.. code-block:: bash

  virsh setvcpus <machine-name> <nr>


Resize disk
===========

* Switch off machine
* Resize only disk image (filesystem left alone)

.. code-block:: bash

  qemu-img resize disk.img +10G

* Or create a new bigger image

.. code-block:: bash

  qemu-img create -f qcow2 new-disk.img 20G

* and convert old image to new one and expand sda2 to max size

.. code-block:: bash

  virt-resize --expand /dev/sda2 old-disk.img new-disk.img


Update a machines config
========================

.. code-block:: bash

  virsh edit <machine-name>


Backup
======

* Save a machines RAM state to a file

.. code-block:: bash

  virsh save <machine-name> <file>

* Take a snapshot of disk and ram (must be supported by disk image format e.g. qcow2 and this will PAUSE the machine)

.. code-block:: bash

  virsh snapshot-create <machine-name>

* or by using qemu tools (but only when vm is off!)

.. code-block:: bash

  qemu-img snapshot -c my-backup disk.img
  qemu-img snapshot -l disk.img

* Another possibility is to install libguestfs-tools and create a tar archive of /

.. code-block:: bash

  virt-tar -z -x <machine_name> / machine-backup.tgz


Restore
=======

.. code-block:: bash

  virsh snapshot-revert <machine_name> <snapshot>


Convert disk image
==================

.. code-block:: bash

  qemu-img convert -f raw -O qcow2 yourdisk.img newdisk.qcow2


Disk tricks
===========

* Install libguestfs-tools

.. code-block:: bash

  virt-df
  virt-df -d <machine_name>

* Get content of a file

.. code-block:: bash

  virt-cat -d <machine_name> <filename>

* Edit a file (vm must be off)

.. code-block:: bash

  virt-edit -d <machine_name> <filename>

* Or even get a shell on a disk image

.. code-block:: bash

  guestfish \
            add disk.img : run : mount /dev/vg_guest/lv_root / : \
                      write /etc/resolv.conf "nameserver 8.8.8.8"


Disk encryption
===============

* Create

.. code-block:: bash

  qemu-img create -e -f qcow2 disk.img 10G

* Convert

.. code-block:: bash

  qemu-img convert -e -O qcow2 disk.img disc-enc.img


Cloning
=======

* Will copy a whole machine and its properties and gives it a new mac address
* The machine must be switched off

.. code-block:: bash

  virt-clone -o <machine-name> -n <new-machine-name>


Migration
=========

* By default, migration only transfers in-memory state of a running domain (memory, CPU state, ...). Disk images are not transferred during migration but they need to be accessible at the same path from both hosts.
* Live migration needs shared network storage via NFS, iSCSI, GFS2 or Fibre Channel

.. code-block:: bash

  virsh migrate --live <machine-name> qemu://example.com/system


Performance overview
=====================

* Use ``virt-top``


Performance tuning
==================

* Use virtio driver for disk and net this will give a machine direct hardware access (no emulation - only for linux guests)
* Maybe you have to load the kernel modules

.. code-block:: bash

  modprobe virtio_blk
  modprobe virtio_net
  modprobe virtio_pci

* If one dont want to use snapshots use `raw` as image type
* Use `Writethrough` as caching type


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
* Use `virt-rescue` (from libguestfs-tools) as live-rescue system

.. code-block:: bash

  virt-rescue -d <machine_name>


KVM
===

* Create an image

.. code-block:: bash

  qemu-img create -f qcow2 disk.img 4G

* Install a machine

.. code-block:: bash

  qemu-kvm -m 1024 -boot -once=d -cdrom cd.iso disk.img

* Start a machine

.. code-block:: bash

  qemu-kvm -m 1024 disk.img

* Start qemu monitor

.. code-block:: bash

  qemu-kvm -m 1024 disk.img -monitor stdin

