#######
Fabfile
#######

.. code-block:: python

  from fabric.api import hosts, run

  @hosts('host1', 'host2')
  def task():
      run('uname -a')
