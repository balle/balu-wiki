##########
Debugging
##########

Overview
========

* To turn on debug code in general insert the following to ``~/.sbclrc''

.. code-block:: lisp

  (sb-ext:restrict-compiler-policy 'debug 3)

* In debugger mode type ``?'' to get a list of available commands
  

Trace function calls
====================

.. code-block:: lisp

  (trace function)

* To undo

.. code-block:: lisp

  (untrace function)
  

Step through a function
=======================

* Every function you want to step into must be compiled with debug optimization, insert

.. code-block:: lisp

  (declaim (optimize (debug 3)))

* Now run
  
.. code-block:: lisp

  (step (function args))

* And use the command ``:step'' to step into NOT ``:next'' note the ``'""!

* With ``source 10'' you can see the source 10 levels (parantheses) deep
  

Invoke debugger at specific conditions
======================================

.. code-block:: lisp

  (ignore-errors ;Normally, this would suppress debugger entry
   (handler-bind ((error #'invoke-debugger)) ;But this forces debugger entry
     (error "Foo.")))


Breakpoints
===========

* Insert ``(break)'' at the specific code lines


Measure time of code execution
==============================

.. code-block:: lisp

  (time (function args))


Disassemble a function
======================

.. code-block:: lisp

  (disassemble 'format)
