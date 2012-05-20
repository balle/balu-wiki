########
Layer 2
########

* ein trunk port auf einer cisco ist nur dazu da, um vlan an einen switch oder router weiter zu reichen
* ein trunk port dient nicht dafuer einen normalen computer in mehrere vlan zu connecten!
* linux kann switch spielen und sich so an einem trunk port in jedes über diesen port geroutetes vlan einklinken

.. code-block:: bash

  vconfig eth0 add <vlan-id>
  ifconfig eth0.<vlan-id> <ip_aus_vlan> up

* wenn ein switch port auf dynamic desirable oder auto steht (man bekommt dtp packets), kann man den port wahlweise mit yersinia oder scapy in den trunk modus fuer alle vlan schalten

.. code-block:: bash

  from scapy.layers.l2 import Dot3 , LLC, SNAP
  from scapy.contrib.dtp import *
  scapy> negotiate_trunk(iface="eth0", mymac="7E:D4:DE:A5:45:21")

* das anschalten des trunk modes kann ein paar minuten dauern!
