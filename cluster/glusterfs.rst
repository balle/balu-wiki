###########
GlusterFS
###########

Network ports
=============

* These are the tcp ports to open in your firewall

===== ===================
Port  Description
===== ===================
616   GlusterFS
38465 GlusterFS
38466 GlusterFS
38468 GlusterFS
38469 GlusterFS
24007 GlusterFSd
49153 Bricks
===== ===================


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

  service glusterd start


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

  gluster volume remove-brick test node1:/export/test node2:/export/test
  gluster volume stop test
  gluster volume remove test

* Add a new disk to a volume

.. code-block:: bash

  gluster volume add-brick <volname> replica 2 node3:/export/moretest

* Manage access by ip

.. code-block:: bash

  gluster volume set testvol auth.allow 192.168.1.1
  # or
  gluster volume set testvol auth.allow all
  gluster volume set testvol auth.reject 192.168.10.*

* How many space to reserve for logs / meta data?

.. code-block:: bash

  gluster volume set cluster.min-free-disk 5%

* Enable self healing (on by default)

.. code-block:: bash

  gluster volume set cluster.self-heal-daemon on


NFS export
==========

* Start rpcbind
* Start nfslock (rpcstatd)
* Start glusterd
* Adjust firewall

===== ===================
Port  Description
===== ===================
2049  GlusterFS (NFS)
111   RPCbind
54539 RCP statd
38003 RPCbind
===== ===================

* Now you can mount it with

.. code-block:: bash

  mount -t nfs -o mountproto=tcp,vers=3 ip1:/testme /mnt


Quota
=====

.. code-block:: bash

  gluster volume quota <volname> enable
  gluster volume quota <volname> limit-usage <directory> 10GB
  gluster volume quota <volname> list
  gluster volume quota <volname> remove <directory>


Performance tuning
==================

* Performance information

.. code-block:: bash

  gluster volume top <volname> read-perf
  gluster volume top <volname> write-perf

* Profiling

.. code-block:: bash

  gluster volume profile <volname> start
  gluster volume profile <volname> info
  gluster volume profile <volname> stop

* Setting read cache size (default 32MB)

.. code-block:: bash

  gluster volume set <volname> performance.cache-size 256MB

* Stripe block size

.. code-block:: bash

  gluster volume set cluster.stripe-block-size 128KB

* I/O threads

.. code-block:: bash

  gluster volume set performance.io-thread-count 32


Troubleshooting
===============

* `requested NFS version or transport protocol is not supported` -> you try to mount with UDP or you didnt start rpcbind, nfslock, glusterd in the right order

* `Protocol not supported` -> you try to mount with version 4 instead of 3

* `node is already part of another cluster` -> delete /var/lib/glusterd/peers/*

* `split brain` means that we detected changes to both replicas

.. code-block:: bash

  gluster volume heal <volname> full
  gluster volume heal <volname> info


* `{path} or a prefix of it is already part of a volume ` -> you forgot to remove the brick before deleting the volume

.. code-block:: bash

  setfattr -x trusted.glusterfs.volume-id $brick_path
  setfattr -x trusted.gfid $brick_path
  rm -rf $brick_path/.glusterfs
  service glusterd restart
