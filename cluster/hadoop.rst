#######
Hadoop
#######

Overview
========

* Name node is the master or controller of the HDFS (currently only one possible!)
* Data nodes are the storage nodes for data
* Mapred nodes are the computing nodes
* HDFS splits files into file block (128 Mb by default) which are split up into storage blocks (512 kb) and keeps distributed copies (3 by default)
* JobTracker is the controller of Map reduce
* A job consists of a number of tasks
* TaskTracker runs on every data node to receive a computation task
* Hadoop moves the computation to the data instead of vice versa
* ``bin/slaves.sh`` allows you to execute a command on all slave nodes


Configuration files
====================

* Default values can be looked up in ``conf/hadoop-defaults.xml``
* Config options can be combined in ``conf/hadoop-site.xml``

================== =====================================================================
File               Description
================== =====================================================================
hadoop-env.sh      Environment variables
hadoop-policy.xml  ACL for various Hadoop services
core-site.xml      Hadoop core settings
hdfs-site.xml      Settings for HDFS: namenode, secondary namenode, datanodes
mapred-site.xml    Settings for MapReduce nodes
masters            Contains the hostname of the SecondaryNameNode
slaves             Lists every ndoe which should start TaskTracker and DataNode daemons
================== =====================================================================


Network ports
=============

* These are the tcp ports to open in your firewall

===== =================== ================================
Port  Description         Config parameter
===== =================== ================================
50070 Name node           dfs.http.address
50075 Data node           dfs.datanode.http.address
50090 Secondary Name node dfs.secondary.http.address
50030 Job tracker         mapred.job.tracker.http.address
50060 Task tracker        mapred.task.tracker.http.address
===== =================== ================================


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
  <property>
    <name>hadoop.security.authorization</name>
    <value>true</value>
  </property>

* Edit ``conf/mapred-site.xml`` to set the locations of the job tracker and its working dir

.. code-block:: bash

  <property>
    <name>mapred.job.tracker</name>
    <value>localhost:54311</value>
    <description>The host and port that the MapReduce job tracker runs
  at.  If "local", then jobs are run in-process as a single map
  and reduce task.
    </description>
  </property>

  <property>
    <name>mapreduce.jobtracker.staging.root.dir</name>
    <value>/user</value>
  </property>

* Edit ``conf/hdfs-site.xml`` to set working dirs of name and data node and how often a file gets replicated

.. code-block:: bash

  <property>
    <name>dfs.replication</name>
    <value>1</value>
    <description>Default block replication.
    The actual number of replications can be specified when the file is created.
    The default is used if replication is not specified in create time.
    </description>
  </property>
  <property>
    <name>dfs.data.dir</name>
    <value>/hadoop/data</value>
  </property>
  <property>
    <name>dfs.name.dir</name>
    <value>/hadoop/name</value>
  </property>

* Create a hadoop user with an SSH key

.. code-block:: bash

  useradd -d /opt/hadoop hadoop
  chown -R hadoop /opt/hadoop
  su - hadoop
  ssh-keygen
  cat .ssh/id_rsa.pub > .ssh/authorized_keys
  chmod 400 .ssh/authorized_keys
  ssh localhost

* Format the HDFS

.. code-block:: bash

  bin/hadoop namenode -format

* Start all servers

.. code-block:: bash

  bin/start-all.sh

* Test the installation

.. code-block:: bash

  bin/hadoop jar hadoop-examples-1.2.1.jar pi 2 10


Configure HDFS
==============

* Config file is ``conf/hdfs-site.xml`` or ``conf/hadoop-site.xml``

=========================== ======================================================
Config option               Description
=========================== ======================================================
fs.default.name             The URI for the name node e.g. hdfs://namenode:9000
dfs.data.dir                Directory where data node stores its stuff
dfs.name.dir                Directory where name node stores its stuff
dfs.block.size              Changes the file block size
dfs.namenode.handler.count  Nr of threads for name node to handle data nodes
=========================== ======================================================


Working with HDFS
=================

* Access to the name node via http://localhost:50070

* Mkdir

.. code-block:: bash

  hadoop dfs -mkdir some_dir

* Copy a file to hdfs

