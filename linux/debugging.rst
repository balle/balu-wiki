#########
Debugging
#########

Create a core dump file
=======================

.. code-block:: bash

  ulimit -c unlimited


Read core dump file
===================

.. code-block:: bash

  gdb /path/to/application /path/to/corefile

