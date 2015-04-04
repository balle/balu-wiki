######
Debian
######

Install with sysvinit as init system
=====================================

* On boot screen of install medium type tab and append

.. code-block:: bash

  preseed/late_command="in-target apt-get install -y sysvinit-core"
		

How to build a deb package
==========================

* Unzip archive
* cd source
* dh_make -e me@mail.net -f ../tar-file
* choose single binary
* Edit debian/control file
* define dependency e.g.
* libssl0.9.8 (>= 0.9.8~)
* Enter description
* Edit debian/rules

.. code-block:: bash

  override_dh_auto_configure:
      dh_auto_configure -- --prefix=/opt/myprogram

* Move debian/init.d.ex to debian/myprogram.init and maybe edit it
* dpkg-buildpackage -rfakeroot -b


Setting up a chroot environment
===============================

.. code-block:: bash

  debootstrap unstable /data/debian-tree