.. code-block:: bash

  hadoop dfs -copyFromLocal file.txt some_dir
  hadoop dfs -put file.txt some_dir

* List a directory

.. code-block:: bash

  hadoop dfs -ls some_dir

* Copy a file on HDFS

.. code-block:: bash

  hadoop dfs -cp file.txt test.txt

* Remove a file

.. code-block:: bash

  hadoop dfs -rm test.txt

* Show file contents

.. code-block:: bash

  hadoop dfs -cat file.txt

* Retrieve a file

.. code-block:: bash

  hadoop dfs -get file.txt local_file.txt

* In python

.. code-block:: bash

  cat = subprocess.Popen(["hadoop", "fs", "-cat", "/path/to/myfile"], stdout=subprocess.PIPE)
  for line in cat.stdout:
    print line


* Export HDFS via NFS, see https://github.com/cloudera/hdfs-nfs-proxy/wiki/Quick-Start


Configure Map Reduce
====================

* Config file is ``conf/mapred-site.xml`` or ``conf/hadoop-site.xml``

======================================== ======================================================
Config option                            Description
======================================== ======================================================
mapred.job.tracker.handler.count         Nr of threads for job tracker to handle task trackers
io.file.buffer.size                      Read/write buffer size
io.sort.factor                           Number of streams to merge concurrently when sorting files during shuffling
io.sort.mb                               Amount of memory to use while sorting data
mapred.reduce.parallel.copies            Number of concurrent connections a reducer should use when fetching its input from mappers
tasktracker.http.threads                 Number of threads each TaskTracker uses to provide intermediate map output to reducers
mapred.tasktracker.map.tasks.maximum     Number of map tasks to deploy on each machine
mapred.tasktracker.reduce.tasks.maximum  Number of reduce tasks to deploy on each machine
======================================== ======================================================


Working with Map Reduce
=======================

* Access the JobTracker with http://localhost:50030
* Access TaskTracker with http://localhost:50060

* Example mapper for word counting (data comes from STDIN and output goes to STDOUT)

.. code-block:: python

  #!/usr/bin/env python

  import sys

  for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
      # This will be the input for the reduce script
      print '%s\t%s' % (word, 1)

* Example reducer code

.. code-block:: bash

  #!/usr/bin/env python

  import sys

  words = {}

  for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
      words[word] = words.get(word, 0) + int(count)
    except ValueError:
      pass

  for (word, count) in words.items():
    print "%s\t%d" % (word, count)

* Execute it with the following command

.. code-block:: bash

  bin/hadoop dfs -mkdir /test
  bin/hadoop dfs -put some_file /test
  bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar -file /full/path/to/mapper.py -mapper /full/path/to/mapper.py -file /full/path/to/reducer.py -reducer /full/path/to/reducer.py -input /test/README.txt -output /myoutput

* Get the result

.. code-block:: bash

  bin/hadoop dfs -cat /myoutput/part-00000


Pydoop
======

* Requires boost-python and maybe boost-devel
* Maybe you need to adjust setup.py to install pydoop (search for ``get_java_library_dirs`` function and return hardcoded path to libjvm.so)
* Simple wordcount

.. code-block:: bash

  #!/usr/bin/python

  def mapper(key, value, writer):
    for word in value.split():
      writer.emit(word, "1")

  def reducer(key, value_list, writer):
    writer.emit(key, sum(map(int, value_list)))

* Run it with

.. code-block:: bash

  pydoop script test-pydoop.py /test/README.txt myout

* Accessing HDFS

.. code-block:: bash

  import pydoop.hdfs as hdfs
  for line in hdfs.open("/some/file"):
    print line


Jobs
====

* List jobs

.. code-block:: bash

  bin/hadoop job -list all

* Terminate a job

.. code-block:: bash

  bin/hadoop job -kill <id>

* Get status of a job

.. code-block:: bash

  bin/hadoop job -status <id>



Security
========

* This is not for user authentication but for authenticating services!
* You can only adapt user permission by setting ``security.client.protocol.acl``
* To enable service-level security set ``hadoop.security.authorization`` to ``true`` in ``conf/core-site.xml``

