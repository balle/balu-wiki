########
Database
########

CLSQL
=====

* (ql:quickload "clsql")

.. code-block:: lisp

  (require "clsql")

  (setq *conn*
      (clsql:connect '("127.0.0.1" "mydb" "user" "secret") :database-type :mysql))
  (setq query "SELECT timestamp, value FROM data LIMIT 100;")

  (loop for row in (clsql:query query :field-names t) do
     (format t "~A ~,5F~%" (nth 0 row) (nth 1 row))



CL-DBI
======

* (ql:quickload "dbi")

.. code-block:: lisp

  (require "dbi")

  (setq *conn*
      (dbi:connect :mysql
                   :host "127.0.0.1"
                   :database-name "mydb"
                   :username "user"
                   :password "secret"))

  (setq query (dbi:prepare *conn* "select timestamp, value from data LIMIT 100;"))
  (setq result (dbi:execute query))

  (loop for row = (dbi:fetch result)
    while row
    do (format t "~A ~,5F~%" (getf row :|timestamp|) (getf row :|value|)))


Mongo
=====

* (ql:quickload "cl-mongo")

.. code-block:: lisp

  (use-package :cl-mongo)
  (db.use "test")
  (defvar *DOC* (make-document))
  (add-element "key" "value" *DOC*)`
  (db.insert "mycollection" *DOC*)
  (db.find "mycollection" (kv "key" "value"))


ORM
===

* http://common-lisp.net/project/elephant/index.html
* http://common-lisp.net/project/cl-prevalence/
