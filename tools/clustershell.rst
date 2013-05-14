############
Clustershell
############

Overview
========

* http://cloud.github.com/downloads/cea-hpc/clustershell/ClusterShell_UserGuide_EN_1.6.pdf


Define node groups
==================

* Edit ``/etc/clustershell/groups``

.. code-block:: bash

  node_all: cluster-node[001-999].somewhere.in-the.net


Run a command on all nodes
==========================

.. code-block:: bash

  clush -w @node_all "my_command with_params"


Iterate over nodes
==================

.. code-block:: bash

  for NODE in $(nodeset -e @node_all); do scp some_file root@$NODE:~/; done


Diff results
============

.. code-block:: bash

  clush -w @node_all --diff "dmidecode -s bios-version"


Combine results
===============

.. code-block:: bash

  clush -w @node_all -b "uname -a"


Copy file
=========

.. code-block:: bash

  clush -v -w @node_all --copy a_file


Retrieve a file
===============

* Will create files like ``id_rsa.node001``

.. code-block:: bash

  clush -v -w @node_all --rcopy /root/.ssh/id_rsa
