###########
Powershell
###########

Find a command
==============

.. code-block:: powershell

  Get-Command -Noun <search_string>

  
Read manual page
================

.. code-block:: powershell

  Get-Help <command> -Examples

Show end of file with continuos entries
=======================================

.. code-block:: powershell

  Get-Content -Tail 10 -Wait <Filename>

List directory sorted by last updated timestamp
===============================================

.. code-block:: powershell

  Get-ChildItem | Sort-Object LastWriteTime

List running processes
======================

.. code-block:: powershell

  Get-Process

  
Start a service
===============

.. code-block:: powershell

  Start-Service -Name "sshd"
  Set-Service -Name "sshd" -StartupType Automatic


List all member (methods and properties) of an object
=====================================================

* e.g. from process edge
  
.. code-block:: powershell

  Get Process -Name msedge | Get-Member

Filter objects
==============

.. code-block:: powershell

  Get-PSDrive | Where-Object { $_.free -gt 1 }
  

Count lines
===========

.. code-block:: powershell

  netstat -an | findstr /s LISTEN | Measure-Object -line

Loop
====

.. code-block:: powershell

  Get Process -Name msedge | ForEach-Object { $_.Kill() }


Recursive directory actions
===========================

.. code-block:: powershell

  get-childitem -Recurse C:\Users | foreach-object { S_.Name }


File Operations
===============

* Copy-Item
* Move-Item
* Rename-Item
* Remove-Item

Get product id of an app
========================

.. code-block:: bash

  get-wmiobject Win32_Product | Format-Table IdentifyingNumber, Name -AutoSize
