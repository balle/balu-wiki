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


Get a Python shell on the cluster
=================================

.. code:: python

  /opt/spark/bin/pyspark


Sample code
===========

* Sum up bytes of an apache acces log

.. code:: python

  log = sc.textFile("/var/log/httpd/access.log")                                                                                                                                                      
  log.map(lambda x: x.split(" ")[9]).filter(lambda x: "-" not in x).map(lambda x: int(x)).sum()


Add slave nodes
===============

.. code:: bash

  echo "root@host" >> /opt/spark/conf/slaves
  /opt/spark/bin/stop-all.sh
  /opt/spark/bin/start-all.sh
