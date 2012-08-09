####
Lisp
####

Basics
======

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
* ``quote`` or ``'`` can be used to bypass the evaluation of its argument


Lists
=====

* ``append`` adds to a list
* ``pop`` returns and removes the first element
* ``push`` insert an element at the beginning of the list
* ``(number-sequence 1 9)`` returns a list with numbers from 1 to 9
* ``length`` returns the number of the lists elements
* ``first`` or ``car`` returns the first element of the list
* ``rest`` or ``cdr`` returns the rest of the list


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





Links
=====

* http://ghostopera.org/blog/2012/06/24/the-newbie-guide-to-common-lisp/
