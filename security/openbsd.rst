########
OpenBSD
########

What's missing (mid of 2019)?
=============================

* Bluetooth
* TRIM support for SSDs
* Adobe Flash


Filesystem tweaks
=================

* Configure soft updates everywhere (softdep)
* Disable access time logging (noatime)
* If possible mount with noexec, nosuid, nodev

.. code-block:: bash

  <duid> /home ffs rw,nodev,nosuid,noatime,softdep 1 2


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


Automatically adjust cpufreq
=============================

* Edit /etc/rc.conf.local

.. code-block:: bash

  apmd_flags="-A"


List all available disks
========================

.. code-block:: bash

  sysctl hw.disknames


List all open files
===================

* For a PID

.. code-block:: bash

  fstat -p <PID>

* For a user

.. code-block:: bash

  fstat -u <user>

  
Which program is using a specific port
======================================

.. code-block:: bash

  fstat | grep ':22'


Display current network connections
===================================

.. code-block:: bash

  systat netstat


Display I/O throughput
=======================

.. code-block:: bash

  systat iostat
  

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

* If you use tmux or screen put the following into ~/.profile

.. code-block:: bash

  export ENV=~/.kshrc


Which program is listening on port x?
=====================================

.. code-block:: bash

  fstat | grep internet | grep <port>


Ignore wifi deauth packets
==========================

.. code-block:: bash

  ifconfig urtwn0 nwflag stayauth

  
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


Login using Google authenticator or freeotp
============================================

.. code-block:: bash

  pkg_add login_oath

* Edit `/etc/login.conf`

.. code-block:: bash

  otp:\
        :auth=-totp-and-pwd:\
        :tc=default:

* Change users login class

.. code-block:: bash

  usermod -L otp username

* Generate random key

.. code-block:: bash

  openssl rand -base64 20 > ~/.totp-key
  chmod 700 /home/username
  chmod 700 /home/username/.totp-key
