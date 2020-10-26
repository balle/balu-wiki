#######
Network
#######

List available wifi networks 
=============================

.. code-block::

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