===================================== ======================================================
Config option                         Description
===================================== ======================================================
security.client.protocol.acl          You must have these permissions to do anything with the API
security.client.datanode.protocol.acl ACL for ClientDatanodeProtocol, the client-to-datanode protocol for block recovery.
security.datanode.protocol.acl        ACL for DatanodeProtocol, which is used by datanodes to communicate with the namenode.
security.inter.datanode.protocol.acl  ACL for InterDatanodeProtocol, the inter-datanode protocol for updating generation timestamp.
security.namenode.protocol.acl        ACL for NamenodeProtocol, the protocol used by the secondary namenode to communicate with the namenode.
security.inter.tracker.protocol.acl   ACL for InterTrackerProtocol, used by the tasktrackers to communicate with the jobtracker.
security.job.submission.protocol.acl  ACL for JobSubmissionProtocol, used by job clients to communciate with the jobtracker for job submission, querying job status etc.
security.task.umbilical.protocol.acl  ACL for TaskUmbilicalProtocol, used by the map and reduce tasks to communicate with the parent tasktracker.
security.refresh.policy.protocol.acl  ACL for RefreshAuthorizationPolicyProtocol, used by the dfsadmin and mradmin commands to refresh the security policy in-effect.
===================================== ======================================================

* Seems like you have to always add root to security.client.protocol.acl
* After altering the policy you have to refresh it for data and task nodes

.. code-block:: bash

  hadoop dfsadmin -refreshServiceAcl
  hadoop mradmin -refreshServiceAcl

* HDFS has POSIX-like permissions

.. code-block:: bash

  hadoop dfs -chown
  hadoop dfs -chmod
  hadoop dfs -chgrp

* Network encryption can be setup in Hadoop >= 2.0.2-alpha see http://blog.cloudera.com/blog/2013/03/how-to-set-up-a-hadoop-cluster-with-network-encryption/


Multi-User-Hadoop
=================

* Setup a hadoop group in ``conf/hdfs-site.xml``

.. code-block:: bash

  <property>
    <name>dfs.permissions.supergroup</name>
    <value>hadoop</value>
  </property>

* Set jobtracker staging directory in dfs to other than /

.. code-block:: bash

  <property>
    <name>mapreduce.jobtracker.staging.root.dir</name>
    <value>/user</value>
  </property>

* Change permissions in hdfs

.. code-block:: bash

  bin/hadoop chgrp -R hadoop /
  bin/hadoop chmod 777 /user

* Adjust tmp directory permission in real filesystem (do NOT change recursively datanodes will blame you for that!)

.. code-block:: bash

  chmod 777 /app/hadoop/tmp
  chmod 777 /app/hadoop/tmp/mapred

* Add your users to the hadoop group


Restart a single daemon on a slave node
=======================================

* Connect to the slave node
* Get hadoop user

.. code-block:: bash

  bin/hadoop-daemon.sh start tasktracker


Addons
======

* `Hive <http://hive.apache.org>` - A SQL-like language to produce map-reduce jobs
* `Pig <http://pig.apache.org>` - high-level mapreduce language
* `oozie <http://oozie.apache.org>` - job scheduling
* `flume <http://flume.apache.org>` - log and data aggregation
* `whirr <http://whirr.apache.org>` - automated cloud clusters on ec2, rackspace etc
* `sqoop <http://sqoop.apache.org>` - relational data import
* `hbase <http://hbase.apache.org>` - realtime processing (based on google bigtable)
* `accumulo <http://accumulo.apache.org>` - NSA fork of HBase
* `mahout <http://mahout.apache.org>` - machine learning libraries


Documentation
=============

* http://developer.yahoo.com/hadoop/tutorial/
* https://www.youtube.com/watch?v=XtLXPLb6EXs
* http://hadoop.apache.org/docs/stable/commands_manual.pdf


Troubleshooting
===============

* Cannot create directory Name node is in safe mode -> NameNode is in safemode until configured percent of blocks reported to be online by the data nodes.
* DFS not leaving safe mode?

.. code-block:: bash

  bin/hadoop dfsadmin -safemode leave

* Start name and data node in foreground

.. code-block:: bash

  bin/hadoop namenode
  bin/hadoop datanode
