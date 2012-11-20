####
LDAP
####

Overview
========

* Data import are handled by ldif files
* Data structure is defined by schema files


Setting auth and email / calendar server
========================================

* Edit /etc/openldap/slapd.conf
* suffix is the start of the directory tree (usually the server name)
* rootdn defines the admin user
* rootpw sets the admins password (generated with slappasswd)

.. code-block:: bash

  include /etc/openldap/schema/nis.schema
  include /etc/openldap/schema/inetorgperson.schema

  suffix "dc=myserver,dc=mydomain,dc=tld"
  rootdn "cn=admin,dc=myserver,dc=mydomain,dc=tld"
  rootpw <password_ohash>


Test config file
================

.. code-block:: bash

  slaptest -u


Migrate passwd / group
======================

* Maybe you need to install migrationtools

.. code-block:: bash

  migrate_base.pl > base.ldif
  migrate_group.pl > group.ldif
  migrate_passwd.pl > passwd.ldif
  
  ldapadd -x -D "cn=admin,dc=myserver,dc=mydomain,dc=tld" -W -f base.ldif
  ldapadd -x -D "cn=admin,dc=myserver,dc=mydomain,dc=tld" -W -f group.ldif
  ldapadd -x -D "cn=admin,dc=myserver,dc=mydomain,dc=tld" -W -f passwd.ldif
