######
Cisco
######


Allgemeines
============

* com2usb linux driver pl2303.ko
* running config mit passwörtern anzeigen

.. code-block:: bash

  more system:running-config

* man kann nur von grösseren security level auf kleinere routen
* mit enable (oder en) kommt man in den enable modus
* mit conf t in den configurations modus
* befehle kann man mit tab vervollständigen
* mögliche optionen erfährt man mit ?
* mit "no" vor einem befehl löscht man eine config zeile

* config speichern mit "copy running-config startup-config"

* system auslastung anzeigen

.. code-block:: bash

  show cpu usage
  show processes
  show mem


Grundconfiguration
===================

* hostname lalala
* domain-name schwubs.tld

* Zeitzone und NTP einstellen

.. code-block:: bash

  clock timezone CET 1
  ntp server 192.168.100.1
  sh clock

* user anlegen

.. code-block:: bash

  username <user> password <password> privilege 15

* enable passwort setzen

.. code-block:: bash

  aaa authentication enable console LOCAL

* SSH und Consolen User lokal authentifiziert

.. code-block:: bash

  aaa authentication ssh console LOCAL

* sh run interface

* interface resetten

.. code-block:: bash

  interface Management0/0
  no nameif
  no security-level 100
  no ip address
  no management-only

* interface config anschauen

.. code-block:: bash

  sh run interface Management0/0
  interface Management0/0
  no nameif
  no security-level
  no ip address

  interface Ethernet0/0
  description WAN interface
  ip address 192.168.103.91 255.255.255.0 standby 192.168.103.92
  security-level 0
  nameif external
  no shut

* SSH Config

.. code-block:: bash

  ssh 192.168.103.0 255.255.255.0 external
  crypto key generate rsa general-keys modulus 2048
  write mem



Routing
========

* Default Gateway setzen (device ip mask gateway)

.. code-block:: bash

  route external 0.0.0.0 0.0.0.0 192.168.103.254

* Routing Tabelle anzeigen

.. code-block:: bash

  sh route

* source validation anschalten

.. code-block:: bash

  ip verify reverse-path interface <iface>


VLAN
======

* trunk port = port der in mehreren vlans hängt

.. code-block:: bash

  interface Management0/0.1
  description LAN Failover Interface
  vlan 8
  interface Management0/0.2
  description STATE Failover Interface
  vlan 9

* wenn man kein vlan angibt, dann sind bei einem trunk port per default alle erlaubt

* VLAN config anschauen

.. code-block:: bash

  sh vlan


ARP
=====

* ARP Cache anzeigen lassen

.. code-block:: bash

  sh arp



NAT
====

* nat-control (alle connections müssen eine nat rule haben)
* alles was aus external raus geht nimm per default die adresse vom external device

.. code-block:: bash

  global (external) 1 interface

* alles was aus interface patronas raus kommt natte mit id 1 also auf das externe interface

.. code-block:: bash

  nat (patronas) 1 192.168.109.176 255.255.255.240

* Alles was nat id 0 hat wird nicht genattet

.. code-block:: bash

  access-list NO_NAT deny ip any any
  nat (patronas) 0 access-list NO_NAT

* Statisches NAT (dev intern, dev extern) (192.168.109.215 wird genattet auf 192.168.103.93)

.. code-block:: bash

  static (axxion,external) 192.168.103.93 192.168.109.215 netmask 255.255.255.255


Logging und Debugging
======================

.. code-block:: bash

  logging enable
  logging console ?
  logging console 6

* wenn man via ssh connected is nimmt man monitor und nicht console

.. code-block:: bash

  logging monitor 7
  term monitor


Packet Filtering / Access lists
================================

* Access list anlegen

.. code-block:: bash

  access-list EXTERNAL_IN permit icmp any any source-quench
  access-list EXTERNAL_IN permit icmp any any unreachable
  access-list EXTERNAL_IN permit tcp any host 192.168.109.215 eq 22

* Access liste an ein interface binden

.. code-block:: bash

  access-group EXTERNAL_IN in interface external

* bei genatteten verbindung brauch man nur die nat ip erlauben das weiterleiten wird dann automatisch erlaubt


Packet Capturing
=================

* Alles was durch die Access-List gelassen wird, wird aufgezeichnet

.. code-block:: bash

  access-list CAP permit ip any any
  capture CAP interface patronas access-list CAP

