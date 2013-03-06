####
Date
####

* (ql:quickload "local-time")

Timestamp for now
=================

.. code-block:: lisp

  (local-time:now)

* Get current month

.. code-block:: lisp

  (local-time:timestamp-month (local-time:now))


Universal time
==============

.. code-block:: lisp

  (get-universal-time)


Unix time
=========

.. code-block:: lisp

  (local-time:timestamp-to-unix (local-time:now))
