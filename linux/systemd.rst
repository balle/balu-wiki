#######
Systemd
#######

List all services and their status
==================================

.. code-block:: bash

  systemctl


An example service
==================

.. code-block:: bash

  [Unit]
  Description=Just a simple test
  After=syslog.target

  [Service]
  ExecStart=/bin/some-daemon
  Type=forking

  [Install]
  WantedBy=multi-user.target

* Afterwards exec 

.. code-block:: bash

  systemctl daemon-reload
  systemctl start test.service
  systemctl status test.service


Enable a service at boot time
=============================

.. code-block:: bash

  systemctl enable test.service


Chrooting
=========

* http://0pointer.de/blog/projects/changing-roots