* Aufgezeichnete Pakete anzeigen

.. code-block:: bash

  sh capture CAP

* Aufzeichnen stoppen

.. code-block:: bash

  no capture CAP

* Allen Traffic auf einem Interface capturen

.. code-block:: bash

  access-list CAP interface external


Failover
=========

* Die Failover IP für LAN muss in einem anderen Netz sein als das für State

.. code-block:: bash

  failover
  failover lan unit primary
  failover lan interface lan-fo Management0/0.1
  failover key Fmjhd3
  failover replication http
  failover link state-fo Management0/0.2
  failover interface ip lan-fo 192.168.109.193 255.255.255.252 standby 192.168.109.194
  failover interface ip state-fo 192.168.109.197 255.255.255.252 standby 192.168.109.198

* sh run failover (config anzeigen)
* sh failover (status anzeigen)

* monitoring bei logischem device anschalten

.. code-block:: bash

  monitor interface patronas

* Die Slave Firewall von der Master aus rebooten

.. code-block:: bash

  failover reload-standby


Firewall Desaster Recovery
===========================

* Es muss sichergestellt sein, dass Ethernet 0/2 auf beiden ASA das aktive Interface ist

.. code-block:: bash

  interface Redundant1
  redundant-interface Redundant 1 active-member Ethernet 0/2


IPSec / VPN
============

* crypto isakmp enable <interface>
* crypto isakmp identity address

* Phase 1 (control connection definieren)
* sh crypto isakmp sa detail

.. code-block:: bash

  crypto isakmp policy 1
  authentication pre-share
  encryption 3des
  hash md5
  group 5
  lifetime 3600

* Phase 2 (data connection definieren)
* sh crypto ipsec sa peer <$VPN_PEER>
* Transform Set definieren (Name für Verschlüsselung / Hashing Optionen für die wirklichen Datentunnel)

.. code-block:: bash

  crypto ipsec transform-set ESP-AES-256-MD5 esp-aes-256 esp-md5-hmac
  crypto ipsec transform-set ESP-3DES-MD5 esp-3des esp-md5-hmac

* Optional maximale Timeouts für das Rekeying definieren

.. code-block:: bash

  crypto ipsec security-association lifetime seconds 28800
  crypto ipsec security-association lifetime kilobytes 4608000

* Name für VPN Peer anlegen

.. code-block:: bash

  name 213.23.72.194 VPN_PEER_TEST

* Welcher Traffic getunnelt werden soll, wird über eine Accesslist (CMAP_$VPN_MAP) definiert
* Die Src muss immer dem Netz der Firewall entsprechen

.. code-block:: bash

  access-list CMAP_TEST_MATCH extended permit ip 192.168.109.176 255.255.255.240 192.168.103.0 255.255.255.0
  access-list CMAP_TEST_MATCH extended permit ip 192.168.109.176 255.255.255.240 192.168.100.0 255.255.255.0
  access-list CMAP_TEST_MATCH extended permit ip 192.168.109.208 255.255.255.240 192.168.103.0 255.255.255.0
  access-list CMAP_TEST_MATCH extended permit ip 192.168.109.208 255.255.255.240 192.168.100.0 255.255.255.0
  access-list CMAP_TEST_MATCH extended permit ip host 123.123.122.66 host 192.168.100.3
  access-list CMAP_TEST_MATCH extended permit ip host 123.123.122.66 host 192.168.100.1
  access-list CMAP_TEST_MATCH extended permit ip 192.168.109.224 255.255.255.240 192.168.100.0 255.255.255.0
  access-list CMAP_TEST_MATCH extended permit ip 192.168.109.224 255.255.255.240 192.168.103.0 255.255.255.0

  * WICHTIG! Genau die selben Regeln müssen auch in die NO_NAT Access-List eingetragen werden

  * Eine Cryptomap ist eine Sammlung von Phase2 gebunden an ein Interface
  * Identifiziert wird über die Zahl z.B. 20

.. code-block:: bash

  crypto map CMAP_STATIC 20 match address CMAP_TEST_MATCH
  crypto map CMAP_STATIC 20 set peer VPN_PEER_TEST
  crypto map CMAP_STATIC 20 set transform-set ESP-AES-256-MD5

  * Optional Perfect Forwarding Secrecy (PFS) einschalten
    * Erzwingt das ein neuer Schlüssel beim Rekeying generiert wird

