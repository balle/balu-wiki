#######
SELinux
#######

Update policy
=============

.. code-block:: bash

  grep qemu-system-x86 /var/log/audit/audit.log | audit2allow -M mypol
  semodule -i mypol.pp

List SELinux modules
====================

.. code-block:: bash

  semodule -l

  
Revoke a policy
===============

.. code-block:: bash

  semodule -r <name>


Show security context for a file
================================

.. code-block:: bash

  ls -Z <file>

* Context consists of user:role:type:level


Apache config
==============

* Allow webserver scripts to connect to the network

.. code-block:: bash

  setsebool -P httpd_can_network_connect 1

* For more see `man httpd_selinux`


Temporarily disable / enable SELinux
====================================

.. code-block:: bash

  setenforce [0|1]
