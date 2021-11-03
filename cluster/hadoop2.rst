#########
Hadoop 2
#########

Overview
========

===== ===================
Port  Description
===== ===================
50070 hadoop namenode web
54310 hadoop namenode
50010 hadoop datanode
50020 hadoop datanode
50075 hadoop datanode
8030  hadoop resourcemanager
8031  hadoop resourcemanager
8032  hadoop resourcemanager
8033  hadoop resourcemanager
8088  hadoop resourcemanager web
13562 hadoop nodemanager
8040  hadoop nodemanager
34568 hadoop nodemanager
8042  hadoop nodemanager
19888 hadoop job history web
10020 hadoop job history
10033 hadoop job history
===== ===================


Installation
============

* Edit ``etc/hadoop/core-site.xml`` to configure tmp dir and location of name node

.. code-block:: bash

  <property>
    <name>hadoop.tmp.dir</name>
    <value>/local/hadoop/tmp</value>
    <description>A base for other temporary directories.</description>
  </property>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://127.0.0.1:54310</value>
  </property>
  <property>
    <name>hadoop.security.authorization</name>
    <value>true</value>
  </property>
  <property>
    <name>hadoop.http.staticuser.user</name>
    <value>hdfs</value>
  </property>


* Edit ``etc/hadoop/mapred-site.xml`` to set the locations of the job tracker and its working dir

.. code-block:: bash

  <property>
    <name>mapred.job.tracker</name>
    <value>127.0.0.1:54311</value>
  </property>
  <property>
    <name>mapreduce.jobtracker.staging.root.dir</name>
    <value>/user</value>
  </property>
  <property>
    <name>mapred.tasktracker.map.tasks.maximum</name>
    <value>16</value>
  </property>
  <property>
    <name>mapred.tasktracker.reduce.tasks.maximum</name>
    <value>16</value>
  </property>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>

  <!--
       DEFAULT VALUES LIKELY TO GET ADJUSTED BELOW HERE
  -->
  <property>
    <name>mapreduce.jobtracker.expire.trackers.interval</name>
    <value>600000</value>
    <description>Expert: The time-interval, in miliseconds, after which
    a tasktracker is declared 'lost' if it doesn't send heartbeats.
    </description>
  </property>

  <property>
    <name>mapreduce.jobtracker.restart.recover</name>
    <value>false</value>
    <description>"true" to enable (job) recovery upon restart,
               "false" to start afresh
    </description>
  </property>

  <property>
    <name>mapreduce.task.io.sort.factor</name>
    <value>10</value>
    <description>The number of streams to merge at once while sorting
    files.  This determines the number of open file handles.</description>
  </property>

  <property>
    <name>mapreduce.task.io.sort.mb</name>
    <value>100</value>
    <description>The total amount of buffer memory to use while sorting
    files, in megabytes.  By default, gives each merge stream 1MB, which
    should minimize seeks.</description>
  </property>

  <property>
    <name>mapreduce.tasktracker.http.threads</name>
    <value>40</value>
    <description>The number of worker threads that for the http server. This is
               used for map output fetching
    </description>
  </property>

  <property>
    <name>mapreduce.task.timeout</name>
    <value>600000</value>
    <description>The number of milliseconds before a task will be
    terminated if it neither reads an input, writes an output, nor
    updates its status string.  A value of 0 disables the timeout.
    </description>
  </property>

  <property>
   <name>mapreduce.task.tmp.dir</name>
   <value>./tmp</value>
   <description> To set the value of tmp directory for map and reduce tasks.
   If the value is an absolute path, it is directly assigned. Otherwise, it is
   prepended with task's working directory. The java tasks are executed with
    option -Djava.io.tmpdir='the absolute path of the tmp dir'. Pipes and
    streaming are set with environment variable,
    TMPDIR='the absolute path of the tmp dir'
    </description>
  </property>

  <property>
    <name>mapreduce.output.fileoutputformat.compress</name>
    <value>false</value>
    <description>Should the job outputs be compressed?
    </description>
  </property>

  <property>
    <name>mapreduce.shuffle.ssl.enabled</name>
    <value>false</value>
    <description>
    Whether to use SSL for for the Shuffle HTTP endpoints.
    </description>
  </property>


* Edit ``etc/hadoop/hdfs-site.xml`` to set working dirs of name and data node and how often a file gets replicated

