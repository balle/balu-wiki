#######
Hadoop
#######

Overview
========

* Name node is the master or controller of the cluster
* Data nodes are the storage nodes for data
* Mapred nodes are the computing nodes


Configuration files
===================

==============  ===============================================================================
File            Description
--------------- -------------------------------------------------------------------------------
hadoop-env.sh   Environment variables
core-site.xml   Hadoop core settings
hdfs-site.xml   Settings for HDFS: namenode, secondary namenode, datanodes
mapred-site.xml Settings for MapReduce nodes
==============  ===============================================================================


Installation
============

* Install Java (at least 1.6.0!)
* Get Hadoop from http://hadoop.apache.org/common/releases.html#Download
* Unzip it e.g. in /opt
* Edit ``conf/hadoop-env.sh`` to set environment variables

.. code-block:: bash

  export JAVA_HOME=/usr/lib/jvm/jre-1.5.0-gcj

* Edit ``conf/core-site.xml`` to configure tmp dir and location of name node

.. code-block:: bash

  <property>
    <name>hadoop.tmp.dir</name>
    <value>/app/hadoop/tmp</value>
    <description>A base for other temporary directories.</description>
  </property>

  <property>
    <name>fs.default.name</name>
    <value>hdfs://localhost:54310</value>
    <description>The name of the default file system.  A URI whose
  scheme and authority determine the FileSystem implementation.  The
  uri's scheme determines the config property (fs.SCHEME.impl) naming
  the FileSystem implementation class.  The uri's authority is used to
  determine the host, port, etc. for a filesystem.</description>
  </property>


* Edit ``conf/mapred-site.xml`` to set the locations of the mapred nodes

.. code-block:: bash

  <property>
    <name>mapred.job.tracker</name>
    <value>localhost:54311</value>
    <description>The host and port that the MapReduce job tracker runs
  at.  If "local", then jobs are run in-process as a single map
  and reduce task.
    </description>
  </property>

* Create a hadoop user with an SSH key

.. code-block:: bash

  adduser hadoop
  su - hadoop
  ssh-keygen
  ssh-copy-id hadoop@localhost

* Format the HDFS

.. code-block:: bash

  bin/hadoop namenode -format

* Start all servers

.. code-block:: bash

  bin/start-all.sh