.. code-block:: bash

  crypto map CMAP_STATIC 20 set pfs

    * Macht immens Probleme zwischen unterschiedlichen Peers

* PreShared Key vergeben
* Hier muss immer die IP verwendet werden
* l2l heisst LAN-to-LAN

.. code-block:: bash

  tunnel-group 123.123.11.22 type ipsec-l2l
  tunnel-group 123.123.11.22 general-attributes
  tunnel-group 123.123.11.22 ipsec-attributes
  pre-shared-key <password>

* Beispiel für einen neuen Tunnel

.. code-block:: bash

  name 123.124.222.5 VPN_PEER_BLA

  access-list CMAP_BLA_MATCH extended permit ip host 192.168.109.213 host 123.222.147.10
  access-list NO_NAT extended permit ip host 192.168.109.213 host 123.222.147.10

  crypto map CMAP_STATIC 40 match address CMAP_BLA_MATCH
  crypto map CMAP_STATIC 40 set pfs
  crypto map CMAP_STATIC 40 set peer VPN_PEER_BLA
  crypto map CMAP_STATIC 40 set transform-set ESP-3DES-MD5
  crypto map CMAP_STATIC 40 set security-association lifetime seconds 28800
  crypto map CMAP_STATIC 40 set security-association lifetime kilobytes 4608000

  tunnel-group 193.228.147.5 type ipsec-l2l
  tunnel-group 193.228.147.5 general-attributes
  default-group-policy VPN
  tunnel-group 193.228.147.5 ipsec-attributes
  pre-shared-key <password>

* PPPOE configuration

.. code-block:: bash

  interface Vlan2
  nameif outside
  security-level 0
  pppoe client vpdn group QSC
  ip address pppoe setroute

  vpdn group ISP request dialout pppoe
  vpdn group ISP localname [your username here]
  vpdn group ISP ppp authentication chap
  vpdn username [your username here] password [your password here ]



Switch Config
==============

* ip domain-name patronas.int
* user spass

.. code-block:: bash

  aaa new-model
  username <user> password 0 <pass>

* ssh server für 15 terminals freischalten

.. code-block:: bash

  line vty 0 15
  transport input ssh

* switch ports sind standardmaessig in vlan1

* trunk port configurieren

.. code-block:: bash

  switchport mode trunk
  switchport trunk allowed vlan 8,9

* einen port in ein vlan hängen

.. code-block:: bash

  switchport access vlan 10

* eine andere art vlan zu confen (im enable mode)

.. code-block:: bash

  vlan database
  vlan <nr> name <name>
  int vlan <nr>
  ip add x.x.x.x

* default gateway einstellen

.. code-block:: bash

  ip default-gateway 192.168.1.1

* lacp config

.. code-block:: bash

  switchport mode access
  channel-protocol lacp
  channel-group 1 mode active


Firmware update on a Cisco device
==================================

* Setup a TFTP server in the same IP range as the Cisco device to backup the configs, IOS image and also for later to upload the new IOS image.

.. code-block:: bash

  testrouter# copy startup-config tftp
  Address or name of remote host []? 10.10.10.2
  Destination filename [startup-config]?
  !!
  1278 bytes c opied in 0.100 secs

* Backup Current IOS Image

.. code-block:: bash

  testrouter# copy flash: tftp:
  Source filename []? xxxxx-xx-xx.121-x.XB
  Address or name of remote host []? 10.10.10.2
  Destination filename [xxxxx-xx-xx.121-x.XB]?

* Now, Load the new IOS image from the TFTP onto the flash

.. code-block:: bash

  ciscorouter#copy tftp: flash:
  Address or name of remote host []? 10.10.10.2
  Source filename []? c3560-ipbasek9-mz.122-40.SE.bin
  Destination filename [c3560-ipbasek9-mz.122-40.SE.bin]?
  Accessing tftp://10.10.10.2/c3560-ipbasek9-mz.122-40.SE.bin
  Loading c3560-ipbasek9-mz.122-40.SE.bin



How to repair a Cisco with erased flash
========================================

* copy xmodem: flash:flash_filename
* now from the "transfer" dropdown menu on the hyperterminal, select "send file" and choose "xmodem" in the subsequent dialog box and browse for the flash_filename (the downloaded IOS bn file) and send.
* boot flash:flash_filename
