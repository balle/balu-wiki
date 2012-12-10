#########
Wireshark
#########

Wifi
====

* View -> Wireless Toolbar
* http://sharkfest.wireshark.org/sharkfest.10/B-5_Parsons%20HANDS-ON%20LAB%20-%20WLAN%20Analysis%20with%20Wireshark%20&%20AirPcap%20Exercises.pdf
* hide beacons

.. code-block:: bash

  wlan.fc.subtype != 8

* filter by ssid

.. code-block:: bash

  wlan_mgt.ssid == "Spatula City"

* only sniff data frames

.. code-block:: bash

  wlan.fc.subtype == 2

* sniff probe request / response

.. code-block:: bash

  wlan.fc.subtype==4 or wlan.fc.subtype==5


WEP / WPA
=========

* Decrypt WEP / WPA traffic with existing key
* Preferences -> Protocols -> IEEE 802.11 -> Enable decryption + Add decryption keys


SSL
===

* Edit preferences -> protocols -> SSL
* Put the following into RSA key list

.. code-block:: bash

  192.168.x.x,443,http,/path/to/keyfile.pem;

* One could also specify 0.0.0.0 as ip, 0 as port and data as protocol
* Afterwards right click on packet and choose Follow SSL Stream
* Filter SSL handshake

.. code-block:: bash

  ssl.record.content_type==22

* Decrypt and display data from dump file

.. code-block:: bash

  tshark -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list:,443,http,rsa_private.key" -o "ssl.debug_file:rsa_private.log" -r all.pcap -R "(tcp.port eq 443)" -V


Detect ARP storms
=================

* Preferences -> Protocols -> ARP -> Detect ARP request storms


Macros
======

* With Analyze -> Display Filter Macros you can give complex display filter strings an easy name


Tshark
======

* Display get requests, dont do dns, dump all packets with payload to all.pcap
* -f "capture filter"
* -R "display filter"
* -S decode payload
* -V Display complete packet

.. code-block:: bash

  tshark -S -n -w all.pcap -f "host www.datenterrorist.de" -R "http.request.method==GET"

* Capture traffic for 10 seconds, display traffic analysis for all ips

.. code-block:: bash

  tshark -q -a duration:10 -z conv,ip

* Sniff cookies

.. code-block:: bash

  tshark -T fields -e http.cookie -R "http.cookie" port 80

