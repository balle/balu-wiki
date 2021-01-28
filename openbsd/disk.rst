=====================
 Disk and Filesystem
=====================

Filesystem tweaks
=================

* Configure soft updates everywhere (softdep)
* Disable access time logging (noatime)
* If possible mount with noexec, nosuid, nodev

.. code-block:: bash

  <duid> /home ffs rw,nodev,nosuid,noatime,softdep 1 2


NTFS
====

* Built-in NTFS support is read-only
* Install ntfs-3g from ports to get write support


List all available disks
========================

.. code-block:: bash

  sysctl hw.disknames


List all open files
===================

* For a PID

.. code-block:: bash

  fstat -p <PID>

* For a user

.. code-block:: bash

  fstat -u <user>

  
Display I/O throughput
=======================

.. code-block:: bash

  systat iostat


Create an encrypted image file
===============================

.. code-block:: bash

  dd if=/dev/zero of=my_encrypted.img bs=1m count=1024
  vnconfig -k /dev/vnd0c my_encrypted.img
  newfs /dev/vnd0

