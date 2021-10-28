#######
General
#######

Ansible on Windows
==================

* Install Cygwin with Git and Ansible
* Install OpenSSH Server via "Additional Features" app
* Edit C:\ProgramData\ssh\sshd_config to change ListenAddress to 127.0.0.1
* Start service via services app

  
Find open port
==============

.. code-block:: bash

  netstat /an | findstr 22


Logs
====

* Open Event Log app


