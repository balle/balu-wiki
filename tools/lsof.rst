####
Lsof
####

Open files by ...
=================

* Pid

.. code-block:: bash

  lsof -p <pid>

* User

.. code-block:: bash

  lsof -u <pid>

* Program

.. code-block:: bash

  lsof -c <progname>


Which command is using this port?
=================================

.. code-block:: bash

  lsof -i :<port>


Which processes have an open TCP socket to remote-site
======================================================

.. code-block:: bash

  lsof -i TCP@remote:port


Which processes are using this file?
====================================

.. code-block:: bash

  lsof /path/to/file


What pids does that binary have?
================================

.. code-block:: bash

  lsof -t /path/to/command


Find all open files in a directory
===================================

.. code-block:: bash

  lsof +D /some/dir
