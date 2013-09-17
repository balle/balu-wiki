###########
GlusterFS
###########

Installation
============

* Install GlusterFS repository

.. code-block:: bash

  wget http://download.gluster.org/pub/gluster/glusterfs/LATEST/CentOS/glusterfs-epel.repo

* Install packages

.. code-block:: bash

  yum install glusterfs{,-server,-fuse,-geo,-replication}

* Start the service

.. code-block:: bash

  service start glusterd


Configuration
=============

* Make a server trust another Gluster node

.. code-block:: bash

  gluster peer probe <ip>

* Lets asume you have a partition mounted to /export/test to distribute with GlusterFS on node1 and node2
* Setup a volume

.. code-block:: bash

  gluster volume create test replica 2 node1:/export/test node2:/export/test
  gluster volume start test

* Now you can mount and use the volume

.. code-block:: bash

  mount -t glusterfs node1:/export/test /mnt


Peers
=====

* Add a new one

.. code-block:: bash

  gluster peer probe <ip>

* Show status

.. code-block:: bash

  gluster peer status

* Remove one

.. code-block:: bash

  gluster peer detach <ip>


Volumes
=======

* Create a new one

.. code-block:: bash

  gluster volume create test replica 2 node1:/export/test node2:/export/test
  gluster volume start test

* List all volumes

.. code-block:: bash

  gluster volume status

* Remove one

.. code-block:: bash

  gluster volume stop test
  gluster volume remove test

* Add a new disk to a volume

.. code-block:: bash

  gluster volume add-brick <volname> replica 2 node3:/export/moretest


Troubleshooting
===============

* Performance information

.. code-block:: bash

  gluster volume top <volname> read-perf
  gluster volume top <volname> write-perf
