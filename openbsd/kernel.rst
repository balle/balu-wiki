#######
Kernel
#######

Permanently disable kernel features like ACPI
==============================================

.. code-block:: bash

  mv /bsd /bsd.old
  config -e -o /bsd /bsd.old
  ukc>disable acpi
  ukc>quit


Tracing kernel calls
====================

* Comparable to strace on Linux

.. code-block:: bash

  ktrace -t cn <program>
  kdump | less


