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


Create index
============

.. code-block:: bash

  db.<collection>.ensureIndex( { myfield: 1 } );