.. code-block:: bash

  <property>
    <name>dfs.replication</name>
    <value>3</value>
  </property>
  <property>
    <name>dfs.data.dir</name>
    <value>/data/hadoop/data-node</value>
  </property>
  <property>
    <name>dfs.name.dir</name>
    <value>/data/hadoop/name-node</value>
  </property>
  <property>
    <name>dfs.permissions.supergroup</name>
    <value>hadoop</value>
  </property>

    <property>
      <name>dfs.namenode.accesstime.precision</name>
      <value>3600000</value>
      <description>The access time for HDFS file is precise upto this value.
    The default value is 1 hour. Setting a value of 0 disables
    access times for HDFS.
      </description>
    </property>

 <!--
       DEFAULT VALUES LIKELY TO GET ADJUSTED BELOW HERE
  -->
  <property>
    <name>dfs.permissions.enabled</name>
    <value>true</value>
    <description>
    If "true", enable permission checking in HDFS.
    If "false", permission checking is turned off,
    but all other behavior is unchanged.
    Switching from one parameter value to the other does not change the mode,
    owner or group of files or directories.
    </description>
  </property>

  <property>
    <name>dfs.namenode.fs-limits.min-block-size</name>
    <value>1048576</value>
    <description>Minimum block size in bytes, enforced by the Namenode at create
      time. This prevents the accidental creation of files with tiny block
      sizes (and thus many blocks), which can degrade
      performance.</description>
  </property>

  <property>
    <name>dfs.blocksize</name>
    <value>134217728</value>
    <description>
      The default block size for new files, in bytes.
      You can use the following suffix (case insensitive):
      k(kilo), m(mega), g(giga), t(tera), p(peta), e(exa) to specify the size (such as 128k, 512m, 1g, etc.),
      Or provide complete size in bytes (such as 134217728 for 128 MB).
    </description>
  </property>

  <property>
    <name>dfs.namenode.fs-limits.max-blocks-per-file</name>
    <value>1048576</value>
    <description>Maximum number of blocks per file, enforced by the Namenode on
        write. This prevents the creation of extremely large files which can
        degrade performance.</description>
  </property>

  <property>
    <name>dfs.heartbeat.interval</name>
    <value>3</value>
    <description>Determines datanode heartbeat interval in seconds.</description>
  </property>

  <property>
    <name>dfs.namenode.handler.count</name>
    <value>10</value>
    <description>The number of server threads for the namenode.</description>
  </property>

  <property>
    <name>dfs.namenode.name.dir.restore</name>
    <value>false</value>
    <description>Set to true to enable NameNode to attempt recovering a
      previously failed dfs.namenode.name.dir. When enabled, a recovery of any
      failed directory is attempted during checkpoint.</description>
  </property>

  <property>
    <name>dfs.image.compress</name>
    <value>false</value>
    <description>Should the dfs image be compressed?
    </description>
  </property>

  <property>
    <name>dfs.image.transfer.bandwidthPerSec</name>
    <value>0</value>
    <description>
        Maximum bandwidth used for image transfer in bytes per second.
        This can help keep normal namenode operations responsive during
        checkpointing. The maximum bandwidth and timeout in
        dfs.image.transfer.timeout should be set such that normal image
        transfers can complete successfully.
        A default value of 0 indicates that throttling is disabled.
    </description>
  </property>

  <property>
    <name>dfs.datanode.max.transfer.threads</name>
    <value>4096</value>
    <description>
        Specifies the maximum number of threads to use for transferring data
        in and out of the DN.
    </description>
  </property>

  <property>
    <name>dfs.ha.automatic-failover.enabled</name>
    <value>false</value>
    <description>
    Whether automatic failover is enabled. See the HDFS High
    Availability documentation for details on automatic HA
    configuration.
    </description>
  </property>

  <property>
    <name>dfs.webhdfs.enabled</name>
    <value>false</value>
    <description>
    Enable WebHDFS (REST API) in Namenodes and Datanodes.
    </description>
  </property>

  <property>
    <name>dfs.https.enable</name>
    <value>false</value>
    <description>Decide if HTTPS(SSL) is supported on HDFS
    </description>
  </property>

* Edit ``etc/hadoop/yarn-site.xml``

