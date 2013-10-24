#######
SELinux
#######

Overview
========

Update policy
=============

* Use a unique policy name otherwise it can clash with system internals and result in strange error messages

.. code-block:: bash

  grep qemu-system-x86 /var/log/audit/audit.log | audit2allow -M mypol
  semodule -i mypol.pp


Booleans
========

* Show all booleans

.. code-block:: bash

  getsebool -a

* Set a boolean

.. code-block:: bash

  setsebool -P <boolean> <value>

Managing file contexts
======================

* SE Linux stores the security context for files directly in the filesystem (currently ext{2,3,4}, XFS, JFS, Btrfs)
* Show file context

.. code-block:: bash

  ls -Z

* Show all context rules

.. code-block:: bash

  semanage fcontext -l

* Set new file context rule

.. code-block:: bash

  semanage fcontext -a -t mysqld_db_t '/some/dir(/.*)?'

* Reset context rules for dir

.. code-block:: bash

  restorecon -RFvv /some/dir

* Copy context

.. code-block:: bash

  chcon -R --reference=/old/dir /new/dir


Compile a te file by hand
==========================

.. code-block:: bash

  make -f /usr/share/selinux/devel/Makefile some.pp


Log everything
==============

.. code-block:: bash

  semanage dontaudit off


Mysql config
============

* Change datadir

.. code-block:: bash

  semanage fcontext -a -t mysqld_db_t '/new/dir/mysql(/.*)?'
  restorecon -RFvv /new/dir/mysql/

* For more see `man mysqld_selinux`


Apache config
==============

* Allow cgi scripts

.. code-block:: bash

  setsebool -P httpd_enable_cgi 1

* Allow webserver scripts to connect to the network

.. code-block:: bash

  setsebool -P httpd_can_network_connect 1

* Run apache on non-standard port

.. code-block:: bash

  semanage port -l | grep http
  semanage port -a -t http_port_t -p tcp 8888

* For more see `man httpd_selinux`


Temporarily disable / enable SELinux
====================================

.. code-block:: bash

  setenforce [0|1]
