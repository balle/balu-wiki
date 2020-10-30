##########
Forensics
##########

RAM dump
=========

* Use OSXPMem (only working till macOS 10.13 due to kernel extension)

.. code-block:: bash

  osxpmem /path/to/memdump.bin


Disk image
==========

* Either boot into rescue mode or from live usb / cd

.. code-block:: bash

  dd if=/dev/diskX of=container.img conv=noerror


Attach APFS container image
===========================

.. code-block:: bash

  hdiutil attach -nomount container.img

