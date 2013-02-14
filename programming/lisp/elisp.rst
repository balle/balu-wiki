#####
Elisp
#####

Basics
=======

* (message "hello world")


Useful objects
==============

* current-buffer
* point


Useful functions
================

*  restore point and mark after executing do-something

.. code-block:: lisp

  (save-excursion do-something)

* open new buffer and swith to it

.. code-block:: lisp

  (pop-to-buffer "*Name*")

* ask user for parameter
* b buffer
* f file

.. code-block:: lisp

  (interactive "fFilename:")


Misc
=====

* http://www.emacswiki.org/emacs/ElispCookbook
* get integer value of char with ?
