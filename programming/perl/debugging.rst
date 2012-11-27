#########
Debugging
##########

Pdb basics
==========

* s - single step
* n - next instruction
* <enter> - repeat previous command
* c (<line>) - continue (to line)
* p $var - print 
* b - set breakpoint
* b <condition e.g. $var eq "foo"> - conditional breakpoint
* L - list all breakpoints
* B <line|*> - delete breakpoint


Run pdb in emacs
================

* esc+x perldb


Enable debugger at runtime
==========================

* cpan Enbugger

.. code-block:: perl

  require Enbugger;
  Enbugger->stop;

  
REPL on fatal errors
====================

* cpan Carp::REPL

