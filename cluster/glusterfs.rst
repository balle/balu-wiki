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
