#######
Systemd
#######

List all units and their status
==================================

* All running

.. code-block:: bash

  systemctl

* List only services

.. code-block:: bash

  systemctl list-units --type=service

* All available

.. code-block:: bash

  systemctl list-unit-files


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

* For a single pid

.. code-block:: bash

  journalctl _PID=123

* For a single user

.. code-block:: bash

  journalctl -u <user>

* For a service

.. code-block:: bash

  journalctl _SYSTEMD_UNIT=<unit name e.g. sshd.service>

* For kernel messages

.. code-block:: bash

  journalctl _TRANSPORT=kernel

* For network stuff

.. code-block:: bash

  journalctl _COMM=network

* For a SELinux context

.. code-block:: bash

  journalctl _SELINUX_CONTEXT=<security context>


* Where to find the log files?

.. code-block:: bash

  cd /var/log/journal

* How to configure max hd space for logs? Edit /etc/systemd/journald.conf

.. code-block:: bash

  SystemMaxUse=100M

* Log rotation (/etc/systemd/journald.conf)

.. code-block:: bash

  MaxRetentionSec=1day
  MaxFileSec=1month

* How to log to syslog (edit /etc/systemd/journald.conf)

.. code-block:: bash

  ForwardToSyslog=yes

* Export log as JSON

.. code-block:: bash

  -o json


Journald Web Gateway
====================

* Install systemd-journal-gateway
* Start service systemd-journal-gateways
* Connect your browser to http://<ip>:19531
* To get an endless stream http://<ip>:19531/entries?follow
* To pull remote journal log an save it to a text file

.. code-block:: bash

  nohup curl --silent -o some-host.log 'http://<ip>:19531/entries?follow' &

* Or to pull it in the original journal format

.. code-block:: bash

  nohup curl --silent -H'Accept: application/vnd.fdo.journal' -o some-host.log 'http://<ip>:19531/entries?follow' &


Rescue Mode / Debugging
=======================

* On Grub prompt try to set one of the following kernel parameter

.. code-block:: bash

  systemd.unit=rescue.target      # (single user mode)
  systemd.unit=emergency.target   # (only shell)

* Ask before starting a servce

  systemd.confirm_spawn=1

* Give me more log output

.. code-block:: bash

  systemd.log_target=kmsg systemd.log_level=debug

* Get console output of legacy sysv init scripts

.. code-block:: bash

  systemd.sysv_console=1


* Which units want which target?

.. code-block:: bash

  systemctl show -p "Wants" multi-user.target

* To analyze which services was slow

.. code-block:: bash

  systemd-analyze blame


What services do get started?
=============================

.. code-block:: bash

  systemctl list-dependencies multi-user.target


Change runlevel
===============

.. code-block:: bash

  systemctl isolate <newtarget e.g. rescue.target or mutli-user.target>


Changing the default runlevel
=============================

.. code-block:: bash

  ln -sf /usr/lib/systemd/system/multi-user.target /etc/systemd/system/default.target


An example service
==================

.. code-block:: bash

  [Unit]
  Description=Just a simple test
  After=syslog.target

  [Service]
  ExecStart=/bin/some-daemon
  Type=forking
  CPUShares=1500
  MemoryLimit=1G
  BlockIOWeight=500

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


I want more gettys / text consoles
==================================

.. code-block:: bash

  ln -sf /usr/lib/systemd/system/getty@.service /etc/systemd/system/getty.target.wants/getty@tty9.service


Python Coding
=============

* http://www.freedesktop.org/software/systemd/python-systemd/
* https://pypi.python.org/pypi/pyjournalctl/0.7.0
