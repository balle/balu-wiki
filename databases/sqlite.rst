######
Sqlite
######

Show tables and databases
=========================

.. code-block:: bash

  sqlite> .tables
  sqlite> .databases


Table schema
============

.. code-block:: bash

  sqlite> .schema <table>
  

Dump database or table
======================

.. code-block:: bash

  sqlite> .output /some/path/dump.sql
  sqlite> .dump
  sqlite> .dump <table>

  
Internal structure
==================

* .db files contain the database data
* .wal files (write ahead log) contain not written changes
* .shm files contain indeces

  
Forensic notes
==============

* .wal file contents get written when database is opened with sqlite3 tool
* deleted data may be still accessible in free pages. Free pages get cleared when database is opened with sqlite3 tool
