####
Ceph
####

Overview
========

* http://www.youtube.com/watch?v=OyH1C0C4HzM
* A monitor is the controller of net ceph cluster. It knows the status of the network.
* You can have multiple monitors but should have a small, odd number
* MDS are the metadata servers (stores hirarchy of ceph fs + owner, timestamps, permissions etc)
* MDS is only necessary for ceph fs
* An OSD is a storage node that contains and servers the real data, replicates and rebalances it
* The OSDs form a p2p network, recognize if one node is out and automatically restore the lost data to other nodes
* The client computes the localization of storage by using the CRUSH algorythm (no need to ask a central server)


Adding OSDs
===========

* Automatically

.. code-block:: bash

  ceph-deploy osd prepare node1:/path
  ceph-deploy osd activate node1:/path

* Manually (ssh to new osd node)

.. code-block:: bash

  ceph-disk-prepare --fs-type xfs /local/path


Configure replication
=====================

* Edit ceph.conf

.. code-block:: bash

  osd pool default size = 2


Access storage
==============

* CEPH FUSE (filesystem access comparable to NFS)

.. code-block:: bash

  ceph-fuse -m <monitor>:6789 /mountpoint

* FUSE via fstab

.. code-block:: bash

  id=admin                /mnt  fuse.ceph defaults 0 0

* CEPH FS kernel client

* RADOS API for object storage

.. code-block:: bash

  rados put test-object /path/to/some_file --pool=data
  rados -p data ls
  ceph osd map data test-object
  rados rm test-object --pool=data

* RADOS FUSE 

* Virtual Block device via kernel driver (needs kernel >= 3.4.20)

* iSCSI interface under development

* Code your own client with librados


Check size
==========

.. code-block:: bash

  ceph df


Check health
============

.. code-block:: bash

  ceph health detail

* get continuos information

.. code-block:: bash

  ceph -w


Check osd status
================

.. code-block:: bash

  ceph osd stat


Check server status
===================

.. code-block:: bash

  /etc/init.d/ceph status


Troubleshooting general
=======================

* Remove everything

.. code-block:: bash

  ceph-deploy purge host1 host2
  ceph-deploy purgedata host1 host2
  ceph-deploy gatherkeys


Troubleshooting sudo
====================

* Make sure that visiblepw is disabled

.. code-block:: bash

  Defaults   !visiblepw

* Is the /etc/sudoers.d directory really included?


Troubleshooting network
=======================

* The name of a osd / mon must be the official name of the host no aliases!
* Make sure you have a ``public network = 1.2.3.4/24`` in your ceph.conf


Repair monitor
==============

* the id can be found by looking into ``/var/lib/ceph/mon/``

* run monitor in debug mode

.. code-block:: bash

  ceph-mon -i <myid> -d

* Reformat monitor data store

.. code-block:: bash

  rm -rf /var/lib/ceph/mon/ceph-<myid>
  ceph-mon --mkfs -i <myid> --keyring /etc/ceph/ceph.client.admin.keyring
