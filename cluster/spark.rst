####
Spark
####

Overview
========

* Configures like Hadoop 1
* Executing engine completly in RAM therefore lightning fast
* Can integrate with YARN
* Can use HDFS, S3, HBase, Cassandra, local files...
* Easier programming interface using resilient distributed dataset (RDD) - an immutable list distributed over the cluster 


Installation
============

* Unzip latest Spark prebuild for latest Hadoop (can also be used standalone)

.. code:: bash

  echo "root@some-slave-host" >> /opt/spark/conf/slaves
  /opt/spark/bin/start-all.sh



Get a Python shell on the cluster
=================================

.. code:: python

  /opt/spark/bin/pyspark


Sample code
===========

* Grep for failures in kern.log

.. code:: python

  log = sc.textFile("/var/log/kern.log")
  rrd = log.filter(lambda x: "error" or "failure" in x.lower())
  for x in rrd.collect(): print x

* Sum up bytes of an apache acces log

.. code:: python

  log = sc.textFile("/var/log/httpd/access.log")
  log.map(lambda x: x.split(" ")[9]).filter(lambda x: "-" not in x).map(lambda x: int(x)).sum()


Add slave nodes to a running cluster
====================================

* On the slave node execute

.. code:: bash

  /opt/spark/sbin/start-slave.sh some-worker-id spark://master-node:7077
