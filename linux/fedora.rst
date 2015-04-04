######
Fedora
######

Restart network
===============

.. code-block:: bash
 
  systemctl restart NetworkManager.service

Allow SELinux exception
=======================

* Click on selinux alert in bottom right corner
* Click on Troubleshoot
* Paste solution as root


Disable boot logo
=================

.. code-block:: bash

  plymouth-set-default-theme details -R


Gnome3 settings
===============

* Install gnome-tweak-tool
* Install gconf-editor



Change login background
=======================

* Edit /usr/share/backgrounds/beefy-miracle/default/beefy-miracle.xml

Install flash plugin
====================

.. code-block:: bash

  rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-i386-1.0-1.noarch.rpm
  rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
  yum check-update
  yum install flash-plugin nspluginwrapper alsa-plugins-pulseaudio libcurl


Upgrade system
==============

* http://fedoraproject.org/wiki/Upgrading_Fedora_using_yum


