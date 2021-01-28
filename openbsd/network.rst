########
Network
########

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


Connect to a Cisco Anyconnect VPN
==================================

* Install vpnc
* Edit /etc/vpnc/my.conf

.. code-block:: bash

  IPSec gateway vpn-gw-name
  IPSec ID groupname
  IPSec secret grouppassword
  Xauth username your-username
  Xauth password your-password


Enable IP forwarding
====================

To make the system route packets, execute

.. code-block:: bash

 sysctl net.inet.ip.forwarding=1

For a permanent configuration, edit  /etc/sysctl.conf and add

.. code-block:: bash

 net.inet.ip.forwarding=1


Which program is using a specific port
======================================

.. code-block:: bash

  fstat | grep ':22'


Display current network connections
===================================

.. code-block:: bash

  systat netstat


Ignore wifi deauth packets
==========================

.. code-block:: bash

  ifconfig urtwn0 nwflag stayauth

  
