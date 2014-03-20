####
Ceph
####

Overview
========

* http://www.youtube.com/watch?v=OyH1C0C4HzM
* A monitor knows the status of the network and keeps it in its monitor map
* You can have multiple monitors but should have a small, odd number
* MDS are the metadata servers (stores hirarchy of ceph fs + owner, timestamps, permissions etc)
* MDS is only needed for ceph fs
* An OSD is a storage node that contains and servers the real data, replicates and rebalances it
* The OSDs form a p2p network, recognize if one node is out and automatically restore the lost data to other nodes
* The client computes the localization of storage by using the CRUSH algorythm (no need to ask a central server)
* RADOS is the object storage interface
* RBD (RADOS Block Device) creates a block device as RADOS object
* Placement groups (pgs) combine objects into group. Replication is done on pgs or pools not files or dirs. You should have 100 pgs / OSD
* Pool is a seperate storage container that contains its own placement groups and objects (think of mountpoint)


Manual installation
===================

* Setup a monitor

.. code-block:: bash

 uuidgen

* Edit ``/etc/ceph/ceph.conf``

.. code-block:: bash

  fsid = <uuid>
  mon initial members = <short_hostname>
  mon host = <ip_address>
  auth cluster required = cephx
  auth service required = cephx
  auth client required = cephx
  osd pool default size = 2

* Generate keys for the monitor and admin user and add the monitor to the monitor map

.. code-block:: bash

  ceph-authtool --create-keyring /tmp/ceph.mon.keyring --gen-key -n mon. --cap mon 'allow *'
  ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --set-uid=0 --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow'
  ceph-authtool /tmp/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring
  monmaptool --create --add <short_hostname> <ip_address> --fsid <uuid> /tmp/monmap

* Create the monitor cache filesystem, start the monitor and see if it created the default pools and is running

.. code-block:: bash

  mkdir -p /var/lib/ceph/mon/ceph-<short_hostname>
  ceph-mon --mkfs -i <short_hostname> --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring
  ceph-mon -i <short_hostname>
  ceph osd lspools
  ceph -s

* Setup an OSD (note the command ceph osd create returns the osd id to use!)

.. code-block:: bash

  uuidgen
  ceph osd create <uuid>
  mkdir -p /var/lib/ceph/osd/ceph-<osd_id>
  fdisk /dev/sda
  ceph-disk prepare /dev/sda1
  mount /dev/sda /var/lib/ceph/osd/ceph-<osd_id>/
  ceph-osd -i <osd_id> --mkfs --mkkey
  ceph auth add osd.<osd_id> osd 'allow *' mon 'allow rwx' -i /var/lib/ceph/osd/ceph-<osd_id>/keyring
  ceph-disk activate /dev/sda1 --activate-key /var/lib/ceph/osd/ceph-<osd_id>/keyring
  ceph-osd -i <osd_id>
  ceph status

* Add another OSD for replication
* Setup a metadata server (only needed when using CephFS)

.. code-block:: bash

  mkdir -p /var/lib/ceph/mds/mds.<mds_id>
  ceph auth get-or-create mds.<mds_id> mds 'allow ' osd 'allow *' mon 'allow rwx' > /var/lib/ceph/mds/mds.<mds_id>/mds.<mds_id>.keyring
  ceph-mds -i <mds_id>
  ceph status


Adding OSDs the easy way
========================

* With ceph-deploy

.. code-block:: bash

  ceph-deploy osd prepare node1:/path
  ceph-deploy osd activate node1:/path

* Manually (ssh to new osd node)

.. code-block:: bash

  ceph-disk prepare --cluster ceph --cluster-uuid <fsid> --fs-type xfs /dev/sda
  ceph-disk-prepare --fs-type xfs /dev/sda


Complete setup of new node
==========================

* On new node

.. code-block:: bash

  useradd -d /home/ceph -m ceph
  passwd ceph
  echo "ceph ALL = (root) NOPASSWD:ALL" | tee /etc/sudoers.d/ceph
  mkdir /local/osd<id>

* On ceph-deploy node

.. code-block:: bash

  su - ceph
  ssh-copyid ceph@<hostname_of_new_node>
  ceph-deploy install <hostname_of_new_node>
  ceph-deploy osd prepare <hostname_of_new_node>:/local/osd<id>
  ceph-deploy osd activate <hostname_of_new_node>:/local/osd<id>
  ceph-deploy mon create <hostname_of_new_node>


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
  ceph osd tree
  ceph osd dump


Check server status
===================

.. code-block:: bash

  /etc/init.d/ceph status


Pools
=============

* Create

.. code-block:: bash

  ceph osd lspools
  ceph osd pool create <pool_name> <num_pgs>

* Change number of pgs

.. code-block:: bash

  ceph osd pool get <name> pg_num
  ceph osd pool set <name> pg_num <nr>

* Create a snapshot

.. code-block:: bash

  ceph osd pool mksnap <name>

* Change nr of replicas per pool

.. code-block:: bash

  ceph osd pool set <name> size 3


Placement groups
================

* Overview

.. code-block:: bash

  ceph pg dump

* What does the status XXX mean?

.. code-block:: bash

  inactive - The placement group has not been active for too long (i.e., it hasn’t been able to service read/write requests).
  unclean - The placement group has not been clean for too long (i.e., it hasn’t been able to completely recover from a previous failure).
  stale - The placement group status has not been updated by a ceph-osd, indicating that all nodes storing this placement group may be down.

* Why is a pg in such a state?

.. code-block:: bash

  ceph pg <pg_num> query

* Where to find an object?

.. code-block:: bash

  ceph osd map <pg_name> <object-name>


Editing the CRUSH map
=====================

* The CRUSH map defines ``buckets`` (think storage groups) to map placement groups tp OSDs across a failure domain (e.g. copy 1 is in rack 1 and copy 2 in rack 2 to avoid power outage of one rack to destroy all copies)
* A higher weight will get more load than a lower weight

.. code-block:: bash

  ceph osd getcrushmap -o crushmap
  crushtool -d crushmap -o mymap
  emacs mymap
  crushtool -c mymap -o newmap
  ceph osd setcrushmap -i newmap


Maintanance
===========

* To stop CRUSH from automatically balance load of the cluster

.. code-block:: bash

  ceph osd set noout


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
