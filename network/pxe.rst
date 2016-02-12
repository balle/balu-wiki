####
PXE
####

Installation
============

* DHCP server
* TFTP server
* Syslinux


Setup DHCP
==========

* next-server is the ip address of the tftp server
* filename points to syslinux image

.. code-block:: bash

  option domain-name-servers 8.8.8.8;
  default-lease-time 86400;
  max-lease-time 604800;
  log-facility local7;
  authoritative;

  subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.150;
    filename "pxelinux.0";        # the PXELinux boot agent
    nextserver 192.168.1.23;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.1.255;
    option routers 192.168.1.1;
  }


Setup TFTP and Syslinux
=======================

.. code-block:: bash

  cp /usr/lib/syslinux/pxelinux.0 /var/tftpboot/
  cp /usr/lib/syslinux/menu.c32 /var/tftpboot/
  cp /usr/lib/syslinux/memdisk /var/tftpboot
  cp /usr/lib/syslinux/mboot.c32 /var/tftpboot/
  cp /usr/lib/syslinux/chain.c32 /var/tftpboot
  mkdir /var/tftpboot/pxelinux.cfg
  mkdir -p /var/tftpboot/images/CentOS

* Download ISO image (e.g. CentOS)
* http://mirror.switch.ch/ftp/mirror/centos/6.3/isos/i386/CentOS-6.3-i386-minimal.iso
* Copy kernel and ramdisk from ISO image

