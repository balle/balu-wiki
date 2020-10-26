#############################
Logging & system information
#############################

Show hardware information
=========================

.. code-block:: bash

  ioreg

* Or use apple icon / about this mac / system report


View system logs
================

Either use the GUI tool Console.app or

.. code-block:: bash

  log show 

* To show the log messages since the last boot

.. code-block:: bash

  log show --last boot

* To show the logs of the last x minutes/hours/days e.g. 1 minute

.. code-block:: bash

  log show --last 1m


Log locations
=============

==================== ============
Path                 Description
-------------------- ------------
/var/log/system.log  System Log 
/Library/Logs System Application Logs
~/Library/Logs User  Application Logs
==================== ============

