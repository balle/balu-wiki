###
sar
###

CPU
===

* Every 10 seconds

.. code:: bash
  
  sar 10

* Every 60 seconds for 5 minutes

.. code:: bash
  
  sar 60 5

* Show single cores

.. code:: bash
  
  sar -P ALL


Load
====

.. code:: bash
  
  sar -q


Mem and swap
=============

.. code:: bash
  
  sar -rS


Disk
====

.. code:: bash
  
  sar -bd


Network
=======

.. code:: bash
  
  sar -n ALL


Inodes and file descriptors
===========================

.. code:: bash
  
  sar -v

Processes
==========

.. code:: bash
  
  sar -w


Continuos monitoring
=====================

.. code:: bash

  /usr/lib/sa/sadc 60 -

* Logs can now be found in /var/log/sa
* Show all logs from current day

.. code:: bash
  
  sar -f -

