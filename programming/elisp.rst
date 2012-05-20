#####
Elisp
#####

Basics 
=======

* (message "hello world")

* setzt globale variable name

.. code-block:: lisp

  (setq name "balle")
  (message "hello %s" name)

* (setq name "balle") ist das selbe wie (set 'name "balle")

* local variables

.. code-block:: lisp

  (let ((var1 value) (var2 value2) do-something)

* var - liefert den wert einer variablen
* 'var - liefert den namen (var) einer variablen


listen 
=======

* jeder listen eintrag besteht aus 1. car (das element) 2. cdr (pointer auf das nächste element)
* der . in einer liste trennt car und cdr
* listen indiziert man mit (nth 2 (1 2 3 4 5)) -> 3
* an listen anhängen geht mit append
* pop liefert und entfernt das erste element
* push fügt vorne an die list an
* range bekommt man mit (number-sequence 1 9)

arrays 
=======

* array und list sind nicht das selbe! arrays sind strings, vectors, bool-vectors, char-tables
* text properties: #("muh" 0 3 (face bold))
* ein vector steht in [ ]
* length liefert die länge einer liste / array
* arrays indiziert man mit aref (aref [1 2 3] 1) -> 2


hashes 
=======

* #s(hash-table size 30 data (key1 val1 key2 300))
* gethash key table &optional default
* puthash key value table

functions 
==========

.. code-block:: lisp

  (defun balle-flyspell-add-word (&optional param)
  "doku"
  (interactive)
  )

* mit lamda macht man anonyme funktionen
* ein macro ist eine lambda function in einem symbol gespeichert
* let macht eine variable lokal


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

