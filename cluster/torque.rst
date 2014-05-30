######
Torque
######

Overview
========

* Controller runs ``pbs_server`` and ``pbs_sched``
* Edit ``/var/lib/torque/server_priv/nodes`` to add all compute nodes (np = number of processors, gpus = number of gpus)

.. code-block:: bash

  pulsar np=4
  pulsar-mobile np=4


* Compute nodes run ``pbs_mom`` after editing ``/etc/torque/mom/config``
* Verify that all nodes are connected to the controller

.. code-block:: bash

  pbsnodes -a


Submitting jobs
===============

.. code-block:: bash

  qsub <my_cool_tool>

* Check the job queue with ``qstat -n``
