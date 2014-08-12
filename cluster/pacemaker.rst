##########
Pacemaker
##########

Setup
=====

* Run these commands on all nodes

.. code-block:: bash

  yum install pacemaker pcs
  passwd hacluster
  corosync-keygen

* Copy ``/etc/corosync/authkey`` to all nodes

* Open UDP port 5405
* Setup the cluster

  systemctl start corosync
  systemctl start pacemaker
  systemctl start pcsd
  pcs cluster auth node1 node2 node3
  pcs cluster setup --name my-cluster node1 node2 node3

* Edit ``/etc/corosync/corosync.conf`` and set

.. code-block:: bash

  secauth: on
  crypto_cipher: aes256
  crypto_hash: sha512

* Restart corosync

.. code-block:: bash

  systemctl restart corosync
  pcs cluster start
  pcs cluster enable
  pcs cluster status


Create a shared floating ip
===========================

.. code-block:: bash

  pcs resource create ha-ip ocf:heartbeat:IPaddr2 params ip="192.168.3.3" cidr_netmask="32" op monitor interval="10s"


Show all resources
==================

.. code-block:: bash

  pcs resource show


Set mandatory fencing off
=========================

.. code-block:: bash

  pcs property set stonith-enabled=false


Configure fencing via IPMI
==========================

* Install ``fence-agents`` on every node

.. code-block:: bash

  pcs stonith create node1 fence_ipmilan params auth="password" ipaddr="1.2.3.4" login="root" passwd="secret" pcmk_host_list="node1" op monitor interval="30s"
  pcs stonith create node2 fence_ipmilan params auth="password" ipaddr="1.2.3.4" login="root" passwd="secret" pcmk_host_list="node2" op monitor interval="30s"

* To test it execute

.. code-block:: bash

  pcs stonith fence another-node


Configure fencing for libvirtd
==============================

* On libvirt node install ``fence-virtd``

.. code-block:: bash

  mkdir /etc/cluster
  dd if=/dev/urandom of=/etc/cluster/fence_xvm.key bs=4k count=1
  semanage boolean -m --on fenced_can_network_connect
  systemctl enable fence_virtd
  systemctl start fence_virtd

* On all nodes install ``fence-virt`` and copy ``/etc/cluster/fence_xvm.key`` to them
* On all nodes and host allow tcp and udp to port ``1229``
* On one node test fencing and enable it afterwards

.. code-block:: bash

  fence_xvm -o list -a 225.0.0.12
  pcs stonith create ha-fence fence_xvm multicast_address=225.0.0.12 pcmk_host_list="node1 node2 node3"


Enable / disable a resource
============================

.. code-block:: bash

  pcs resource enable/disable <resource>


Maintenance a node
==================

* On the node exec

.. code-block:: bash

  pcs cluster standby


Reset logs of a resource
========================

.. code-block:: bash

  pcs resource cleanup <resource>


Debug a resource
================

.. code-block:: bash

  pcs resource debug-start <resource>


Move a resource to another node
================================

.. code-block:: bash

  pcs resource move <resource> <node>


Define a service
================

* Cloned means the service runs on all nodes, no clone only one node
* mongodb is a name for the resource, mongod the name of the init script / systemd service

.. code-block:: bash

  pcs resource create mongodb lsb:mongod --clone

* For systemd services

.. code-block:: bash

  pcs resource create myhaproxy systemd:mongod


Define a mountpoint
===================

.. code-block:: bash

  pcs resource create my-nfs Filesystem device=192.168.1.1:/export/something directory=/mnt fstype=nfs options=nolock


Group resources
===============

.. code-block:: bash

  pcs resource group add my-group resource1 resource2


Define constraints
==================

* Start order

.. code-block:: bash

  pcs constraint order start <resource1> then <resource2>

* Ensure both resources are on the same node

.. code-block:: bash

  pcs contraint colocation add <resource1> with <resource2>

* Prefered node

.. code-block:: bash

  pcs contraint location <resource> prefers <node>

* Delete a contraint (without with or then or prefers...)

.. code-block:: bash

  pcs contraint [colocation|...] remove <resource1> <resource2>


Setup a 2 node cluster
======================

* Normally an odd number greater than 1 is used to build a cluster to form a valid quorom

.. code-block:: bash

  pcs resource clone lsb:httpd globally-unique=true clone-max=2 clone-node-max=2
