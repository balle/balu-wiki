#######
Regexp
#######

* http://weitz.de/cl-ppcre/
* (ql:quickload :cl-ppcre)

Match
=====

.. code-block:: Lisp

  (if (cl-ppcre:scan "^[1-9]+$" "23-")
    (print "muh"))

    
Split
=====

.. code-block:: lisp

  (cl-ppcre:split "\\s" "a cow says mooh")


Replace
=======

.. code-block:: lisp

  (cl-ppcre:regexp-replace-all "\\d" "h4llo" "a\\1")
  
