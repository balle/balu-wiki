######
Slurm
######

Overview
========

.. image:: ../images/slurm-arch.gif

Setup munge authentication service on controller node
=====================================================

.. code-block:: bash

  apt install munge
  systemctl enable munge
  systemctl start munge


Setup Slurmdbd on controller node
==================================

* Install packages

.. code-block:: bash

  apt install slurmdbd mysql-server


* Edit /etc/mysql/conf.d/mysql

.. code-block:: bash

  innodb_buffer_size=128M

* Start mysql and create slurm user

.. code-block:: bash

  systemctl enable mysql
  systemctl start mysql
  echo "create database slurm" | mysql
  echo "create user slurm@localhost identified by '$STORAGE_PASS'" | mysql
  echo "GRANT ALL PRIVILEGES ON slurm.* TO 'slurm'@'localhost';" | mysql

* Create slurmdbd config

.. code-block:: bash

  zcat /usr/share/doc/slurmdbd/examples/slurmdbd.conf.simple.gz > /etc/slurm-llnl/slurmdbd.conf

* Set the StoragePass used to create db user
* Start slurmdbd

.. code-block:: bash

  systemctl enable slurmdbd
  systemctl start slurmdbd


Setup Slurmctld on controller node
==================================

* Install packages

.. code-block:: bash

  apt install slurm-client slurmctld

* Create example config

.. code-block:: bash

  zcat /usr/share/doc/slurm-client/examples/slurm.conf.simple.gz > /etc/slurm-llnl/slurm.conf

* Set ControlMachine to name of Slurm controller
* Configure cluster nodes

.. code-block:: bash

  #
  # COMPUTE NODES
  #
  NodeName=DEFAULT CPUs=2 RealMemory=2000 TmpDisk=64000 State=UNKNOWN
  NodeName=my-nodes-[1-42]

  #
  # Partition Configurations
  #
  PartitionName=mypart Nodes=my-nodes-[1-42] Default=YES MaxTime=INFINITE State=UP

* To get the number of CPUs, Cores, RealMemory etc for above configuraton

.. code-block:: bash

  slurmd -C

* Start slurmctld

.. code-block:: bash

  systemctl enable slurmctld
  systemctl start slurmctld

* To make slurmctld HA install it on another machine and set BackupController in /etc/slurm-llnl/slurm.conf
* Reload slurmd, slurmctld and check that config got loaded

.. code-block:: bash

  systemctl restart slurmctld
  systemctl restart slurmd
  scontrol show config | grep Backup

* Open tcp ports 6817 and 6818 on controller and backup node


Setup Slurmd on compute node
============================

* Install packages

.. code-block:: bash

  apt install slurmd munge

* Copy config  /etc/slurm-llnl/slurm.conf from controller node
* Copy munge shared key /etc/munge/munge.key from controller node
* Start munge and slurmd

.. code-block:: bash

  systemctl enable munge
  systemctl start munge

  systemctl enable slurmd
  systemctl start slurmd


Check cluster status
=====================

.. code-block:: bash

  sinfo -a
  scontrol show nodes


Submit a test batch job and show job queue
===========================================

.. code-block:: bash

  echo -en '#!/bin/bash\n\nsleep 10\nhostname\n' > test.sh; chmod a+rx test.sh; sbatch ./test.sh
  squeue
