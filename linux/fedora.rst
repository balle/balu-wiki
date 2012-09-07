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

  plymouth-set-default-theme text
