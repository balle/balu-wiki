########
Parallel
########

Start thread in SBCL
====================

* Run a function in a thread

.. code-block:: lisp

  (sb-thread:make-thread #'(lambda () (a-function)) :name "a good name")

* List all running threads

.. code-block:: lisp

  (sb-thread:list-all-threads)

* Check if a thread is running

.. code-block:: lisp

  sb-thread:thread-alive-p

* Kill a thread

.. code-block:: lisp

  sb-thread:terminate-thread


Start thread in CLISP
=====================

* Run a function in a thread

.. code-block:: lisp

  (MT:MAKE-THREAD #'a-function :name "a good name")

* List all running threads

.. code-block:: lisp

  (mt:list-threads)

* Check if a thread is running

.. code-block:: lisp

  (mt:thread-active-p "thread name")


Bordeaux Threads
================

* Portable thread library
* http://trac.common-lisp.net/bordeaux-threads/wiki/ApiDocumentation

.. code-block:: bash

  (ql:quickload "bordeaux-threads")
  (bordeaux-threads:make-thread (lambda () (print "MUH")) :name "balle")

