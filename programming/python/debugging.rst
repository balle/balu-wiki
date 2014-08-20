##########
Debugging
##########

Pdb
===

* pdb is the integrated (but quite unhandy) debugger
* To start it at a specific code point

.. code-block:: bash

  import pdb; pdb.set_trace()

* ``l`` to list the current code, ``p`` to print a variable, ``n`` for next statement, ``s`` to step-into and ``b`` for breakpoint
* use the power of ``dir()`` to get a list of attributes of a variable / class

Pudb
====

* Nice ncurses based debugger
* Same keybindings as pdb
* Install

.. code-block:: bash

  pip install pudb

* Afterwards edit /usr/lib/python2.6/site-packages/urwid/raw_display.py, go to ``signal_init`` and ``signal_restore``, comment out all code and insert ``pass``

* To invoke pudb

.. code-block:: bash

  import pudb; pudb.set_trace()

* To start a script in pudb

.. code-block:: bash

  python -m pudb.run yourfile.py


Winpdb
=======

* A graphical debugger with remote support and conditional breakpoints
* To invoke it

.. code-block:: bash

  import rpdb2; rpdb2.start_embedded_debugger("password")

* Now launch ``winpdb`` File --> Password, File --> Attach
* To tunnel winpdb through SSH

.. code-block:: bash

  ssh -C -N -f -L 51000:localhost:51000 user@$SERVER_HOST



Inject a pudb into a running process
====================================

* Install pyrasite
* Create a inject-pudb.py file

.. code-block:: bash

  import pudb;pudb.set_trace()

* Find pid of desired python process
* Inject the code

.. code-block:: bash

  pyrasite <pid> inject-pudb.py
