##########
Forensics
##########

RAM dump
=========

* Use OSXPMem (only working till macOS 10.13 due to kernel extension)

.. code-block:: bash

  osxpmem /path/to/memdump.bin

* Another tool in Memoryze https://www.fireeye.com/services/freeware/memoryze.html
* To analyze a memory dump use Volatility https://www.volatilityfoundation.org


Syscall tracing
================

* You may have to disable system integrity protection to get the desired results
  
.. code-block:: bash

  dtruss -f -p <pid> -t <syscall>


Disk image
==========

* Either boot into rescue mode or from live usb / cd

.. code-block:: bash

  dd if=/dev/diskX of=container.img conv=noerror


Attach APFS container image
===========================

.. code-block:: bash

  hdiutil attach -nomount container.img
  mount -o rdonly,noexec,noowners /dev/diskX /Volumes/Container

