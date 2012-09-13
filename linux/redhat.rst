######
Redhat
######

Service Configuration
=====================

* List all available services and their status

.. code-block:: bash

  chkconfig --list


* Turn service on boot on or off

.. code-block:: bash

  chkconfig <service> [on|off]


* Start or stop a service

.. code-block:: bash

  service <service> [start|stop]


Firewall Config
===============

* Prefered tool is ``system-config-firewall``
* or lokkit

.. code-block:: bash

  lokkit -p 80:tcp
  lokkit -s http

* Script can be found under ``/etc/sysconfig/iptables`` but will be overwritten by the commands above


Bridged interface
=================

* /etc/sysconfig/network-scripts/ifcfg-br0

.. code-block:: bash

  DEVICE=br0
  TYPE=Bridge
  BOOTPROTO=dhcp
  ONBOOT=yes
  DELAY=0

* /etc/sysconfig/network-scripts/ifcfg-eth0

.. code-block:: bash

  BRIDGE=br0


Kickstart
=========

* The kickstart file used to setup the system can be found in /root/anaconda-ks.cfg

  
Gnome-Keyring
=============

* To reset Gnome-Keyring passwords run

.. code-block:: bash

  rm ~/.gnome2/keyrings/*


Setting up a chroot environment
===============================

.. code-block:: bash

  mkdir -p /data/redhat/var/cache/yum/x64_64/\$releaseserver
  cp /etc/yum.repos.d/redhat.repo /data/redhat/var/cache/yum/x64_64/\$releaseserver
  yum --disablerepo=* --enablerepo=redhat --disableplugin=* --installroot=/data/redhat install bash
  
