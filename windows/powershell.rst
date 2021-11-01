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
