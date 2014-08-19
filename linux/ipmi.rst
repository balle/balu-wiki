####
IPMI
####

Overview
========

* Install freeipmi (http://www.gnu.org/software/freeipmi/documentation.html) or ipmitool
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
  ipmitool sdr list

* Remote

.. code-block:: bash

  ipmi-sensors -h $host -u $user -P
  ipmitool sdr list -H $host -U $user -P

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
  ipmitool power reset -H $host -U $user


Activate chassis LED
====================

.. code-block:: bash

  ipmi-chassis -h $host -u $user -P -i 1


Read system event logs
======================

* General information

.. code-block:: bash

  ipmi-sel -h $host -u $user -P -i
  ipmitool sel elist

* Real logs

.. code-block:: bash

  ipmi-sel -h $host -u $user -P


Configure network for remote console
====================================

.. code-block:: bash

  ipmitool lan set 2 ipaddr $IP
  ipmitool lan set 2 netmask 255.255.255.0
  ipmitool lan set 2 defgw ipaddr $GW
  ipmitool lan print 2


Configure user
==============

.. code-block:: bash

  ipmitool user set name <userid> balle
  ipmitool user set password <userid> ""

* admin privs

.. code-block:: bash

  ipmitool channel setaccess 1 <userid> link=on ipmi=on callin=on privilege=4
  ipmitool channel setaccess 2 <userid> link=on ipmi=on callin=on privilege=4

* user privs

.. code-block:: bash

  ipmitool channel setaccess 1 <userid> link=on ipmi=on callin=on privilege=2
  ipmitool channel setaccess 2 <userid> link=on ipmi=on callin=on privilege=2

* dont forget to enable the user

.. code-block:: bash

  ipmitool user enable <userid>


Get serial console
==================

.. code-block::

  ipmiconsole -h $host -u $user -P


Restart ipmi controller
=======================

.. code-block:: bash

  ipmitool bmc reset cold


Check that ipmi controller is ok
================================

.. code-block:: bash

  ipmitool bmc selftest
