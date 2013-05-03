#######
iproute
#######

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


Create a virtual interface
==========================

.. code-block:: bash

  ip link add type veth
  ip a add 1.2.3.4/24 dev veth0


A network interface with multiple mac addresses
================================================

.. code-block:: bash

  ip link add link eth0 dev peth0 type macvlan address aa:aa:aa:aa:aa:aa

