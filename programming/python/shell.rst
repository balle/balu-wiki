############
Python Shell
############

* Attach python console to a running process with [http://code.google.com/p/rfoo/|rconsole]

* Stop a running process by signal and let it drop you to a python console

.. code-block:: bash

  import code
  import signal
  signal.signal(signal.SIGUSR2, lambda sig, frame: code.interact())

  user@shell> kill -SIGUSR2 <PID>
