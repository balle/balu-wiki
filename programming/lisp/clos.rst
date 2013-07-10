#################################
CLOS - Common Lisp Object System
#################################

Overview
========

* Its class based, but
* Methods are not bound to objects
* Objects are bound to methods
* It supports multiple inheritance
* There is no enforce encapsulation (like in python) everyone can directly access all slots (properties) of an object


Example
=======

.. code-block:: bash

  (defclass vehicle ()
    ((wheels)
     (color
      :initarg :black)))

  (defclass automobile (vehicle)
    ((wheels
      :initarg :4)))

  (defclass motorbike (vehicle)
    ((wheels
      :initarg :2)))

  (defmethod drive ((vehicle automobile))
    (format *standard-output* "Driving a car~%"))

  (defmethod drive ((vehicle motorbike))
    (format *standard-output* "Flying over the street with a motorbike~%"))

  (defvar ferrari (make-instance 'automobile))
  (defvar kawasaki (make-instance 'motorbike))

  (drive ferrari)
  (drive kawasaki)
