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
