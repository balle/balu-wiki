####
IPMI
####

Overview
========

* Install freeipmi (http://www.gnu.org/software/freeipmi/documentation.html)
* Read http://www.thomas-krenn.com/de/wiki/IPMI_Grundlagen
* Check that your system has IPMI

.. code-block:: bash

  dmidecode | grep IPMI
  cat /proc/ipmi/0/stats
  ls /dev/ipmi0

* If you dont have ipmi0 

.. code-block:: bash

  modprobe ipmi_devintf


Configuration
=============

.. code-block:: bash

  bmc-config --checkout > ipmi.conf

* Edit ipmi.conf

.. code-block:: bash

  cat ipmi.conf | bmc-config --commit


Get sensor data
===============

* Local

.. code-block:: bash

  ipmi-sensors

* Remote

.. code-block:: bash

  ipmi-sensors -h $host -u $user -P

* More detailed and better parsable data

.. code-block:: bash

  ipmimonitoring -h $host -u $user -P


Get chassis status
==================

.. code-block:: bash

  ipmi-chassis -h $host -u $user -P -s


Power machine on / off
======================

.. code-block:: bash

  ipmipower --on -h $host -u $user -P


Activate chassis LED
====================

.. code-block:: bash

  ipmi-chassis -h $host -u $user -P -i 1
  

Read system event logs
======================

* General information

.. code-block:: bash

  ipmi-sel -h $host -u $user -P -i

* Real logs

.. code-block:: bash

  ipmi-sel -h $host -u $user -P 


Get serial console
==================

.. code-block::

  ipmiconsole -h $host -u $user -P
  
