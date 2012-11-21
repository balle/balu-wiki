####
LDAP
####

Overview
========

* Data imports are handled by ldif files
* Data structure is defined by schema files


Basic setup
===========

* Edit /etc/openldap/slapd.conf
* suffix is the start of the directory tree (usually the server name)
* rootdn defines the admin user
* rootpw sets the admins password (generated with slappasswd)

.. code-block:: bash

  include /etc/openldap/schema/core.schema
  include /etc/openldap/schema/cosine.schema
  include /etc/openldap/schema/nis.schema
  include /etc/openldap/schema/inetorgperson.schema

  suffix "dc=myserver,dc=mydomain,dc=tld"
  rootdn "cn=admin,dc=myserver,dc=mydomain,dc=tld"
  rootpw <password_hash>


Test config file
================

.. code-block:: bash

  slaptest -u


Migrate passwd / group
======================

* Maybe you need to install migrationtools

.. code-block:: bash

  migrate_base.pl > base.ldif
  migrate_group.pl /etc/group > group.ldif
  migrate_passwd.pl /etc/passwd > passwd.ldif

* Edit ldif files and change ``dc=padl,dc=com`` to ``dc=myserver,dc=mydomain,dc=tld``
* Maybe you have to delete the first entry of base.ldif because the root dn already exists
  
  ldapadd -x -D "cn=admin,dc=myserver,dc=mydomain,dc=tld" -W -f base.ldif
  ldapadd -x -D "cn=admin,dc=myserver,dc=mydomain,dc=tld" -W -f group.ldif
  ldapadd -x -D "cn=admin,dc=myserver,dc=mydomain,dc=tld" -W -f passwd.ldif


Dump database
=============

.. code-block:: bash

  ldapsearch -x -D "cn=admin,dc=myserver,dc=mydomain,dc=tld" -W -b "dc=myserver,dc=mydomain,dc=tld"


Migrate from 2.3 to 2.4
=======================

* Use ``/usr/lib/openldap/convert-config.sh`` to convert old slapd.conf to new cn=config format
