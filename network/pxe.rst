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

  ks=http://192.168.1.23/centos-kickstart.cfg
