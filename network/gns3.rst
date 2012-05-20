####
GNS3
####

Getting a console on a router 
==============================

* Drag and drop a router onto the working space
* Click on the play button (triangle)
* Right mouse click on the router -> console
* If the setup configruation after the first boot fails or freezes -> Dont panic!
* Delete the router
* Create a new one
* Skip first setup and configure it manually


Configure a Cisco Switch 
=========================

* switches must be simulated as a router
* cisco catalyst switches must use platform c3600 or c3700
* right click on the router -> configure
* in the slots tab choose NM-16ESW on slot1
* you only be able to start some catalyst images in gns3
  (see http://7200emu.hacki.at/viewtopic.php?t=6614)
* c3640-is-mz.123-14.T6.bin is known to be working as well


Configuring hosts 
==================

* Install a Qemu Linux (or whatever OS you desire) Image
  (or download one from http://wiki.qemu.org/Download#QEMU_disk_images)
* Goto Edit -> Preferences -> Qemu
* Check that the path of qemuwrapper.py is right
* Try to execute qemuwrapper.py
* If there are errors try to fix them
* On Arch linux you have to change python into python2 on the first line of the script
* Insert the path to your Qemu image in "Path to quemu-img"
* To test or manipulate Qemu images you can either mount it into your filesystem or
  start it with Qemu
* mount -n -o loop <path-to-qemu-image> /mnt
* qemu <path-to-qemu-image>
* for more information see http://en.wikibooks.org/wiki/QEMU/Images


Use your own Linux system as host os 
=====================================

* Download the ISO of your Linux distro as distro.iso
* Create a qemu harddisk
* qemu-img create linux.img 2G
* qemu -hda linux.img -cdrom distro.iso -boot -d -m 512


Links 
======

* http://anakappa.blogspot.com - Lots of great video tutorials regarding GNS3
