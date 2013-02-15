==============
Input / Output
==============

* Write file

.. code-block:: lisp

(let ((stream (open "/some/file/name.txt" :direction :output)))
  (format stream "hello world~%")
    (close stream))

* or using a macro
* :if-exists :supersede will override an existing file

.. code-block:: lisp

  (with-open-file (out filename
                   :direction :output
                   :if-exists :supersede)
     (with-standard-io-syntax
       (print *content* out))))

* Read file

.. code-block:: lisp

  (let ((in (open "/some/file/name.txt" :if-does-not-exist nil)))
    (when in
      (loop for line = (read-line in nil)
               while line do (format t "~a~%" line))
                   (close in)))

* or using a macro

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