.. code-block:: bash

  <property>
    <name>yarn.resourcemanager.resource-tracker.address</name>
    <value>[% HADOOP_MASTER %]:8031</value>
    <description>host is the hostname of the resource manager and
    port is the port on which the NodeManagers contact the Resource Manager.
    </description>
  </property>

  <property>
    <name>yarn.resourcemanager.scheduler.address</name>
    <value>127.0.0.1:8030</value>
    <description>host is the hostname of the resourcemanager and port is the port
    on which the Applications in the cluster talk to the Resource Manager.
    </description>
  </property>

  <property>
    <name>yarn.resourcemanager.scheduler.class</name>
    <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler</value>
    <description>In case you do not want to use the default scheduler</description>
  </property>

  <property>
    <name>yarn.nodemanager.local-dirs</name>
    <value>/data/hadoop/nm</value>
    <description>the local directories used by the nodemanager</description>
  </property>

  <property>
    <name>yarn.nodemanager.address</name>
    <value>127.0.0.1:8040</value>
    <description>the nodemanagers bind to this port</description>
  </property>

  <property>
    <name>yarn.nodemanager.resource.memory-mb</name>
    <value>10240</value>
    <description>the amount of memory on the NodeManager in GB</description>
  </property>

  <property>
    <name>yarn.nodemanager.remote-app-log-dir</name>
    <value>/app-logs</value>
    <description>directory on hdfs where the application logs are moved to </description>
  </property>

   <property>
    <name>yarn.nodemanager.log-dirs</name>
    <value></value>
    <description>the directories used by Nodemanagers as log directories</description>
  </property>

  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
    <description>shuffle service that needs to be set for Map Reduce to run </description>
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

  su - hadoop -c '/opt/hadoop/bin/hdfs namenode -format -force'

* Start the services

.. code-block:: bash

  su - hadoop -c '/opt/hadoop/sbin/hadoop-daemon.sh start namenode && /opt/hadoop/sbin/hadoop-daemon.sh start datanode' && /opt/hadoop/sbin/yarn-daemon.sh start resourcemanager && /opt/hadoop/sbin/yarn-daemon.sh start nodemanager'"


Check status
============

* HDFS

.. code-block:: bash

  /opt/hadoop/bin/hdfs dfsadmin -report

* YARN

.. code-block:: bash

  /opt/hadoop/bin/yarn node -list

* Test Namenode

.. code-block:: bash

  su - hadoop -c '/opt/hadoop/bin/hadoop fs -mkdir /user'
  su - hadoop -c '/opt/hadoop/bin/hadoop fs -mkdir /user/hadoop'

* Test Datanode

.. code-block:: bash

  su - hadoop -c '/opt/hadoop/bin/hadoop fs -put /opt/hadoop/etc/hadoop/hadoop-env.sh /user/hadoop/hadoop-env'

* Test YARN

.. code-block:: bash

  su - hadoop -c "/opt/hadoop/bin/hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 2 10"


Configure High Availability
===========================

* Edit core-site.xml

.. code-block:: bash

  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://mycluster</value>
  </property>
  <property>
    <name>ha.zookeeper.quorum</name>
    <value>zookeeper1:2181,zookeeper2:2181,zookeeper3:2181</value>
  </property>

* Edit hdfs-site.xml

.. code-block:: bash

  <!-- only for single node setup
  <property>
    <name>dfs.name.dir</name>
    <value>file:///local/hadoop/name-node</value>
    </property>
  -->

  <!-- HA settings -->
  <property>
    <name>dfs.nameservices</name>
    <value>mycluster</value>
  </property>

  <property>
    <name>dfs.ha.namenodes.mycluster</name>
    <value>nn1,nn2</value>
  </property>

  <property>
    <name>dfs.namenode.rpc-address.mycluster.nn1</name>
    <value>hadoop_master:8020</value>
  </property>
  <property>
    <name>dfs.namenode.rpc-address.mycluster.nn2</name>
    <value>hadoop_master2:8020</value>
  </property>

  <property>
    <name>dfs.namenode.http-address.mycluster.nn1</name>
    <value>hadoop_master:50070</value>
  </property>
  <property>
    <name>dfs.namenode.http-address.mycluster.nn2</name>
    <value>hadoop_master2:50070</value>
  </property>

  <property>
    <name>dfs.namenode.shared.edits.dir</name>
    <value>qjournal://hadoop_master:8485;hadoop_master2:8485/mycluster</value>
  </property>

  <property>
    <name>dfs.client.failover.proxy.provider.mycluster</name>
    <value>org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider</value>
  </property>

  <property>
    <name>dfs.ha.fencing.methods</name>
    <value>sshfence</value>
  </property>

  <property>
    <name>dfs.ha.fencing.ssh.private-key-files</name>
    <value>/opt/hadoop/.ssh/id_rsa</value>
  </property>

  <property>
    <name>dfs.ha.automatic-failover.enabled</name>
    <value>true</value>
    <description>
    Whether automatic failover is enabled. See the HDFS High
    Availability documentation for details on automatic HA
    configuration.
    </description>
  </property>

  <property>
    <name>ha.zookeeper.quorum</name>
    <value>zookeeper1:2181,zookeeper2:2181,zookeeper3:2181</value>
  </property>


