######
Spark
######

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


Status Overview
===============

* Point your web browser to http://<yourmasternode>:8080
* Run example 

.. code:: bash

  bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://127.0.0.1:7077 \
  --executor-memory 1G \
  --total-executor-cores 1 \ 
  lib/spark-examples-1.1.1-hadoop2.4.0.jar \
  1000               


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


Troubleshooting
===============

* Be sure if remotely submiting jobs to use the DNS name and not IP
* ``TaskSchedulerImpl: Initial job has not accepted any resources; check your cluster UI to ensure that workers are registered and have sufficient memory``


Monitoring
==========

* http://www.hammerlab.org/2015/02/27/monitoring-spark-with-graphite-and-grafana/
