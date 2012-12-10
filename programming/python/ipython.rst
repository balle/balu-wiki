#######
Ipython
#######

Load a file into external editor
================================

.. code-block:: bash

  edit file

* Use Emacs

.. code-block:: bash

  EDITOR=emacsclient ipython
  edit file


Run a file
==========

.. code-block:: bash

  run file

Save code from shell
====================

.. code-block:: bash

  save filename.py 1-10

Display available namespaces
============================

.. code-block:: bash

  who

* Including data types

.. code-block:: bash

  whos


Get documentation
=================

* Use ? after module, function, whatever
* pinfo some module or function or whatever

Show source code of a function
==============================

.. code-block:: bash

  psource <function>

* Get whole source file

.. code-block:: bash

  pfile <function>


Edit a function
===============

* -x will not execute the new code

.. code-block:: bash

  edit <function>


Debugging
=========

* Switch on pdb on execptions

.. code-block:: bash

  pdb

* Run script in pdb

.. code-block:: bash

  run -d file

* Run script in pdb with breakpoint in line 23

.. code-block:: bash

  run -d -b 23 file

* Automatically start Ipython debugger on exception

.. code-block:: bash

  try:
    ret = 1 / 0
  except Exception, e:
    import sys, IPython
    IPython.Shell.IPShell(argv=[])
    IPython.Debugger.Pdb(IPython.ipapi.get().options.colors).set_trace(sys._getframe())


Profile
=======

.. code-block:: bash

  %time some_function

* Run cProfile

.. code-block:: bash

  %prun file or function

* Filter output

.. code-block:: bash

  %prun -l some_filter_string file or function


History
=======

* Show history

.. code-block:: bash

  hist

* Execute command nr x

.. code-block:: bash

  _ix

* Ranges (1-5)

.. code-block:: bash

  In[1:6]

* Print output of command 42

.. code-block:: bash

  Out[42]


Bookmarks
=========

* Create a dir bookmark

.. code-block:: bash

  bookmark name

* Save bookmark

.. code-block:: bash

  store name

* List bookmarks

.. code-block:: bash

  bookmark -l

* Delete bookmark

.. code-block:: bash

  bookmark -d name


Macros
======

* Save history commands 1-5 in a macro muh

.. code-block:: bash

  macro muh 1-5

* Save the macro

.. code-block:: bash

  store muh

* Execute it by calling its name
* Show the source

.. code-block:: bash

  print muh


Background jobs
===============

* Start a statement in the background

.. code-block:: bash

  bg some_func()

* Show status of job

.. code-block:: bash

  job[0].status

* Get the result

.. code-block:: bash

  job[0].result

