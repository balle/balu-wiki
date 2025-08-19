#######
Network
#######

List available wifi networks 
=============================

.. code-block:: bash

  airport -s

Join a wifi network
===================

.. code-block:: bash

  networksetup -setairportnetwork en0 SSID PASSWORD

Wifi monitor mode
=================

Monitor all traffic on channel 1

.. code-block:: bash

  airport en0 sniff 1

Turn wifi off
=============

.. code-block:: bash

  networksetup -setairportpower en0 off


View bluetooth information
==========================

.. code-block:: bash

  system_profiler SPBluetoothDataType


List active network connections
===============================

* And the corresponding processes

.. code-block:: bash

  lsof -i
  nettop
 
Pf logging
===========

 .. code-block:: bash

    sudo ifconfig pflog0 create 
    sudo tcpdump -n -e -ttt -i pflog0
    sudo ifconfig pflog0 destroy
    
