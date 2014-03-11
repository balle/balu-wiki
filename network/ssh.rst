###
SSH
###

Local port forward
==================

* Local port 5555 gets forwarded to 25 on remote machine

.. code-block:: bash

  ssh -L 5555:remote-machine:25 user@ssh-host


Socks forward
=============

.. code-block:: bash

  ssh -D 5555 user@remote-machine

* Now connect your firefox to socks proxy port 5555 and it will tunnel everything over it
