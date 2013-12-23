#######
Cgroups
#######

Overview
========

* Cgroups group processes so that you can define ressource limits and get stats for it
* Processes are called tasks
* Every process can only be in one cgroup
* A cgroup can inherit the properties of another cgroup

.. code-block:: bash

  mkdir /cgroup/
  mount -t cgroup -o memory nodev /cgroup/


Installation
============

.. code-block:: bash

  yum install libcgroup


Create a new cgroup
===================

* Temporarily

.. code-block:: bash

  mkdir /cgroup/<groupname>

* Or

.. code-block:: bash

  cgcreate -a <user> -g memory,cpu:<groupname>


* Permanent by editing ``/etc/cgconfig.conf``

.. code-block:: bash

  group <name> {
    [<permissions>]
    <controller> {
        <param name> = <param value>;
     }
  }

* e.g.

.. code-block:: bash

  mount {
        cpuset  = /cgroup/cpuset;
        cpu     = /cgroup/cpu;
        cpuacct = /cgroup/cpuacct;
        memory  = /cgroup/memory;
        devices = /cgroup/devices;
        freezer = /cgroup/freezer;
        net_cls = /cgroup/net_cls;
        blkio   = /cgroup/blkio;
  }

  group students {
    blkio {
      blkio.throttle.read_bps_device = "1000";
      blkio.throttle.write_bps_device = "1000";
    }
  }

* Dont forget to restart the cgconfig service in order to load the changes!

.. code-block:: bash

  service cgconfig restart


Map user and processes to a cgroup
==================================

* Edit ``/etc/cgrules.conf``

.. code-block:: bash

   <user> <subsystems> <cgroup>
   <user>:<command> <subsystems> <cgroup>

* names with a prepending @ are groups



Manually starting a process in a cgroup
=======================================

.. code-block:: bash

  cgexec -g <subsystems>:<cgroup> <command> <arguments>


Define limits
=============

* For memory

.. code-block:: bash

  memory.limit_in_bytes = 1000000

* Cpu time (default 1024 is 100% so 100 is ~10%)

.. code-block:: bash

  cpu.shares = 100

* CPU pinning

.. code-block:: bash

  cpuset.cpus = 0-5,14,15

* Storage time (100% is value of 1024)

.. code-block:: bash

  blkio.weight = 512
