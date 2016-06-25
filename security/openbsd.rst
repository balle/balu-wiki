########
OpenBSD
########

Filesystem tweaks
=================

* Configure soft updates everywhere (softdep)
* Disable access time logging (noatime)
* If possible mount with noexec, nosuid, nodev

.. code-block:: bash

  <duid> /home ffs rw,nodev,nosuid,noatime,softdep 1 2


Ports and packages
==================

* Packages dont get security updates!
* Therefore configure ports to use packages if possible
* And follow the stable ports branch

.. code-block:: bash

  echo "FETCH_PACKAGES=yes" >> /etc/mk.conf
  cd /usr
  cvs -qd anoncvs@anoncvs.ca.openbsd.org:/cvs get -rOPENBSD_5_9 -P ports

* Which packages / ports need to be updated?

.. code-block:: bash

  /usr/ports/infrastructure/bin/out-of-date

* Update a port

.. code-block:: bash

  cd /usr/ports/<portname>
  make update

* Possible binary updates through packages from https://stable.mtier.org/


Update base system
==================

* Follow patch branch

.. code-block:: bash

  cd /usr
  cvs -qd anoncvs@anoncvs.ca.openbsd.org:/cvs get -rOPENBSD_5_9 -P src
  cd /usr/src/sys/arch/$(uname -m)/conf
  config GENERIC
  cd /usr/src/sys/arch/$(uname -m)/compile/GENERIC
  make clean && make
  make install
  reboot
  rm -rf /usr/obj/*
  cd /usr/src
  make obj
  cd /usr/src/etc && env DESTDIR=/ make distrib-dirs
  cd /usr/src
  make build


Upgrade to a new release
=========================

* Refer to the upgrade documentation e.g. http://www.openbsd.org/faq/upgrade59.html
* If you cannot upgrade by CD / USB / PXE use the ``Upgrade without the Install Kernel`` documentation


Set clock to localtime
======================

.. code-block:: bash

  ln -sf /usr/share/zoneinfo/right/CET /etc/localtime
  rdate -ncv time.fu-berlin.de


Increase / derease volumne
===========================

.. code-block:: bash

  mixerctl outputs.master=100,100


WPA-PSK
=======

* Create /etc/hostname.<ifname>

.. code-block:: bash

  nwid <ssid>
  wpa
  wpakey <passphrase>
  dhcp


WPA enterprise
===============

* Install wpa-supplicant
* Create /etc/wpa-supplicant.conf

.. code-block:: bash

  ctrl_interface=/var/run/wpa_supplicant
  ctrl_interface_group=wheel

  ap_scan=0
  eapol_version=1
  fast_reauth=1

  network={
        key_mgmt=WPA-EAP
	proto=WPA2
	eap=PEAP # or TTLS
        pairwise=CCMP
	group=CCMP
	phase1="peaplabel=0"
  #     phase1="tls_disable_tlsv1=1 tls_disable_tlsv1_1=2" # if only sslv3 is supported
	phase2="auth=MSCHAPV2"
	ca_cert="/etc/certs/QV2.pem"
	ssid="<ssid>"
	identity="<username>"
	password="<mysecetpass>"
  }

* You must setup wiki card before running wpa_supplicant!
* It is better to set the bssid
* wpaakms must be configure otherwise wpa_supplicant will fail!

.. code-block:: bash

  ifconfig urtwn0 nwid <ssid> bssid <mac_of_ap> wpa wpaakms 802.1x up
  wpa_supplicant -B -c /etc/wpa_supplicant.conf -D openbsd -i urtwn0


UTF-8 system-wide
=================

.. code-block:: bash

  echo 'export LC_ALL="en_US.UTF-8"' >> /etc/profile
  echo 'export LC_ALL="en_US.UTF-8"' >> ~/.xsession


Adjust max memory size
======================

* Edit /etc/login.conf

.. code-block:: bash

  :datasize-max=1024M:\
  :datasize-cur=1024M:\

* Or set `infinity:` as value
  
		      
NTFS
====

* Built-in NTFS support is read-only
* Install ntfs-3g from ports to get write support


Flash support
=============

* Adobe and Chrome flash plugins do not work on OpenBSD
* But you can use Gnash in Firefox

.. code-block:: bash

  pkg_add gnash
  mkdir /home/<user>/.mozilla/firefox/<account_id>.default/plugins
  cd /home/<user>/.mozilla/firefox/<account_id>.default/plugins
  ln -s /usr/local/lib/mozilla/plugins/libgnashplugin.so


Permanently disable kernel features like ACPI
==============================================

.. code-block:: bash

  mv /bsd /bsd.old
  config -e -o /bsd /bsd.old
  ukc>disable acpi
  ukc>quit


Linux compatibility (untested yet)
==================================

* Currently only works on i386!
* You may need to build a custom kernel

.. code-block:: bash

  cd /usr/src/sys/arch/$(uname -m)/conf
  cp GENERIC.MP MYKERNEL
  echo "option COMPAT_LINUX" >> MYKERNEL
  config MYKERNEL
  cd ../compile/MYKERNEL
  make depend
  make
  make install
  reboot

* Now you can activate it with

.. code-block:: bash

  sysctl kern.emul.linux = 1

* And start your Linux program
* If it is dynamically linked you need to provide all libs under /emul/linux (easiest way is to unzip a base package e.g. fedorabase there)
* For more information see http://www.openbsd.org/papers/slack2k11-on_compat_linux.pdf


List all available disks
========================

.. code-block:: bash

  sysctl hw.disknames


Ksh config
==========

* ~/.kshrc

.. code-block:: bash

  export PS1='\[\t\] \u@\h:\w\$ '
  export EDITOR=/usr/local/bin/zile

  set -o emacs

  alias cp='cp -i'
  alias mv='mv -i'
  alias rm='rm -i'


Which program is listening on port x?
=====================================

* Install lsof

.. code-block:: bash

  lsof -i :<port>


Readmes for packages
====================

* Can be found in /usr/local/share/doc/pkg-readmes


Fix arrow keys in Emacs under Xorg
==================================

.. code-block:: lisp

  (if (not window-system)                        ;; Only use in tty-sessions.
    (progn
      (defvar arrow-keys-map (make-sparse-keymap) "Keymap for arrow keys")
      (define-key esc-map "[" arrow-keys-map)
      (define-key arrow-keys-map "A" 'previous-line)
      (define-key arrow-keys-map "B" 'next-line)
      (define-key arrow-keys-map "C" 'forward-char)
      (define-key arrow-keys-map "D" 'backward-char)))


Automatic installation over PXE
===============================

* Possible with autoinstall
* http://www.bsdnow.tv/tutorials/autoinstall


Tracing kernel calls
====================

* Comparable to strace on Linux

.. code-block:: bash

  ktrace -t cn <program>
  kdump | less


Building images for cloud and embedded devices
===============================================

* Read http://stable.rcesoftware.com/resflash/
