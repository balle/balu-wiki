#####
MySQL
#####

Create new user
===============

.. code-block:: sql

  grant all privileges on db.* to user@'%' identified by 'passwd'; 


Show extended table information
================================

.. code-block:: sql

  show table status;


Show table structure
====================

.. code-block:: sql

  describe <table>
  

Show indices
============

.. code-block:: sql

  show index from <table>


Show all running processes
==========================

.. code-block:: sql

  show full processlist;


Kill a process
==============

.. code-block:: sql

  kill <pid>;


Repair a table
==============

.. code-block:: sql

  repair table <table>;


Backup whole database
=====================

.. code-block:: bash

  mysqldump <db> > backup.sql

  
Selective backup
================

.. code-block:: sql

  select * into dumpfile "backup.sql" from table where foo="bar";


Create database with utf-8 charset
==================================

.. code-block:: sql

  create database <db_name> default character set utf8;

* Or edit my.cnf

.. code-block:: bash

  [mysqld]
  default-character-set = utf8
  
  [mysql]
  default-character-set = utf8

Use InnoDB tables instead of MyISAM
====================================

* Edit my.cnf

.. code-block:: bash

  default-storage-engine=INNODB

Change db charset
=================

.. code-block:: sql

  alter database <db_name> character set utf8;
  

Add Foreign Key Contraint
==========================

.. code-block:: sql

  alter table add constraint <contraint_name> foreign key <column> references <table> <column> on delete cascade;

Add check constraint
====================

.. code-block:: sql

  alter table add constraint <name> CHECK (some_column > 0 and other_column != "");
  
Add index
=========

.. code-block:: sql

  create index <name> on <table> (<column>);
  
Delete entries older than 30 days
=================================

.. code-block:: sql

  DELETE FROM <table> WHERE DATE_SUB(CURDATE(),INTERVAL 30 DAY) <= <column>;
  
