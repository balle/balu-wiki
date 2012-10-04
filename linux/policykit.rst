#########
Policykit
#########

Example config
==============

* E.g. /etc/polkit-1/localauthority/50-local.d/network-manager.pkla

.. code-block:: bash

  [User muh can configure network]
  Identity=unix-user:muh
  Action=org.freedesktop.NetworkManager.settings.modify.*
  ResultInactive=no
  ResultActive=auth_self


List all known actions
======================

.. code-block:: bash

  pkaction

