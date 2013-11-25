#######
Systemd
#######

List all units and their status
==================================

.. code-block:: bash

  systemctl

* List only services

.. code-block:: bash

  systemctl list-units --type=service


List all failed services
========================

.. code-block:: bash

  systemctl --failed

Start / Stop service
====================

* All services can be found in `/usr/lib/systemd/system`

.. code-block:: bash

  systemctl [start|stop] sshd.service

Activate service on boot
========================

.. code-block:: bash

  systemctl enable sshd.service

Show status and ongoing log messages of a service
=================================================

.. code-block:: bash

  systemctl status sshd.service -f


Filtering logs
==============

* Since last boot

.. code-block:: bash

  journalctl -b


* Since today

.. code-block:: bash

  journalctl --since today

* Or timerange

.. code-block:: bash

  journalctl --since=2012-10-15 --until="2011-10-16 23:59:59"

* For a specific file

.. code-block:: bash

  journalctl /some/file


* Tailed

.. code-block:: bash

  journalctl -f


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


Power management
================

.. code-block:: bash

  systemctl suspend
  systemctl hibernate


Use systemd as inetd
====================

* http://0pointer.de/blog/projects/inetd.html


Chrooting
=========

* Set up chroot environment with yum or debootstrap or whatever
* Old school with chroot()

.. code-block:: bash

  [Service]
  RootDirectory=/srv/chroot/foobar

* New age with kernel namespaces

.. code-block:: bash

  systemd-nspawn -D <chroot_dir> <command>

* For more see http://0pointer.de/blog/projects/changing-roots


More security options
======================

* Disable networking

.. code-block:: bash

  PrivateNetwork=yes

* Isolate tmp dir

.. code-block:: bash

  PrivateTmp=yes

* Read-only or inaccessible directories

.. code-block:: bash

  InaccessibleDirectories=/home
  ReadOnlyDirectories=/var

* Use capabilities (see man capabilities)

.. code-block:: bash

  CapabilityBoundingSet=CAP_CHOWN CAP_KILL

* Use process limits

.. code-block:: bash

  LimitNPROC=1
  LimitFSIZE=0

* Limit device usage

  DeviceAllow=/dev/null rw

* Run as a specific user / group

.. code-block:: bash

  User=nobody
  Group=nobody
