##########
Filesystem
##########

Show used inodes
================

.. code-block:: bash

  df -i


Dont reserve 5% space for system
================================

.. code-block:: bash

  mke2fs -m 0


Find out filesystem of unmounted device
========================================

.. code-block:: bash

  parted -l /dev/sda
