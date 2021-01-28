####################
Software management
####################

Ports
=====

* Checkout stable ports branch

.. code-block:: bash

  echo "FETCH_PACKAGES=yes" >> /etc/mk.conf
  cd /usr
  cvs -qd anoncvs@anoncvs.ca.openbsd.org:/cvs get -rOPENBSD_6_8 -P ports

* Which packages / ports need to be updated?

.. code-block:: bash

  /usr/ports/infrastructure/bin/out-of-date

* Update a port

.. code-block:: bash

  cd /usr/ports/<portname>
  make update

* Possible binary updates through packages from https://stable.mtier.org/ and https://mtier.org/solutions/apps/openup/


Update base system
==================

.. code-block:: bash

  syspatch
  

Upgrade to a new release
=========================

* Refer to the upgrade documentation e.g. http://www.openbsd.org/faq/upgrade68.html

.. code-block:: bash

  sysupgrade

* If you cannot or dont want to upgrade by CD / USB / PXE / sysupgrade use the ``Upgrade without the Install Kernel`` documentation


Flash support
=============

* Adobe and Chrome flash plugins do not work on OpenBSD
* But you can use Gnash in Firefox

.. code-block:: bash

  pkg_add gnash
  mkdir /home/<user>/.mozilla/firefox/<account_id>.default/plugins
  cd /home/<user>/.mozilla/firefox/<account_id>.default/plugins
  ln -s /usr/local/lib/mozilla/plugins/libgnashplugin.so


Readmes for packages
====================

* Can be found in /usr/local/share/doc/pkg-readmes


Automatic installation over PXE
===============================

* Possible with autoinstall
* http://www.bsdnow.tv/tutorials/autoinstall


Building images for cloud and embedded devices
===============================================

* Read http://stable.rcesoftware.com/resflash/


