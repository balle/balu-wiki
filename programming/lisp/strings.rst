#######
Strings
#######

Concatenate
===========

.. code-block:: lisp

  (concatenate 'string "foo " bar)


Split
=====

* (ql:quickload "cl-utilities")

.. code-block:: lisp

  (cl-utilities:split-sequence #\newline some-string)

