#######
Ambari
#######

Overview
========

* Ambari (ambari.apache.org) is used to setup Hadoop / Spark etc environment


Upgrading Ambari
=================

* This will only affect Ambari (all Hadoop / Spark components keep running in old version)
* Read the release notes!
* Get the newest Repo from ambari.apache.org

.. code-block:: bash

  wget -nv http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.2.0.0/ambari.repo -O /etc/yum.repos.d/ambari.repo
  
* Make sure you have a backup of the postgres db on the management node

.. code-block:: bash

  su - postgres
  pg_dumpall > ambari.sql
  
* Stop Ambari on management node

.. code-block:: bash

  ambari-server stop
  
* Stop Ambari on all compute nodes

.. code-block:: bash

  ambari-agent stop
  
* Upgrade Ambari on management node

.. code-block:: bash

  yum upgrade ambari-server
  
* And on all compute nodes

.. code-block:: bash

  yum upgrade ambari-agent

* Afterwards run this on management node

.. code-block:: bash

  ambari-server upgrade
  ambari-server start

* And start Ambari on all compute nodes

.. code-block:: bash

  ambari-agent start


Upgrading HDP (Hadoop Stack)
============================

* Run the following commands on the master node
* Set HDFS into maintenance mode and flush namespace cache

.. code-block:: bash

  su - hdfs -c "hdfs dfsadmin -safemode enter"
  su - hdfs -c "hdfs dfsadmin -saveNamespace"
  
* Check HDFS for errors

.. code-block:: bash

  su - hdfs -c "hdfs fsck / -files -blocks -locations"
  
* In the Ambari Webinterface go to Admin -> Stack and Versions -> Versions -> Manage Versions
* Click on Register Version, tick for redhat 7 (or whatever OS it's running on)
* URLs for new HDP repos can be found here http://docs.hortonworks.com/HDPDocuments/Ambari-2.2.2.0/bk_Installing_HDP_AMB/content/_hdp_stack_repositories.html
* Click on "Install on and "Install Packages" afterwards
* After successful installation don't forget to leave maintenance mode for HDFS

.. code-block:: bash

  su - hdfs -c "hdfs dfsadmin -safemode leave"

Remove a service from ambari using the REST API
===============================================

.. code-block:: bash

  curl -u admin:"$PASSWORD" -H "X-Requested-By: ambari" http://127.0.0.1:8080/api/v1/clusters/<cluster_name>/hosts/<hostname>/host_components
  curl -u admin:"$PASSWORD" -H "X-Requested-By: ambari" -X DELETE http://127.0.0.1:8080/api/v1/clusters/<cluster_name>/hosts/<hostname>/host_components/<service_name>


Reinstall an ambari client
===========================

* Install ambari-agent, set server hostname to ambari master in /etc/ambari-agent/conf/ambari-agent.ini and start the agent

.. code-block:: bash

  ambari-agent start

* Now you can delete most of the services from the host in the ambari webinterface and afterwards install it again
* If you cannot delete a service use the REST API (see above)
