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


Use old network device names
============================

* Start kernel with the parameters ``net.ifnames=0 biosdevname=0``
* Or disable automatic renaming in udev

.. code-block:: bash

  ln -s /dev/null /etc/udev/rules.d/80-net-setup-link.rules

* Or rename devices with udev

.. code-block:: bash

  cat > /etc/udev/rules.d/99-rename-to-eth0.rules << EOF
  SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="$(cat /sys/class/net/ens33/address)", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
  EOF


Availale parameters for kernel module
======================================

.. code-block:: bash

  modinfo <module_name>


Show current kernel boot parameters
===================================

.. code-block:: bash

  cat /proc/cmdline
