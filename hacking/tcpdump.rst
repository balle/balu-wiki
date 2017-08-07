########
Tcpdump
########

Show RST packets on all interfaces
==================================

.. code-block:: bash

  tcpdump -i any -n -v 'tcp[tcpflags] & (tcp-rst) != 0'

Sniff wifi traffic without beacons, probe requests and responses
=================================================================

.. code-block:: bash

  tcpdump -y IEEE802_11_RADIO not subtype beacon and not subtype probereq and not subtype proberesp