.. code-block:: bash

  mount -o loop CentOS-6.3-i386-bin-DVD1.iso /mnt/
  cp /mnt/images/pxeboot/* /var/tftpboot/images/CentOS
  umount /mnt

* Create file /var/tftpboot/pxelinux.cfg/default

.. code-block:: bash

  DEFAULT menu.c32
  PROMPT 0
  MENU TITLE Balle sein PXE Main Menu

  console 0
  serial 0 115200 0

  LABEL CentOS
    MENU LABEL ^CentOS
    KERNEL images/CentOS/vmlinuz
    APPEND initrd=images/CentOS/initrd.img ksdevice=eth0 console=ttyS0,115200 earlyprint=serial,ttyS0,115200 ramdisk_size=9025


Optionally kickstart setup
==========================

* Install a webserver (e.g. nginx)
* Create kickstart file (/srv/http/web/centos-kickstart.cfg)

.. code-block:: bash

  install
  url --url http://mirror.centos.org/centos/5/os/i386
  lang de_DE.UTF-8
  keyboard de
  network --device eth0 --bootproto dhcp
  rootpw test123
  firewall --enabled --ssh
  authconfig --enableshadow --enablemd5
  selinux --enforcing
  timezone --utc Europe/Zurich
  bootloader --location=mbr
  reboot

  # Partitioning
  clearpart --all --drives=sda
  part /boot --fstype ext3 --size=100 --ondisk=sda
  part pv.2 --size=0 --grow --ondisk=sda
  volgroup VolGroup00 --pesize=32768 pv.2
  logvol / --fstype ext3 --name=LogVol00 --vgname=VolGroup00 --size=1024 --grow
  logvol swap --fstype swap --name=LogVol01 --vgname=VolGroup00 --size=256 --grow --maxsize=512

  %packages
  @core
  openssh
  openssh-clients
  openssh-server

* Edit /var/tftpboot/pxelinux.cfg/default and append to the APPEND line

.. code-block:: bash

  ks=http://<ip_of_pxe_server>/centos-kickstart.cfg


Install clonezilla images
=========================

* Unzip clonezilla zip into ``/var/lib/tftpboot/images/clonezilla``
* Edit ``/var/tftpboot/pxelinux.cfg/default`` and for manual installtion append

.. code-block:: bash

  LABEL Clonezilla
      MENU LABEL Clonezilla
      APPEND initrd=clonezilla/live/initrd.img boot=live config noswap nolocales edd=on nomodeset ocs_live_run="ocs-live-general" ocs_live_extra_param="" keyboard-layouts="" ocs_live_batch="no" locales="" vga=788 nosplash noprompt fetch=tftp://<ip_of_pxe_server>/pxe/clonezilla/live/filesystem.squashfs
      KERNEL clonezilla/live/vmlinuz

* for full-automatic installion append

.. code-block:: bash

  LABEL Clonezilla
      MENU LABEL Clonezilla
      APPEND initrd=images/clonezilla/live/initrd.img boot=live config noswap nolocales edd=on nomodeset ocs_live_run="/usr/sbin/ocs-sr --batch -q -e1 auto -e2 -r -j2 -p reboot restoredisk $IMAGENAME sda" ocs_live_extra_param="" ocs_live_keymap="NONE" ocs_live_batch="yes" ocs_lang="en_US.UTF-8" vga=788 nosplash noprompt ocs_prerun="mount -t nfs -o vers=3 <ip_of_pxe_server>:/local/clonezilla /home/partimag" ocs_postrun="$POST_COMMAND && reboot" fetch=tftp://<ip_of_pxe_server>/images/clonezilla/live/filesystem.squashfs
      KERNEL clonezilla/live/vmlinuz

* Make sure to replace $POST_COMMAND, $IMAGENAME, /path/to/image and the ip of your pxe server
* Virtio disks can also be a problem make sure to use normal disks in vms


Diskless Redhat
===============

* Install dracut and dracut-network
* Edit ``/etc/dracut.conf`` and make sure the following is set

.. code-block:: bash

  add_dracutmodules+="nfs"

* Also add network kernel modules to ``add_drivers+``
* Build initramdisk

.. code-block:: bash

  dracut initramfs-3.10.0-327.4.5.el7.x86_64 3.10.0-327.4.5.el7.x86_64
  lsinitrd initramfs-3.10.0-327.4.5.el7.x86_64

* Create minimal root filesystem

.. code-block:: bash

  yum groupinstall Base --installroot=/export/diskless-el7
  yum install openssh-server openssh-clients --installroot=/export/diskless-el7

* Make sure there is a network config file for your card e.g. ``/export/diskless-el7/etc/sysconfig/network-scripts/ifcfg-eno0``

.. code-block:: bash

  DEVICE=eno0
  NAME=eno0
  BOOTPROTO=dhcp
  ONBOOT=yes

* Create ``/export/diskless-el7/etc/fstab``

.. code-block:: bash

  none            /tmp            tmpfs   defaults        0 0
  tmpfs           /dev/shm        tmpfs   defaults        0 0
  sysfs           /sys            sysfs   defaults        0 0
  proc            /proc           proc    defaults        0 0
  none            /var/log        tmpfs   defaults        0 0
  none            /var/run        tmpfs   defaults        0 0
  none            /var/lock       tmpfs   defaults        0 0
  none            /var/tmp        tmpfs   defaults        0 0
  none            /var/spool      tmpfs   defaults        0 0

* Set default target to multi-user instead of graphical

.. code-block:: bash

  rm -f /export/diskless-el7/etc/systemd/system/default.target
  ln -s ../../../usr/lib/systemd/system/multi-user.target /export/diskless-el7/etc/systemd/system/de

* Create some links to files or dirs that otherwise want to be writable

.. code-block:: bash

  ln -s etc/ld.so.cache~ tmp/ld.so.cache~
  ln -s etc/udev/hwdb.bin tmp/hwdb.bin
  mkdir tmp/catalog; ln -s var/lib/systemd/catalog tmp/catalog
  ln -s etc/machine-id /tmp/machine-id

* Generate ssh host keys for the image

.. code-block:: bash

  mount -o bind /dev /export/diskless-el7/dev
  chroot /export/diskless-el7
  ssh-keygen -A
  exit
  umount /export/diskless-el7/dev

* Copy your public key into the image

.. code-block:: bash

  mkdir /export/diskless-el7/root/.ssh
  cat ~/.ssh/id_rsa.pub > /export/diskless-el7/root/.ssh/authorized_keys

* Delete unneeded services

.. code-block:: bash

  cd /export/diskless-el7/etc/systemd/multi-user.target.wants
  rm -f abrt* atd.service crond.service chronyd.service firewalld.service kdump.service libstoragemgmt.service rhel-dmesg.service rhsmcertd.service rngd.service sysstat.service

* Edit ``/var/tftpboot/pxelinux.cfg/default`` and add

.. code-block:: bash

  LABEL  rhel7
     KERNEL diskless/vmlinuz-3.10.0-327.4.5.el7.x86_64
     APPEND initrd=diskless/initramfs-3.10.0-327.4.5.el7.x86_64 root=nfs:<ip_to_nfs_server>:/export/diskless-el7:nfsvers=3 ip=dhcp netdev=boot


Fedora netinstall
=================

* Download lkrn from https://boot.fedoraproject.org/download
* Edit ``/var/tftpboot/pxelinux.cfg/default`` and add

.. code-block:: bash

  LABEL  Fedora
  MENU LABEL boot.fedoraproject.org
  IPAPPEND 2
  KERNEL linux/bfo.lkrn
