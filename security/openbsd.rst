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
  cd /usr/src/sys/arch/$(uname -m)/compile/GENERIC
  make install
  reboot
  rm -rf /usr/obj/*
  cd /usr/src
  make obj
  cd /usr/src/etc && env DESTDIR=/ make distrib-dirs
  cd /usr/src
  make build


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
#       phase1="tls_disable_tlsv1=1 tls_disable_tlsv1_1=2" # if only sslv3 is supported
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
  
