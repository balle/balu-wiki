#####
Elisp
#####

Basics
=======

* (message "hello world")


Handling Buffers
================

* Get object of current and most recent buffer

.. code-block:: bash

  (current-buffer)
  (other-buffer)

* Exec commands on another buffer without changing to it

.. code-block:: bash

  (set-buffer "name")


Switch to an existing buffer or create a new one
=================================================

* To create a new one just enter a not existing name as string

.. code-block:: bash

  (switch-to-buffer (other-buffer))
  (switch-to-buffer-other-window "some-new-buffer")


Working with directories
========================

.. code-block:: bash

  (directory-files "~/")



Cursor
==============

* point-min ; beginning of buffer
* point ; current position
* point-max ; end of buffer


Shell
=====

* Execute a shell command with ``call-process-shell-command``


Function
=========

* ask user for parameter in (interactive) function
* b existing buffer
* B buffer name but doesnt need to exist
* d position of point
* D directory
* f file
* r region
* s text

.. code-block:: lisp

  (interactive "fFilename:")


Profiling
==========

.. code-block:: bash

  profiler-start
  profiler-stop
  profiler-result

* You can expand lines with a + by pressing RET


Debugging
=========

* ``trace-function``
* ``edebug-all-defs``
* ``edebug-defun`` behind function definition
* <SPC> - execute next expression
* n - next debuggable statement
* c - continue
* i - step into
* b - set breakpoint
* x - set conditional breakpoint
* u - unset breakpoint
* g - goto next breakpoint
* h - goto here
* d - backtrace
* e - eval expression e.g. (symbol-value 'some-var)


Misc
=====

*  restore point and mark after executing do-something

.. code-block:: lisp

  (save-excursion do-something)

* Run a command if user is idle

.. code-block:: bash

  (defun balle()
  (message "MUH"))

  (run-with-idle-timer 10 t 'balle)

* http://www.emacswiki.org/emacs/ElispCookbook
* get integer value of char with ?
