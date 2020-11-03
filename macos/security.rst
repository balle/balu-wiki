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


Keychain
========

* Located at /Users/basti/Library/Keychains/login.keychain-db
* Can be displayed with

.. code-block:: bash

  security dump-keychain

* Display password using

.. code-block:: bash

  security find-generic-password -ga <acct_name>

