###############
NetworkManager
###############

Console interface
=================

* List connections

.. code-block:: bash

  nmcli c

* Start / stop a connection

.. code-block:: bash

  nmcli c up/down <connection>


Applet
======

.. code-block:: bash

  nm-applet --sm-disable


Edit connections
================

.. code-block:: bash

  nm-connection-editor