* Edit yarn-site.xml

.. code-block:: bash

  <property>
    <name>yarn.resourcemanager.ha.enabled</name>
    <value>true</value>
  </property>
  <property>
    <name>yarn.resourcemanager.cluster-id</name>
    <value>mycluster</value>
  </property>
  <property>
    <name>yarn.resourcemanager.ha.rm-ids</name>
    <value>rm1,rm2</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname.rm1</name>
    <value>hadoop_master</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname.rm2</name>
    <value>hadoop_master2</value>
  </property>
  <property>
    <name>yarn.resourcemanager.webapp.address.rm1</name>
    <value>hadoop_master:8088</value>
  </property>
  <property>
    <name>yarn.resourcemanager.webapp.address.rm2</name>
    <value>hadoop_master2:8088</value>
  </property>
  <property>
    <name>yarn.resourcemanager.zk-address</name>
    <value>zookeeper1:2181,zookeeper2:2181,zookeeper3:2181</value>
  </property>

* Start Zookeeper Fencing Service additionally to normal Zookeeper

.. code-block:: bash

  /opt/hadoop/sbin/hadoop-daemon.sh --script /opt/hadoop/bin/hdfs start zkfc

* Start HDFS Journalnode on Namenode servers

.. code-block:: bash

  /opt/hadoop/sbin/hadoop-daemon.sh start journalnode

* Initialize and format Namenode

.. code-block:: bash

  /opt/hadoop/bin/hdfs zkfc -formatZK
  /opt/hadoop/bin/hdfs namenode -format -force
  /opt/hadoop/sbin/hadoop-daemon.sh start namenode

* Check the status

.. code-block:: bash

  bin/hdfs haadmin -getServiceState nn1
  bin/hdfs haadmin -getServiceState nn2
  bin/yarn rmadmin -getServiceState rm1
  bin/yarn rmadmin -getServiceState rm2


Convert single namenode to HA
=============================

.. code-block:: bash

  /opt/hadoop/bin/hdfs namenode -bootstrapStandby
  /opt/hadoop/bin/hdfs namenode -initializeSharedEdits


Configure Capacity Scheduler
============================

* The CapacityScheduler is designed to allow sharing a large cluster while giving each organization a minimum capacity guarantee.
* Make sure ``org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler`` is set as ``yarn.resourcemanager.scheduler.class`` in ``etc/hadoop/yarn-site.xml``
* Configure resources for unix groups a, b and default
* Edit ``etc/hadoop/capacity-scheduler.xml``

