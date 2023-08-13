###########
Powershell
###########

Keyboard shortcuts for Powershell and Windows Terminal App
===========================================================

* Normal shortcuts like CTRL+A / CTRL+C / CTRL+V 
* CTRL+Shift+T new tab
* ALT+- new pane
* CTRL+TAB to switch tabs
* CTRL+ALT+1 goto first tab
* ALT+up/down switch panes
* CTRL+Shift+W close focused pane
* CTRL+left/right jump word back-/forwards
* CTRL+Backspace delete word

Profile handling
=================

* Edit profile

.. code-block:: powershell

  notepad.exe $profile

* Reload profile

.. code-block:: powershell

  &$profile

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

Measure execution time of a command
===================================

.. code-block:: powershell

  Measure-Command {some.exe param1 param2}
  
Start a service
===============

.. code-block:: powershell

  Start-Service -Name "sshd"
  Set-Service -Name "sshd" -StartupType Automatic

Show Routing table
==================

.. code-block:: powershell

  Get-NetRoute

Show IP adresses
================

.. code-block:: powershell

  Get-NetIPAddress

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
