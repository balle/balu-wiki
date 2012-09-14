####
SNMP
####

* get all info

.. code-block:: bash

  snmpwalk -Os -c public -v 1 $host .

* print numeric OIDs

.. code-block:: bash

  snmpwalk -On -c public -v 1 $host .
  
* set a special info

.. code-block:: bash

  snmpset -c public -v 1 192.168.1.1 ipDefaultTTL.0 i 66

* Exceute command via snmp (in snmpd.conf)

.. code-block:: bash

  exec muh /some/command
