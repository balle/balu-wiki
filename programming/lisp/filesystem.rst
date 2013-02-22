##########
Filesystem
##########

* (ql:quickload "cl-fad")
* http://weitz.de/cl-fad/

Get current directory
=====================

.. code-block:: lisp

  (truename ".")


List a directory
================

.. code-block:: lisp

  (directory (make-pathname :directory '(:absolute "var" "log") :name :wild :type :wild))

Parsing
=======

* Print filename and type

.. code-block:: lisp

  (pathname-name (pathname "/some/file.txt"))
  (pathname-type (pathname "/some/file.txt"))


Test if file exists
===================

.. code-block:: lisp

  (probe-file "/some/file")

