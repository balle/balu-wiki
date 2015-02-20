##########
Profiling
##########

* In Emacs

.. code-block:: bash

  elp-instrument-function
  elp-instrument-package

* In SBCL

.. code-block:: bash

  (require :sb-sprof)

  (defvar l '())
  (dotimes (x 10000) (push (random 10) l))
  (sb-sprof:with-profiling (:report :graph) (loop for x in l collect (* x 2)))
