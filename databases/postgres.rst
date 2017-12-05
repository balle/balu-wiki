########
Postgres
########

Create a database
==================

.. code-block:: bash

  createdb mydb -E UTF8 -O myuser

* or

.. code-block:: bash

  CREATE DATABASE mydb WITH OWNER mypuser;

* By default this will copy template1 db


Create a user
==============

.. code-block:: bash

  createuser --password myuser

* or

.. code-block:: bash

  CREATE USER myuser WITH password 'secret';


Change user password
=====================

.. code-block:: bash

  ALTER USER myuser WITH PASSWORD 'moresecret';

Change user permissions
========================

.. code-block:: bash

  ALTER USER myuser CREATEDB;

Delete user
============

.. code-block:: bash

  dropuser myuser


* or

.. code-block:: bash

  DROP USER myuser

List databases
===============

.. code-block:: bash

  \l

Connect to a database
======================

.. code-block:: bash

  \c <db>

List all tables
================

.. code-block:: bash

  \dt


Describe table
==============

.. code-block:: bash

  \d+ table


List user and permissions
==========================

.. code-block:: bash

  \du


Show active connections
=======================

.. code-block:: bash

  SELECT * FROM pg_stat_activity;


Export select as CSV
====================

.. code-block:: bash

  copy(select * from table) to '/some/file' with csv header;


Import CSV
==========

.. code-block:: bash

  copy table from '/some'file' with csv header;

Backup / Restore
================

* Backup in binary format

.. code-block:: bash

  pg_dump -F c -b -U user database > backup.dump

* Restore

.. code-block:: bash

  pg_restore --disable-triggers -U user -d database backup.dump

* If you want to disable all constraints for data import

.. code-block:: bash

  echo "SET CONSTRAINTS ALL DEFERRED;" | psql

* And to enable contraints

.. code-block:: bash

  echo "SET CONSTRAINTS ALL IMMEDIATE;" | psql


Show all trigger of a table or view
===================================

.. code-block:: bash

  select * from pg_trigger where tgrelid = 'schema.table'::regclass;

* Schema name can be looked up in output of `\d`

* To get the source code of a trigger use

.. code-block:: bash

  select p.prosrc from pg_trigger t join pg_proc p on p.oid=t.tgfoid where t.tgname = 'RI_ConstraintTrigger_a_130239';

* Or all together

.. code-block:: bash

  select t.*, p.prosrc from pg_trigger t join pg_proc p on p.oid=t.tgfoid where t.tgrelid = 'schema.table'::regclass;


Show all functions
==================

.. code-block:: bash

  \df+


Import SQL file
================

* Beside `psql < sqlfile` there is the possibility to use

.. code-block:: bash

  \i sqlfile


Change output format
====================

.. code-block:: bash

  \x on
