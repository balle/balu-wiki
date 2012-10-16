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


Security context
=================

* Context consists of user:role:type:level

* Show for a file

.. code-block:: bash

  ls -Z <file>

* Show for a running process

.. code-block:: bash

  ps -eZ

* Show for current user

.. code-block:: bash

  id -Z

* Copy from reference to target file

.. code-block:: bash

  chcon --reference=some_file target_file

* Restore vendor context

.. code-block:: bash

  restorecon reset file_or_dir

Booleans
=========

.. code-block:: bash

  getsebool -a


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


More doc
========

* http://www.selinuxproject.org/page/Recipes
