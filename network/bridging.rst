#########
Bridging
#########

Overview
========

* Bridging creates a virtual switch
* A bridge can handle STP (be aware of it!)
* Usually the bridge uses a physical interface like eth0 as uplink


Setup
=====

* Install bridge-utils
* Add a new bridge interface

.. code-block:: bash

  brctl addbr br0

* Add uplink

.. code-block:: bash


  brctl addif br0 eth0

* Add other ports
* Show config

.. code-block:: bash

  brctl show

* Remember to disable STP if you dont need it!

.. code-block:: bash

  brctl stp br0 off

* Switch of network-manager
* Here how a bridge can be automatically configured with RHEL/CentOS/Fedora

.. code-block:: bash

  DEVICE=br0
  TYPE=Bridge
  ONBOOT=yes
  DELAY=0
  BOOTPROTO=static
  IPADDR=192.168.100.1
  NETMASK=255.255.255.0
  STP=off

* And how to add eth0 as uplink

.. code-block:: bash

  BRIDGE=br0
  NM_CONTROLLED=no


Firewalling
===========

* To disable firewalling between bridge ports check `/proc/sys/net/bridge/bridge-nf-call-*`