.. code-block:: bash

  <property>
    <name>yarn.scheduler.capacity.root.queues</name>
    <value>a,b,default</value>
    <description>The queues at the this level (root is the root queue).
    </description>
  </property>

  <!-- GROUP A -->
  <property>
    <name>yarn.scheduler.capacity.root.a.capacity</name>
    <value>30</value>
    <description>Default queue target capacity.</description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.a.user-limit-factor</name>
    <value>1</value>
    <description>
      Default queue user limit a percentage from 0.0 to 1.0.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.a.maximum-capacity</name>
    <value>100</value>
    <description>
      The maximum capacity of the default queue.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.a.state</name>
    <value>RUNNING</value>
    <description>
      The state of the default queue. State can be one of RUNNING or STOPPED.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.a.acl_submit_applications</name>
    <value>group_a</value>
    <description>
      The ACL of who can submit jobs to the default queue.
    </description>
  </property>


  <!-- GROUP B -->
  <property>
    <name>yarn.scheduler.capacity.root.b.capacity</name>
    <value>30</value>
    <description>Default queue target capacity.</description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.b.user-limit-factor</name>
    <value>1</value>
    <description>
      Default queue user limit a percentage from 0.0 to 1.0.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.b.maximum-capacity</name>
    <value>100</value>
    <description>
      The maximum capacity of the default queue.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.b.state</name>
    <value>RUNNING</value>
    <description>
      The state of the default queue. State can be one of RUNNING or STOPPED.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.b.acl_submit_applications</name>
    <value>group_b</value>
    <description>
      The ACL of who can submit jobs to the default queue.
    </description>
  </property>


  <!-- GROUP DEFAULT -->
  <property>
    <name>yarn.scheduler.capacity.root.default.capacity</name>
    <value>40</value>
    <description>Default queue target capacity.</description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.default.user-limit-factor</name>
    <value>1</value>
    <description>
      Default queue user limit a percentage from 0.0 to 1.0.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.default.maximum-capacity</name>
    <value>100</value>
    <description>
      The maximum capacity of the default queue.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.default.state</name>
    <value>RUNNING</value>
    <description>
      The state of the default queue. State can be one of RUNNING or STOPPED.
    </description>
  </property>

  <property>
    <name>yarn.scheduler.capacity.root.default.acl_submit_applications</name>
    <value>*</value>
    <description>
      The ACL of who can submit jobs to the default queue.
    </description>
  </property>

* Refresh queues

.. code-block:: bash

  bin/yarn rmadmin -refreshQueues
  bin/hadoop queue -list

* Submit a test job

.. code-block:: bash

  bin/hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi -Dmapred.job.queue.name=a 2 10


Configure Fair Scheduler
========================

* All jobs get, on average, an equal share of resources over time
* Make sure ``org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler`` is set as ``yarn.resourcemanager.scheduler.class`` in ``etc/hadoop/yarn-site.xml``
* A pool has the same name as the user
* Create file ``etc/hadoop/fair-scheduler.xml``

.. code:: xml

  <?xml version="1.0"?>

  <allocations>
    <pool name="hadoop">
      <minMaps>5</minMaps>
      <maxMaps>90</maxMaps>
      <maxReduces>20</maxReduces>
      <weight>2.0</weight>
    </pool>
    <user name="hadoop">
      <maxRunningJobs>3</maxRunningJobs>
    </user>
    <userMaxJobsDefault>2</userMaxJobsDefault>
  </allocations>

* Restart resource manager


HDFS NFS Gateway
================

* Edit ``hdfs-site.xml``

.. code-block:: bash

    <property>
      <name>dfs.nfs3.dump.dir</name>
      <value>/data/hadoop/.hdfs-nfs</value>
    </property>

    <property>
      <name>dfs.nfs.exports.allowed.hosts</name>
      <value>* rw</value>
    </property>

* Edit ``core-site.xml``

.. code-block:: bash

  <property>
    <name>hadoop.proxyuser.nfsserver.groups</name>
    <value>*</value>
    <description>
           The 'nfsserver' user is allowed to proxy all members of the 'nfs-users1' and
           'nfs-users2' groups. Set this to '*' to allow nfsserver user to proxy any group.
    </description>
  </property>

  <property>
    <name>hadoop.proxyuser.nfsserver.hosts</name>
    <value>*</value>
    <description>
           This is the host where the nfs gateway is running. Set this to '*' to allow
           requests from any hosts to be proxied.
    </description>
  </property>

* Start the daemons

.. code-block:: bash

  systemctl stop rpcbind
  sbin/hadoop-daemon.sh start portmap
  su - nfsserver -c "sbin/hadoop-daemon.sh start nfs3"

* Test nfs mount

.. code-block:: bash

  rpcinfo -p localhost
  showmount -e
  mount -t nfs -o vers=3,proto=tcp,nolock localhost:/ /mnt


Troubleshooting
===============

* ``java.lang.IllegalArgumentException: Illegal capacity of -1.0 for queue`` -> You dont have defined a capacity for the queue like yarn.scheduler.capacity.root.$QUEUENAME.capacity
* ``org.apache.hadoop.util.Shell$ExitCodeException: chmod: cannot access `/user/myuser1544460269/.staging/job_local1544460269_0001': No such file or directory`` -> set mapreduce.framework.name to yarn in mapred-site.xml
* datanode says ``Initialization failed for Block pool`` -> Namenode got formated / changed afterwards, delete the contents of dfs.data.dir
