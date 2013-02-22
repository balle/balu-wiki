########
Parallel
########

Start thread
============

* Run a function in a thread in SBCL

.. code-block:: lisp

  (sb-thread:make-thread (a-function) :name "a good name")

* List all running threads

.. code-block:: lisp

  (sb-thread:list-all-threads)

* Check if a thread is running

.. code-block:: lisp

  sb-thread:thread-alive-p

* Kill a thread

.. code-block:: lisp

  sb-thread:terminate-thread

