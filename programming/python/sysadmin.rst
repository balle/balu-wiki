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



