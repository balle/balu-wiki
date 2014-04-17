###
SSH
###

Local port forward
==================

* Local port 5555 gets forwarded to 25 on remote machine over ssh-host

.. code-block:: bash

  ssh -Nf -L 5555:remote-machine:25 user@ssh-host


Socks forward
=============

.. code-block:: bash

  ssh -D 5555 user@remote-machine

* Now connect your firefox to socks proxy port 5555 and it will tunnel everything over it


Ignore Host key
===============

.. code-block:: bash

  ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no
