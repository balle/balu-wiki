#############
Open vSwitch
#############

Overview
========

* Consists of a daemon and a database server that stores the switch config in json
* You can use a kernel daemon for better performance
* A port is a bridge


Create a new port
==================

.. code-block:: bash

  ovs-vsctl add-br br0
  ovs-vsctl add-port br0 eth0
  ovs-vsctl show


Connect a vm to a port
=======================

* Use `virsh edit <vm>` to update network config and set

.. code-block:: bash

  <interface type='bridge'>
    <mac address='52:54:00:71:b1:b6'/>
    <source bridge='br0'/>
    <virtualport type='openvswitch'/>
    <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
  </interface>


Limit an interface to 1 MBit
============================

.. code-block:: bash

  ovs-vsctl set Interface tap0 ingress_policing_rate=1000
  ovs-vsctl set Interface tap0 ingress_policing_burst=100


Set a port into a VLAN
======================

.. code-block:: bash

  ovs-vsctl set port <port name> tag=<VLAN ID>


Bonding
=======

.. code-block:: bash

  ovs-vsctl add-br ovsbr1
  ovs-vsctl add-bond ovsbr1 bond0 eth1 eth3


Get information
===============

* About the switch overall

.. code-block:: bash

  ovs-vsctl show

* A port

.. code-block:: bash

  ovs-vsctl list port

* An interface 

.. code-block:: bash

  ovs-vsctl list interface


