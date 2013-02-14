==============
Input / Output
==============

* Write file

.. code-block:: lisp

  (with-open-file (out filename
                   :direction :output
                   :if-exists :supersede)
     (with-standard-io-syntax
       (print *content* out))))

* Read file

.. code-block:: lisp

  (with-open-file (in filename)
    (with-standard-io-syntax
      (setf *content* (read in)))))

* Ask user for Input

.. code-block:: lisp

  (defun prompt-read (prompt)
    (format *query-io* "~a: " prompt)
    (force-output *query-io*)
    (read-line *query-io*))
