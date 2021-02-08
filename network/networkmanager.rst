###############
NetworkManager
###############

List devices
============

.. code-block:: bash

  nmcli d

  
List connections
================

.. code-block:: bash

  nmcli c

Start / stop a connection
=========================

.. code-block:: bash

  nmcli c up/down <connection>


Scan for wifi networks
=======================

.. code-block:: bash

  nmcli d wifi list


Add a new ethernet connection
=============================

.. code:: bash

  nmcli con add con-name my-eth1 ifname eth1 type ethernet ip4 192.168.100.100/24 gw4 192.168.100.1

  
Add a new wifi connection
=========================

.. code-block:: bash

  nmcli con add con-name MyCafe ifname wlan0 type wifi ssid MyNet
  nmcli con modify MyNet wifi-sec.key-mgmt wpa-psk
  nmcli con modify MyNet wifi-sec.psk 'password'


Add OpenVPN config file
========================

.. code-block:: bash

  nmcli connection import type openvpn file /etc/openvpn/client/crb.conf
  
  
Applet
======

.. code-block:: bash

  nm-applet --sm-disable


Edit connections
================

.. code-block:: bash

  nm-connection-editor
