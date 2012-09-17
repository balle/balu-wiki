####
SNMP
####

get all info
============

.. code-block:: bash

  snmpwalk -Os -c public -v 1 $host .

print numeric OIDs
==================

.. code-block:: bash

  snmpwalk -On -c public -v 1 $host .
  
set a special info
==================

.. code-block:: bash

  snmpset -c public -v 1 192.168.1.1 ipDefaultTTL.0 i 66

Exceute command via snmp (in snmpd.conf)
========================================

.. code-block:: bash

  exec muh /some/command

Install a new MIB file
=======================

* Copy the file (e.g. MY-MIB.txt) to /usr/share/snmp/mibs

.. code-block:: bash

  snmpwalk -Of -v 1 -c public -m +MY-MIB 192.168.1.1 .
  
Translate a MIB to its number
=============================

* maybe you need to delete the last .0

.. code-block:: bash

  snmptranslate -m ALL -On <mib>
  
