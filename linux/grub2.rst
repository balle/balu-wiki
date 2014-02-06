#####
Grub2
#####

Overview
=========

* Setting can be found in ``/etc/default/grub``
* Menu entries are located in ``/etc/grub.d/`` as shell scripts (ordered by their number)
* Do not directly edit /boot/grub/grub.cfg that the main config but its created from the above
* To generate a basic config run

.. code-block:: bash

  grub-mkconfig -o /boot/grub/grub.cfg

* To install grub into MBR

.. code-block:: bash

  grub-install /dev/sda


Global Kernel parameter
========================

* Edit ``/etc/default/grub`` parameter ``GRUB_CMDLINE_LINUX``


Create a new Linux entry
========================

* Create a new script in ``/etc/grub.d`` e.g. 11_mylinux or edit ``40_custom``

.. code-block:: bash

  #!/bin/sh
  set -e

  menuentry "My Linux" {
    set root=(hd0,1)
    linux /vmlinuz (add other options here as required)
    initrd /initrd.img (if the other kernel uses/needs one)
  }

* Dont forget to make it executable!


Boot encrypted root with ramdisk
================================

.. code-block:: bash

  menuentry "My Linux" {
    set root=(hd0,1)
    linux /vmlinuz root=/dev/mapper/root cryptdevice=/dev/sda4:root
    initrd /initrd.img
  }


Boot encrypted root without ramdisk (untested)
==============================================

.. code-block:: bash

  menuentry "My Linux" {
    insmod gzio
    insmod part_gpt
    insmod cryptodisk
    insmod luks
    insmod gcry_twofish
    insmod gcry_sha256

    cryptomount -u <uuid>

    insmod lvm
    insmod ext2

    set root='lvm/vg-root'
    linux /vmlinuz root=/dev/mapper/vg-root
  }


Boot Windows
============

* Create a new script in ``/etc/grub.d`` e.g. 99_windows

.. code-block:: bash

  #!/bin/sh

  menuentry "Windows XP" {
    set root="(hd0,3)"
    chainloader +1
  }


Boot only signed kernel and ramdisk
===================================

* Generate gpg keypair
* Sign kernel

.. code-block:: bash

  gpg --detach-sign vmlinuz

* Edit Grub config

.. code-block:: bash

  trust boot.key
  set check_signatures=enforce


Booting a rescue cd image
=========================

.. code-block:: bash

  menuentry "SYSRESCUECD" {
    set iso=/systemrescuecd-x86-3.8.1.iso
    loopback loop ${iso}
    linux  (loop)/isolinux/rescue64 nomodeset vga=791 docache setkmap=fr isoloop=${iso}
    initrd (loop)/isolinux/initram.igz
  }


Convert grub1 menu.lst to grub2 config
======================================

.. code-block:: bash

  grub-menulst2cfg /boot/grub/menu.lst /boot/grub/grub.cfg
