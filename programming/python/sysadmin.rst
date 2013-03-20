######################
System Administration
######################

* How to use find in python

.. code-block:: python

  import commands
  print commands.getoutput("find /tmp")

* shutil has some useful shell commands as functions
* Run a command on some hosts via SSH (fab task)

.. code-block:: python

  from fabric.api import hosts, run

  @hosts('host1', 'host2')
  def task():
      run('uname -a')

* Get all files in a directory recursively

.. code-block:: python

  def get_files(dir):
      files = []

      for (path, subdirs, new_files) in os.walk(dir):
          for new_file in new_files:
              files.append(os.path.join(path, new_file))

      return files

ClusterShell
============

* create node sets (assume your hosts are named mynode001, mynode002 ...)
* create 2 set of nodes without node 100

.. code-block:: bash

  nodeset --split=2 -e "mynode[001-172]" -x mynode100

* group of nodes are managed in `/etc/clustershell/groups`
* e.g. create a group called mynodes
* run parallel commands in shell scripts

.. code-block:: bash

  clush -w @mynodes "uname -a"

* or python scripts

.. code-block:: python

  from ClusterShell.Task import task_self, NodeSet

  task = task_self()
  task.run("/bin/uname -r", nodes="mynode[001-123]")

  for output, nodes in task.iter_buffers():
      print NodeSet.fromlist(nodes), output

      
* diff output of nodes

.. code-block:: bash

  clush -w node[3-5,62] --diff dmidecode -s bios-version
  

Misc
====

* http://jessenoller.com/blog/2009/02/05/ssh-programming-with-paramiko-completely-different
* http://plumbum.readthedocs.org

