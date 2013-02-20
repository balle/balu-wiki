#####
Shell
#####

* Execute a command on shell

.. code-block:: lisp

  (require 'asdf)
  (asdf:run-shell-command "touch foo")

* Reading output of command

.. code-block:: lisp

  (with-output-to-string (stream) (asdf:run-shell-command "ps ax" :output stream))

* or better

.. code-block:: lisp

  (ql:quickload "trivial-shell")
  (setq output (trivial-shell:shell-command "df -k"))

