#####
Elisp
#####

Basics
=======

* Go get a REPL with M-x ielm
* (message "hello world")


Performance
===========

* Use ``(goto-char (point-min))`` instead of ``(beginning-of-buffer)``


Handling Buffers
================

* Get object of current and most recent buffer

.. code-block:: bash

  (current-buffer)
  (other-buffer)

* Exec commands on another buffer without changing to it

.. code-block:: bash

  (set-buffer "name")

* Iterate over buffer list

.. code-block:: bash

  (dolist (buffer buffer-list)
    (message (concat "BLAH " (buffer-name buffer))))


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


Read file as list of lines
==========================

.. code-block:: bash

  (defun read-lines (filePath)
    "Return a list of lines of a file at filePath."
    (with-temp-buffer
      (insert-file-contents filePath)
      (split-string (buffer-string) "\n" t)))


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


Run as script
=============

.. code-block:: bash

  emacs --script myscript.el


Profiling
==========

.. code-block:: bash

  profiler-start
  profiler-report
  profiler-stop

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


Detect mode
============

.. code-block:: bash

  (when (derived-mode-p 'emacs-lisp-mode) (message "MUH"))


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

* Use common lisp (Emacs 24.3 and later)

.. code-block:: bash

  (require 'cl-lib)
  (cl-defun print-name (&key first (last "?"))

* Earlier Emacs versions

.. code-block:: bash

  (require 'cl)
  (defun* print-name (&key first (last "?"))

* Common Lisp interpreter written in Emacs Lisp https://github.com/larsbrinkhoff/emacs-cl
* Namespaces https://github.com/Bruce-Connor/names
* http://www.emacswiki.org/emacs/ElispCookbook
* get integer value of char with ?
