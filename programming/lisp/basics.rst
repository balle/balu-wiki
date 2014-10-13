######
Basics
######

Overview
========

* (print "Hello world")
* (format "%s" "Hello world")
* create a global variable with ``defvar`` or ``defparameter``
* (setq name "balle") is the same as (set 'name "balle")

* local variables

.. code-block:: lisp

  (let ((var1 value) (var2 value2) do-something)

* use ``let*`` if vars must know each other during declaration
* var returns the value of var
* 'var returns a reference (the symbol) of var
* symbols are always treated like uppercase 
* quote or ' suspresses evaluation
* ` suspresses evaluation for all expression but prefixed with ,

* nil and () are the same
* with type-of you get the type of an object


Lists
=====

* ``car`` returns the first element of a list
* ``cdr`` returns all but the first element of a list
* ``cons`` adds a element in front of list by creating a new list
* ``nthcdr`` exec cdr nth times on list
* ``nth`` returns the nth element of the list staring with 0
* ``setcar`` replace first element of list
* ``setcdr`` replace all but first element of list
* ``append`` adds to a list by copying the first list
* ``nconc`` adds the second, third etc list to the first
* ``push`` insert an element at the beginning of the list
* ``pop`` returns and removes the first element
* ``(member what list)`` check if what is in list
* ``(position what list)`` get position of what in list
* ``(remove what list)`` remove element what from list (returns new list)
* ``(delete what list)`` remove element what from list directly
* ``(number-sequence 1 9)`` returns a list with numbers from 1 to 9
* ``first`` or ``car`` returns the first element of the list
* ``rest`` or ``cdr`` returns the rest of the list
* ``cadr`` is the same as (car (cdr alist))
* ``cdar`` is the same as (cdr (car alist))
* (:muh 1 :maeh 2) is a property list
* plist (property list) is a list with (:key value) pairs
* (getf list :keyword) returns value of keyword in a plist
* alist is a plist where you can also lookup by value using (assoc 'what-to-find my-list)
* plists and alists are still handled sequencially
* ``set-difference`` tells which items are in one list but not in another
* ``intersection`` tells which items are in both Lists
* ``remove-duplicates`` creates a unique list out of two or more lists
* ``(mapcar #'function alist)`` applys function on every list element and returns new list
* ``(mapc #'function alist)`` applys function on every list element without returning a new list


Sequence functions
==================

* ``length`` returns the number of the lists elements
* ``(map 'type #'function aseq)`` to loop through a sequence create a new 'type and apply function on ever element
* ``(reduce function aseq)`` calls function with next item and previous return value of function and thus reduces a sequence to one value
* ``(apply function aseq)`` Call function with remaining args, using last arg as list of args


hashes
=======

* #s(hash-table size 30 data (key1 val1 key2 300))
* gethash key table &optional default
* puthash key value table

Arrays
======

* make a resizeable array (init size is 5)

.. code-block:: lisp

  (make-array 5 :fill-pointer 0 :adjustable t)
  (vector-push-extend 'new-stuff my-array)
  (aref my-array 3)


Structures
==========

.. code-block:: LISP

  (defstruct person surname firstname age)
  (defvar hans (make-person :surname wurst :firstname hans :age 35))
  (person-age hans)


functions
==========

.. code-block:: lisp

  (defun hello (name)
  "function to say hello to someone or something"
    (print (concat "Hello " name)))
  (hello "world")

* parameter after ``&optional`` are optional
* default values for parameters

.. code-block:: lisp

  (defun some-func (a &optional (b 10)))

* define keyword arguments

.. code-block:: lisp

  (defun hello (&key name "world" by default))

* #' or function suspresses evaluation of functions (aka returns pointer)
* use lambda to define anonymous functions
* flet declares local functions
* labels command is for flet what let* is for let (functions know each other during definition)


control structures
==================

* equal check euqalness eq identity
* (eq "abc" "abc") -> nil
* (equal "abc" "abc") -> t
* check numbers with =
* (= 1 1) -> t
* check symbols with eq
* check everything else with equal

* if else

.. code-block:: lisp

  (if (eq "abc" "bcd")
    (progn do-this-if-cond-is-true)
    (progn do-this-if-cond-is-false)
  )


* ``when`` is an if without else that can handle multiple statements
* cond is a list of checks like if, else if, else if, else

.. code-block:: lisp

  (cond ((equal var value)
	(do-something))

      ((equal var value2)
	(do-something))

      (t
	(do-something))
  )

* there is also a switch case

.. code-block:: lisp 

  (case person
      ((hans)
         '(give him some food))
      ((wurst)
         '(run away screaming))
      ((otherwise)
         '(be cool)))


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

.. code-block:: lisp

  (loop for i from min to max by step)

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

* Disable style warnings in SBCL

.. code-block:: lisp

  (declaim #+sbcl(sb-ext:muffle-conditions style-warning))

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
* Packages are namespaces (like in Perl)
* A system is a bunch of code with instructions to install them plus their dependencies
* A module is something you can load to your lisp code


Channel
=======

* *standard-output*
* *error-output*, *debug-io* and *trace-output*
* *query-io* for user input


Redirect stdout
===============

.. code-block:: lisp

  (let ((*standard-output* (make-broadcast-stream)))
    (app:noisy-code))

Debugging
=========

* (trace) will trace function calls
* (step) through function calls
* (break) sets a break point


Links
=====

* http://ghostopera.org/blog/2012/06/24/the-newbie-guide-to-common-lisp/
* http://psg.com/~dlamkins/sl/contents.html - Successful lisp

