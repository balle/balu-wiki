#######
SELinux
#######

Overview
========

* .te -> type enforcement = allow rules, new types, user etc (used most of the time)
* .fc -> file context = define file context rules for module (<regexp> <security_context>)
* .if -> interfaces = macros


Update policy
=============

* Use a unique policy name otherwise it can clash with system internals and result in strange error messages

.. code-block:: bash

  grep qemu-system-x86 /var/log/audit/audit.log | audit2allow -M <policy_name>
  semodule -i <policy_name>.pp

* Or to allow all since the last policy change

.. code-block:: bash

  audit2allow -alR


Show all policy modules
=======================

.. code-block:: bash

  semodule -l


Get rid of a policy
===================

* Disable

.. code-block:: bash

  semodule -d <policy_name>

* Remove

.. code-block:: bash

  semodule -r <policy_name>


Write your own policy module
============================

* Allow rules have the definition ``allow <from_type> <to_type> : <object_class> {permissions};``
* Every type / attribute / class used and not defined in module must be required
* Choose a good name (not mypol) to avoid clashing with other predefined modules
* Copy Makefile from /usr/share/selinux/devel/

.. code-block:: bash

  policy_module(mypol, 1.0)

  require {
    type httpd_t;
  }

  type my_type;
  allow httpd_t my_type : file { getattr read };

* All object classes can be found in ``/usr/src/redhat/BUILD/serefpolicy-<version>/policy/flask/security_classes``
* All permissions for a class can be found in ``/usr/src/redhat/BUILD/serefpolicy-<version>/policy/flask/access_vectors``


Check policy module
===================

.. code-block:: bash

  checkmodule -m some.te


Compile a te file by hand
==========================

.. code-block:: bash

  make -f /usr/share/selinux/devel/Makefile some.pp


Search a policy rule
====================

.. code-block:: bash

  sesearch -A | grep <whatever>

* To see all allow rules with type httpd_t as source

.. code-block:: bash

  sesearch -a -s httpd_t


* or to see what a boolean / macro does (needs policy.conf see below)

.. code-block:: bash

  apol


Generate a policy skeleton
==========================

.. code-block:: bash

  sepolicy generate --application /usr/bin/firefox
  sepolicy generate --init /path/to/my/init-service


Booleans
========

* Show all booleans

.. code-block:: bash

  semanage boolean -l
  getselbool -a

* Set a boolean

.. code-block:: bash

  setsebool -P <boolean> <value>

* All local changes are in ``/etc/selinux/<policy>/modules/booleans.local``


Write your own boolean
=======================

