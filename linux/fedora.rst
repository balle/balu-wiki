######
Fedora
######

Restart network
===============

.. code-block:: bash
 
  systemctl restart NetworkManager.service
i

Allow SELinux exception
=============l==========

* Click on selinux alert in bottom right corner
* Click on Troubleshoot
* Paste solution as root


Configure startup applications
==============================

.. code-block:: bash

  gnome-session-properties


Disable boot logo
=================

.. code-block:: bash

  plymouth-set-default-theme details


Gnome3 settings
===============

* Install gnome-tweak-tool
* Install gconf-editor


Changing keyboard shortcuts
===========================

* Applications -> System Tools -> System Settings -> Keyboard


Default shortcuts
=================

* Alt+F1 - Switch between overview and desktop view
* Alt+F2 - Launch command
