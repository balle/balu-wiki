##########
Forensics
##########

RAM dump and analysis
=====================

* Use OSXPMem (only working till macOS 10.13 due to kernel extension)

.. code-block:: bash

  osxpmem /path/to/memdump.bin

* Another tool is Memoryze https://www.fireeye.com/services/freeware/memoryze.html (officially supports macos up to 10.8)
* To analyze a memory dump use Volatility https://www.volatilityfoundation.org


Syscall tracing
================

* You may have to disable system integrity protection to get the desired results
  
.. code-block:: bash

  dtruss -f -p <pid> -t <syscall>

* The following command enables system integrity protection without disabling dtrace used by dtruss 

.. code-block:: bash

  crsutil enable --without dtrace
  

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


Known wifi networks
===================

And their last connection timestamp can be found in /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist

To display the stored password

.. code-block:: bash

  security find-generic-password -ga <SSID_or_MAC_OF_ACCESS_POINT>


Known bluetooth devices
=======================

.. code-block:: bash

  plutil -p /Library/Preferences/com.apple.Bluetooth.plist

* Link keys can be found with

.. code-block:: bash

  plutil -p /private/var/root/Library/Preferences/com.apple.bluetoothd.plist
