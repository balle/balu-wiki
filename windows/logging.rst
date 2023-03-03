########
Logging
########

View logs
=========

* Open Event Log app

Log failed login attempts
=========================

* Open local security policy app -> local policies -> audit

Using Powershell
================

* Show last 100 system logs

.. code-block:: bash

  Get-EventLog -LogName System -Newest 100

* Show summary of event logs

.. code-block:: bash

  Get-EventLog -List

Useful LogNames
===============

* Applicaten
* System
* HardwareEvents
