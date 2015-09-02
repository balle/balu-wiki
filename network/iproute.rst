#######
iproute
#######

Simple stuff
============

* Set device up and give it an ip

.. code-block:: bash

  ip l s <dev> up/down
  ip a add <ip> <netmask> dev <dev>
  ip a sh dev <dev>
 
* Remove one IP

.. code-block:: bash

  ip a del <ip> dev <dev>

* Remove all ips

.. code-block:: bash

  ip a flush dev eth0

* Show routing table

.. code-block:: bash

  ip r

* Configure default gateway

.. code-block:: bash

  ip route add default via 192.168.1.254

* Arp table

.. code-block:: bash

  ip n


* Show interface statistics for packets and errors

.. code-block:: bash

  ip -s l sh dev eth0


Change MAC
==========

.. code-block:: bash

  ip link set <dev> addr <mac>


Promisc mode
===========

.. code-block:: bash

  ip link set dev eth0 promisc on


Source routing
==============

* Different default gateway depending on source address

.. code-block:: bash

  ip route add $P1_NET dev $IF1 src $IP1 table T1
  ip route add default via $P1 table T1
  ip route add $P2_NET dev $IF2 src $IP2 table T2
  ip route add default via $P2 table T2


Load balancing
==============

.. code-block:: bash

  ip route add default scope global nexthop via $P1 dev $IF1 weight 1 \
    nexthop via $P2 dev $IF2 weight 1


Show routes of ipsec tunnel
===========================

.. code-block:: bash

  ip xfrm policy
  ip xfrm state


Create a virtual interface
==========================

.. code-block:: bash

  ip link add type veth
  ip a add 1.2.3.4/24 dev veth0


A network interface with multiple mac addresses
================================================

.. code-block:: bash

  ip link add link eth0 dev peth0 type macvlan address aa:aa:aa:aa:aa:aa


Network namespaces
==================

* http://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/
* With network namespaces, you can have different and separate instances of network interfaces and routing tables that operate independent of each other.
* Only virtual network interfaces can be assigned to a network namespace and they always come in pairs connected peer-to-peer. One device for the default namespace to be connected to the physical interface by bridge and one to assign to the network namespace

.. code-block:: bash

  ip netns add balle
  ip netns list
  ip link add veth0 type veth peer name veth1
  ip link set veth1 netns balle
  brctl addbr balle_br
  brctl addif balle_br eth0 veth0
  ip netns exec balle ip addr add 192.168.100.1/24 dev veth1
  dhclient balle_br

* Now you can start a process or a shell if you like to use the new network namespace

.. code-block:: bash

  ip netns exec balle bash

* Monitor namespaces

.. code-block:: bash

  ip netns monitor
