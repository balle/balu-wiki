######
Kernel
######

Find out which driver is in use
===============================

* network card

.. code-block:: bash

  ls -al /sys/class/net/eth5/device/driver/module

* generic

.. code-block:: bash

  lspci | grep VGA
  02:00.0 VGA compatible controller: Matrox Electronics Systems Ltd. MGA G200e [Pilot] ServerEngines (SEP1) (rev 02)

  find /sys | grep driver.*02:00

* or more easy

.. code-block:: bash

  lspci -vv


Availale parameters for kernel module
======================================

.. code-block:: bash

  modinfo <module_name>


Show current kernel boot parameters
===================================

.. code-block:: bash

  cat /proc/cmdline
