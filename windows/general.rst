#######
General
#######

Ansible on Windows
==================

* Install Cygwin with Git and Ansible
* Install OpenSSH Server via Settings -> Apps -> Apps and Features -> Optional Features -> Add a feature
* Edit C:\ProgramData\ssh\sshd_config to change ListenAddress to 127.0.0.1
* Start service via services app

  
Find open port
==============

.. code-block:: bash

  netstat /an | findstr 22


Logs
====

* Open Event Log app
* To log stuff like failed login attempts open local security policy app -> local policies -> audit

