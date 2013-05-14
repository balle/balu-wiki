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


Clush.conf
==========

* Need ssh password auth? Install sshpass and edit /etc/custershell/clush.conf

.. code-block:: bash

  ssh_user: root
  ssh_path: /usr/bin/sshpass -p "password"
  ssh_options: -oStrictHostKeyChecking=no


Scripting in Python
===================

.. code-block:: python

  from ClusterShell.Task import task_self, NodeSet

  task = task_self()
  task.run("/bin/uname -r", nodes="mynode[001-123]")

  for output, nodes in task.iter_buffers():
      print NodeSet.fromlist(nodes), output
