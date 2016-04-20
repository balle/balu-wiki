##########
Cassandra
##########

Overview
========

  * Cassandra is a partitioned row store database (Db split over whole cluster)
  * Replication for HA
  * Designed from the ground up as a distributed database with peer-to-peer communication (No Master node)
  * Feels lot like MySQL
  * Cassandra Demo App https://github.com/snazy/barker


Specifics
=========

  * Update of non-existent data row will insert it as new, Insert of existing data row will update it
  * Select WHERE clause only possible for indexed fields (or by appending ALLOW FILTERING)


Start CQL Client
================

.. code-block:: bash

  bin/cqlsh


Create new database
===================

.. code-block:: bash

  cqlsh> CREATE KEYSPACE app WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
  cqlsh> use app;


Create new table
================

.. code-block:: bash

  cqlsh:app> CREATE TABLE users (username TEXT PRIMARY KEY, firstname TEXT, surname TEXT, password BLOB, last_login TIMESTAMP);


INSERT, UPDATE, SELECT, DELETE
===============================

.. code-block:: bash

  cqlsh:app> INSERT INTO users (username, firstname, surname) VALUES ('balle', 'Sebastian', 'Ballmann') IF NOT EXISTS;
  cqlsh:app> UPDATE users SET firstname='Bastian' WHERE username = 'balle';
  cqlsh:app> SELECT username, last_login FROM users WHERE surname='Ballmann' ALLOW FILTERING;
  cqlsh:app> DELETE FROM users WHERE username='balle';


Create a cluster
================

* Edit ``conf/cassandra.yaml``
* Set at least the Cluster name and listen_address
* Include all nodes in seed provider list
* Start cassandra on all nodes
* Check cluster status

.. code-block:: bash

  bin/nodetool status


Import data from MySQL
======================

* Install squoop (http://sqoop.apache.org/)

.. code-block:: bash

  sqoop import --connect jdbc:mysql://127.0.0.1/dev --username root --cassandra-keyspace dev --cassandra-create-schema
