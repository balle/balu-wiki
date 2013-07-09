###########
KVM / Qemu
###########

Create an image
===============

.. code-block:: bash

  qemu-img create -f qcow2 disk.img 4G

Install a machine
=================

.. code-block:: bash

  qemu-kvm -m 1024 -boot -once=d -cdrom cd.iso disk.img

Start a machine
===============

.. code-block:: bash

  qemu-kvm -m 1024 disk.img

Start qemu monitor
==================

.. code-block:: bash

  qemu-kvm -m 1024 disk.img -monitor stdin


Downloading disk images
=======================

* Grab an image from http://virtual-machine.org or http://virtualboximages.com/


Convert virtualbox or vmware image
==================================

.. code-block:: bash

  qemu-img convert -O qcow2 Platte.(vdi|vmdk) Platte.img

* http://qemu-buch.de/de/index.php/QEMU-KVM-Buch/_Speichermedien/_Festplatten-Images_anderer_Virtualisierungssoftware


Resize disk
===========

* Switch off machine
* Resize only disk image (filesystem left alone)

.. code-block:: bash

  qemu-img resize disk.img +10G

* Or create a new bigger image

.. code-block:: bash

  qemu-img create -f qcow2 new-disk.img 20G


Disk encryption
===============

* Create

.. code-block:: bash

  qemu-img create -e -f qcow2 disk.img 10G

* Convert

.. code-block:: bash

  qemu-img convert -e -O qcow2 disk.img disc-enc.img