.. code-block:: bash

  bool mybool <defaultvalue>;
  tuneable_policy(`mybool', `
    allow statements
  ');

* Name can be combined with || or && and other boolean names to activated this boolean only if condition is true


Managing file contexts
======================

* SE Linux stores the security context for files directly in the filesystem (currently ext{2,3,4}, XFS, JFS, Btrfs)
* Last rule matches
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

* Permanently set same context as other directory

.. code-block:: bash

  semanage fcontext -a -e /var/www /srv/www

* Delete a file context

.. code-block:: bash

  semanage fcontext -d <dir>

* Automatically relabel all files on next boot

.. code-block:: bash

  touch /.autorelabel


List all roles
==============

.. code-block:: bash

  seinfo -r


Change role
===========

.. code-block:: bash

  newrole -r system_r -t unconfined_t
  id -Z


Start a program in a specific role
==================================

.. code-block:: bash

  runcon system_u:system_r:crond_t:s0 /bin/bash


Configure users
===============

* List all users

.. code-block:: bash

  seinfo -u


* Map Unix user to SELinux user

.. code-block:: bash

  semanage login -a -s user_u <unix_user>
  semanage login -l

* Map SELinux user to roles

.. code-block:: bash

  semanage user -a -R "user_r sysadm_r" user_u
  semanage user -l


Log everything
==============

.. code-block:: bash

  semanage dontaudit off

* or

.. code-block:: bash

  semanage -DB


Reset base policy
=================

.. code-block:: bash

  semodule -B


Generate policy.conf (source file of your policy)
==================================================

* install src rpm of policy

.. code-block:: bash

  rpmbuild -bp selinux-policy.spec
  cd BUILD/serefpolicy-<version>

* Edit ``build.conf`` and set type to mcs, name to whatever, distro to redhat and monolithic to y

.. code-block:: bash

  make bare conf
  cp ../../SOURCES/boolean-targeted.conf policy/booleans.conf
  cp ../../SOURCES/modules-targeted.conf policy/modules.conf
  make policy.conf

* To make a module policy set MONOLITHIC=n and ``make base.pp`` instead of make policy.conf
* If apol complains it cannot load policy due to whatever failure just delete those line(s)


Configure Non-executable stack / heap
=====================================

.. code-block:: bash

  setsebool -P allow_execstack 0
  setsebool -P allow_execmem 0


Kernel parameter
================

.. code-block:: bash

  selinux=0|1
  enforcing=0|1
  autorelabel=0|1


Switch to MCS or MLS policy
===========================

* Install policy rpm
* Edit ``/etc/selinux/config``

.. code-block:: bash

  touch /.autorelabel
  reboot

* Boot with ``enforcing=0``
* Reboot after relabeling


Define new category
===================

* Edit ``/etc/selinux/targeted/setrans.conf``

.. code-block:: bash

  s0:c0=NotImportant
  s0:c100=VeryImportant

* Restart mcstrans


Change category of a user
=========================

.. code-block:: bash

  semanage login -a -r <category> <user>


Change category of file / dir
==============================

* Multiple categories are AND conditions

.. code-block:: bash

  chcat +|-<category> <file|dir>


Write your own macro
====================

.. code-block:: bash

  define(`macro_name', `allow $1 $2: file { getattr read }');


Domain transition
=================

.. code-block:: bash

  init_daemon_domain(myproc_t, myfile_exec_t)
  domain_auto_trans(unconfined_t, myfile_exec_t, myproc_t)
  auth_domtrans_chk_passwd(myproc_t)
  auth_domtrans_upd_passwd(myproc_t)


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


NFS / Mounting
===============

* Specify security context with mount parameter ``--context=<security_label>`` to have all files / dirs that security label or
* ``--defcontext=<security_label>`` to define a label just for those unlabeled


Temporarily disable / enable SELinux
====================================

.. code-block:: bash

  setenforce [0|1]


Audit Framework
================

* For permanent rules edit ``/etc/audit/audit.rules``

* Show current status

.. code-block:: bash

  auditctl -s

* Enable / disable audit

.. code-block:: bash

  auditctl -e 0/1

* Show all rules

.. code-block:: bash

  auditctl -l

* Delete all rules

.. code-block:: bash

  auditctl -D

* Log all execve calls of user root

.. code-block:: bash

  auditctl -a exit,always -S execve -F euid=0

* Log all executions of a specific program

.. code-block:: bash

  auditctl -A exit,always -F path=/path/to/executable -S execve

* Suppress all successful executions of some program

.. code-block:: bash

  auditctl -w /path/to/executable -F success=1

* Show all logs of a specific timespan and from a certain user

.. code-block:: bash

  ausearch --start month/day/year time --end month/day/year time -ui 0


* Show recent events (last 5 minutes)

.. code-block:: bash

  ausearch -ts recent


Documentation
=============

* http://www.selinuxproject.org/page/User_Resources
* http://www.admin-magazin.de/Online-Artikel/Mandatory-Access-Control-MAC-mit-SE-Linux
* http://magazine.redhat.com/2007/08/21/a-step-by-step-guide-to-building-a-new-selinux-policy-module/
* https://www.youtube.com/user/domg4721/videos
