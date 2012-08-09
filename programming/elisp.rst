#####
Elisp
#####

Basics
=======

* (message "hello world")


listen
=======

* jeder listen eintrag besteht aus 1. car (das element) 2. cdr (pointer auf das nächste element)
* der . in einer liste trennt car und cdr


vergleiche
===========

* equal prüft auf gleichheit eq auf identität
* (eq "abc" "abc") -> nil
* (equal "abc" "abc") -> t
* zahlen prüft man mit =
* boolean prüft man mit t


kontrollstrukturen
===================

* switch case wird durch cond eingeleitet

.. code-block:: lisp

  (cond ((equal var value)
	(do-something))

      ((equal var value2)
	(do-something))

      (t
	(do-something))
  )

* selbe wie { do-something }

.. code-block:: lisp

  (progn do-something)

  (if (eq "abc" "bcd")
    (progn do-this-if-cond-is-true)
    (progn do-this-if-cond-is-false)
  )


schleifen
==========

.. code-block:: lisp

  (while (< (count) 10)
    do-something
  )


Nützliche Objekte
==================

* current-buffer
* point


Nützliche Funktionen
=====================

*  restore point and mark after executing do-something

.. code-block:: lisp

  (save-excursion do-something)

* open new buffer and swith to it

.. code-block:: lisp

  (pop-to-buffer "*Name*")

* erfrage parameter vom user
* b buffer
* f file

.. code-block:: lisp

  (interactive "fFilename:")


Misc
=====

* http://www.emacswiki.org/emacs/ElispCookbook
* mit ? kann man den integerwert eines characters erfahren
* symbols, die mit : beginnen sind keywords / constants
* nil und () sind das selbe (leere liste)
* mit type-of erfährt man den typ eines objects (type-of 23)
