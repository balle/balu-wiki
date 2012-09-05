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

* /etc/sysconfig/iptables


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

  
Gnome-Keyring
=============

* To reset Gnome-Keyring passwords run

.. code-block:: bash

  rm ~/.gnome2/keyrings/*
