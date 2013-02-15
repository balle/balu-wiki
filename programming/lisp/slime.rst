#####
SLIME
#####

Getting help
============

* , help - repl commands
* ctrl+c ctrl+d d - describe symbol
* ctrl+c ctrl+d h - hyperspec manual


Evaluation
==========

* ctrl+c ctrl+r - eval region
* ctrl+x ctrl+e - eval expression
* ctrl+c ctrl+z - jump to repl


Jumping around
==============

* alt+x slime-selector - jump around in lisp / slime buffer
* alt+. - jump to source
* alt+x slime-list-callers
* alt+p / n - previous / next warning / error


Autocompletion
==============

* ctrl+c TAB - autocomplete symbol
* ctrl+c ctrl+s - autocomplete form


Helpers
=======

* ctrl+alt+q - format lisp expression
* ctrl+c ctrl+k - compile whole file
* ctrl+alt+t transpose expressions
* ctrl+alt+k kill expression
* ctrl+c return - macro expansion


Debugger
========

* ctrl+c alt+i - inspect value
* ctrl+c ctrl+t trace expression
* (untrace)
* (on frame in stacktrace) alt+x sldb-show-source
* i - inspect frame


Using Swank for remote lisp repl
================================

* Starting swank server

.. code-block:: lisp

  (ql:quickload "swank")

  (setf swank:*use-dedicated-output-stream* nil)
  (setf swank:*communication-style* :fd-handler)
  (swank:create-server :dont-close t)

* Setup SSH tunnel on local Emacs machine

.. code-block:: bash

  ssh -L 4005:localhost:4005 me@remote-machine

* Reconnect slime with M-x slime-connect
