########
Security
########

Sandboxing
==========

Check if an application is using sandboxing

.. code-block:: bash

  asctl sandbox check <appname>

The containers can be found in "˜/Library/Containers"


System Integrity Protection
===========================

Protects system binaries and libs from being modified.
Can be controlled by ``csrutil``


Firewall
========

Enable firewall in system preferences / security & privacy and let it block all incoming connections
