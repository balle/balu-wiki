######
Macros
######

Overview
========

* Macros generate code


Example
=======

.. code-block:: bash

  (defmacro thread (&rest body)
    `(sb-thread:make-thread (lambda () (progn ,@body)) :name ,(symbol-name (gensym))))

* ` defines partial evaluation (only code prefixed by , will get executed)
* the @ before body handles the variable as a list
* gensym generates a random symbol name
* this macro can be used like

.. code-block:: bash

  (thread (print "FOO") (print "BAR"))


Debugging
=========

* macroexpand resolves the real code of a macro
* the macro must be prefixed by ' otherwise it gets executed

.. code-block:: bash

  (macroexpand '(mymacro "param"))



