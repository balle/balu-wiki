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


Gnome-Keyring
=============

* To reset Gnome-Keyring passwords run

.. code-block:: bash

  rm ~/.gnome2/keyrings/*
