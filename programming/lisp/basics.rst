######
Basics
######

Overview
========

* (print "Hello world")
* (format "%s" "Hello world")
* create a global variable

.. code-block:: lisp

  (setq name "balle")

* (setq name "balle") is the same as (set 'name "balle")

* local variables

.. code-block:: lisp

  (let ((var1 value) (var2 value2) do-something)

* var returns the value of var
* 'var returns a reference on var
* quote or ' suspresses evaluation
* ` suspresses evaluation for all expression but prefixed with ,

* nil and () are the same
* with type-of you get the type of an object


Lists
=====

* ``append`` adds to a list
* ``pop`` returns and removes the first element
* ``push`` insert an element at the beginning of the list
* ``(number-sequence 1 9)`` returns a list with numbers from 1 to 9
* ``length`` returns the number of the lists elements
* ``first`` or ``car`` returns the first element of the list
* ``rest`` or ``cdr`` returns the rest of the list
* (:muh 1 :maeh 2) is a property list
* (getf list :keyword) returns value of keyword in list


hashes
=======

* #s(hash-table size 30 data (key1 val1 key2 300))
* gethash key table &optional default
* puthash key value table


functions
==========

.. code-block:: lisp

  (defun hello (name)
  "function to say hello to someone or something"
    (print (concat "Hello " name))
  )
  (hello "world")

* parameter after ``&optional`` are optional
* define keyword arguments

.. code-block:: lisp

  (defun hello (&key name "world" by default))

* use lamda to define anonymous functions
* let declares a local variable


control structures
==================

* equal check euqalness eq identity
* (eq "abc" "abc") -> nil
* (equal "abc" "abc") -> t
* check numbers with =
* (= 1 1) -> t

* if else

.. code-block:: lisp

  (if (eq "abc" "bcd")
    (progn do-this-if-cond-is-true)
    (progn do-this-if-cond-is-false)
  )


* do switch case with cond

.. code-block:: lisp

  (cond ((equal var value)
	(do-something))

      ((equal var value2)
	(do-something))

      (t
	(do-something))
  )


Loops
=====

* simple while

.. code-block:: lisp

  (while (< (count) 10)
    do-something
  )

* iterate each item of a list

.. code-block:: lisp

  (dolist (item list)
     (print item))

* or

.. code-block:: lisp

  (loop for i in '(1 2 3) do
    (print i))

* iterate over key, value pairs of a hash

.. code-block:: lisp

  (loop for k being the hash-key using (hash-value v) of h do (format t "~a ~a~%" k v))


Store state of interpreter in file
==================================

* SBCL

.. code-block:: lisp

  (SAVE-LISP-AND-DIE "foo.core")

* Load with

.. code-block:: bash

  sbcl --core foo.core

* CLISP

.. code-block:: lisp

  (saveinitmem "foo.mem")

* Load with

.. code-block:: bash

  clisp -M foo.mem


Scripting
=========

* SBCL

.. code-block:: lisp

  #!/usr/bin/sbcl --script

  (require ".sbclrc")

* CLISP

.. code-block:: lisp

  #!/usr/local/bin/clisp

  (require ".clisprc.lisp")


Installing modules
==================

* Install http://www.quicklisp.org/beta/

.. code-block:: lisp

  (ql:quicklib "module")


Loading modules
===============

* load is used to load a single lisp file
* require is used to load modules that can consist of more than one file


Whats the difference between packages, systems and modules?
===========================================================

* http://weitz.de/packages.html
* Packages are, loosely speaking, containers for symbols
* A system is a bunch of code with instructions to install them plus their dependencies
* A module is something you can load to your lisp code


Channel
=======

* *standard-output*
* *error-output*, *debug-io* and *trace-output*
* *query-io* for user input


Redirect stdout
===============

.. code-block::

  (let ((*standard-output* (make-broadcast-stream)))
    (app:noisy-code))


Links
=====

* http://ghostopera.org/blog/2012/06/24/the-newbie-guide-to-common-lisp/
* http://psg.com/~dlamkins/sl/contents.html - Successful lisp

