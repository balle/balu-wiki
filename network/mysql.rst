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
