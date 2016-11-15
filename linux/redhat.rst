######
Redhat
######

Building a RPM package
======================

* Install rpmbuild
* Setup environment

.. code-block:: bash

  mkdir ~/rpmbuild
  cd ~/rpmbuild
  mkdir BUILD  BUILDROOT  RPMS  SOURCES  SPECS  SRPMS

* Put the source archive in the SOURCES directory (e.g. myprogram-0.1.tgz)
* Make a spec file in SPECS (e.g. myprogram.spec)

.. code-block:: bash

  Name:           myprogram
  Version:        0.1
  Release:        1
  Summary:        A short description

  Group:          System Environment/Libraries
  License:        GPL
  URL:            https://some.url.net
  Packager:       Your name <you@somewhere.net>

  Requires:       some_other_package>=1.2.3, another_package

  Source:         %name-%version.tgz

  %description
  Some longer description of this software package

  %prep
  %setup

  %build
  ./configure --prefix=%{buildroot}
  make

  %install
  rm -rf %{buildroot}
  make install

* Build the package

.. code-block:: bash

  rpmbuild -bb SPECS/myprogram.spec

* rpmbuild will complain that there are files that are not packaged. Put those into the %files section of the spec file

.. code-block:: bash

  %files
  /path/to/file1
  /path/to/file2

* Rebuild the package
* The RPM should now be available in the RPM subdir
* Only install dont recompile

.. code-block:: bash

  rpmbuild -bi --short-circuit SPECS/myprogram.spec

* Dont want to package all installable files?

.. code-block:: bash

  %define _unpackaged_files_terminate_build 0

* For more goto http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html-single/RPM_Guide/index.html


List contents of uninstalled rpm
================================

.. code-block:: bash

  rpm -qlp <rpm_file>

Unpack rpm without installing
=============================

.. code-block:: bash

  mkdir bla
  cd bla
  rpm2cpio ../ethjudge-backend-libs-1.4-4.el7.noarch.rpm | cpio -idvm


Check checksum of files in a rpm
=================================

* Installed rpm

.. code-block:: bash

  rpm -Vv <rpm_file>

* Uninstalled rpm

.. code-block:: bash

  rpm -V -p <rpm_file>


Exclude a package from update
=============================

* Edit /etc/yum.conf

.. code-block:: bash

  exclude=some_pkg*

Get all versions of a package and their repos
==============================================

.. code-block:: bash

  yum list <pkgname> --showduplicates


Downgrade a package
===================

.. code-block:: bash

  yum downgrade <pkgname>


Remove package with all dependencies
====================================

* Edit ``/etc/yum.conf``

.. code-block:: bash

  clean_requirements_on_remove=1


Examine installation history
============================

.. code-block:: bash

  yum history list [package]
  yum history info <id>


Revert an update
================

.. code-block:: bash

  yum history list
  yum undo <id>


Service Configuration
=====================

* List all available services and their status

.. code-block:: bash

  chkconfig --list


* Turn service on boot on or off

.. code-block:: bash

  chkconfig <service> [on|off]


* Start or stop a service

.. code-block:: bash

  service <service> [start|stop]


Firewall Config
===============

* Prefered tool is ``system-config-firewall``
* or lokkit

.. code-block:: bash

  lokkit -p 80:tcp
  lokkit -s http

* Script can be found under ``/etc/sysconfig/iptables`` but will be overwritten by the commands above


Bridged interface
=================

* /etc/sysconfig/network-scripts/ifcfg-br0

.. code-block:: bash

  DEVICE=br0
  TYPE=Bridge
  BOOTPROTO=dhcp
  ONBOOT=yes
  DELAY=0

* /etc/sysconfig/network-scripts/ifcfg-eth0

.. code-block:: bash

  BRIDGE=br0


Kickstart
=========

* The kickstart file used to setup the system can be found in /root/anaconda-ks.cfg


Gnome-Keyring
=============

* To reset Gnome-Keyring passwords run

.. code-block:: bash

  rm ~/.gnome2/keyrings/*


Setting up a chroot environment
===============================

.. code-block:: bash

  mkdir -p /data/redhat/var/cache/yum/x64_64/\$releaseserver
  cp /etc/yum.repos.d/redhat.repo /data/redhat/var/cache/yum/x64_64/\$releaseserver
  yum --disablerepo=* --enablerepo=redhat --disableplugin=* --installroot=/data/redhat install bash
