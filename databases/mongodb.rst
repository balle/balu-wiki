#########
Mongo Db
#########

Overview
========

* You dont need to create users / passwords / dbs or tables just use it
* Programming language is Javascript


List all databases
==================

.. code-block:: bash

  show dbs

Connect to a db
===============

.. code-block:: bash

  use <db>

List all collections
====================

.. code-block:: bash

  show collections


Insert data
===========

.. code-block:: bash

  db.<collection>.save({name: "wurst", firstname: "hans"})


* Import in json format

.. code-block:: bash

  cat json_file | /usr/bin/mongoimport --type json -d mydb -c mycollection


Select from collection
======================

* all

.. code-block:: bash

  db.<collection>.find()

* filter by field

.. code-block:: bash

  db.<collection>.find(field: "value")

* filter by regexp

.. code-block:: bash

  db.<collection>.find(field: /\d+/)

* select specific fields

.. code-block:: bash

  db.<collection>.find({},{"field_to_select": 1})


Iterate over all results
========================

.. code-block:: bash

  var cursor = db.<collection>.find();
  while (cursor.hasNext()) printjson(cursor.next());


* Or better

.. code-block:: bash

  db.<collection>.find().forEach(printjson)


Sorting
=======

* Lowest first

.. code-block:: bash

  db.<collection>.find().sort({"field": 1})

* Highest first

.. code-block:: bash

  db.<collection>.find().sort({"field": -1})


Update data
===========

.. code-block:: bash

  db.<collection>.update({"_id": 1}, {$set: {"field": "new value"}})


Delete data
===========

* Remove complete collection

.. code-block:: bash

  db.<collection>.drop()

* Remove some entries

.. code-block:: bash

  db.<collection>.remove({"name": "wurst"})

* Delete a field

  db.<collection>.update({"_id": 1}, {$unset: {"field": ""}})
  
.. code-block:: bash
  
* Delete whole database

.. code-block:: bash

  db.dropDatabase()


Working with timestamps
=======================

* Get all entries from 1.12. till 6.12.

.. code-block:: bash

  db.snmp.find({'time': {'$gt': ISODate('2012-12-01T00:00:00'), '$lt': ISODate("2012-12-05T23:59:59")}})

Select distinct values
======================

.. code-block:: bash

  db.<collection>.distinct('field')


Create index on collection field
================================

* sparse will only create index if a value for that field exists

.. code-block:: bash

  db.<collection>.ensureIndex( { myfield: 1 }, {sparse: true, background: true} );

* Unique constraint

.. code-block:: bash

  db.<collection>.ensureIndex( { myfield: 1 }, {unique: true} );


Show indexes
==========================

* Of collection

.. code-block:: bash

  db.<collection>.getIndexes()

* All

.. code-block:: bash

  db.system.indexes.find()


Replication
============

* MongoDB has automatically master / slave failover buildin!
* You need at least 3 server
* Edit ``/etc/mongodb.conf`` and set a replSet

.. code-block:: bash

  replSet = rs0

* On the master node execute the folowing in mongo shell

.. code-block:: bash

  rs.initiate()
  rs.conf()
  rs.add("mongodb1.example.net")
  rs.add("mongodb2.example.net")
  rs.status()

  
Show real data size
===================

* With indizes

.. code-block:: bash

  db.<collection>.totalSize()

* Only data

.. code-block:: bash

  db.<collection>.dataSize()


Defrag
======

* Whole database

.. code-block:: bash

  db.repairDatabase()

* Single collection

.. code-block:: bash

  db.<collection>.compact()


Load collection into memory
===========================

.. code-block:: bash

  db.runcommand({ touch: “collection_name”, data: true, index: true})


Round robin collections
=======================

If you've not heard of capped collections before, they're a nice little feature of MongoDB that lets you have a high-performance circular queue. Capped collections have the following nice features:

* They "remember" the insertion order of their documents
* They store inserted documents in the insertion order on disk
* They remove the oldest documents in the collection automatically as new documents are inserted

.. code-block:: bash

  db.create_collection(
    'capped_collection',
    capped=True,
    size=size_in_bytes,     # required
    max=max_number_of_docs, # optional
    autoIndexId=False)      # optional

* One can tail for new data in capped collections

.. code-block:: bash

  cur = db.capped_collection.find(
        tailable=True,
        await_data=True)

* For more see http://blog.pythonisito.com/2013/04/mongodb-pubsub-with-capped-collections.html


Getting help
============

.. code-block:: bash

  db.help()


