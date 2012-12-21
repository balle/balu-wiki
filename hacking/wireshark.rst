#########
Wireshark
#########

Shortcuts
=========

============ ============
Shortcut Description
============ ============
ctrl+k       Capture dialog
ctrl+e       Start / stop capture
alt+a        Analyze menu
alt+s        Statistics menu
ctrl+m       Mark packet
shift+ctrl+n Next marked packet
shift+ctrl+b Previous marked packet
============ ============


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

* With Analyze -> Display Filter Macros you can give complex display filter strings an easy name and even use parameters
* E.g. ICMP redirection not from gateway ip and save it under name icmp_redir

.. code-block:: bash

  icmp.type == 5 and ip.src != $1

* $1 will get replace by specified ip
* To use it type the following display filter

.. code-block:: bash

  ${icmp_redir:192.168.1.1}

* Macros are stored in ~/.wireshark/profiles/$profile/dfilter_macros

.. code-block:: bash

  "arp_req","arp.opcode == 0x0001"
  "arp_rep","arp.opcode == 0x0002"
  "echo_req","icmp.type == 8"
  "echo_rep","icmp.type == 0"
  "ssl_handshake","ssl.record.content_type==22"
  "nobeacons","wlan.fc.subtype != 8"
  "ssid","wlan_mgt.ssid == \x22$1\x22"
  "probes","wlan.fc.subtype==4 or wlan.fc.subtype==5"
  "dns_req","dns.flags.response == 0"
  "dns_res","dns.flags.response == 1"
  "dns_error","dns.flags.rcode != 0"
  "icmp_redir","icmp.type == 5 and ip.src != $1"


GeoIP
=====

* Make a new dir called geoip
* Download http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz and unzip it to that dir
* Add the dir to Preferences -> Name Resolution -> GeoIP database directories
* Restart wireshark
* Statistics -> Endpoints -> IPv4 -> Map
* Edit preferences -> protocols -> ipv4 -> enable geoip (optional to filter on geoip)
* To filter on geoip information use

.. code-block:: bash

  ip.geoip.country == "China"


HTTP
====

* Display filter

.. code-block:: bash
  http.response.code
  http.request.method
  http.host
  http.user_agent
  http.referer contains 
  http.content_type
  http.cookie

* Export html pages (File -> Export -> Objects -> HTTP)


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


Cheat Sheets
============

* General filtering http://packetlife.net/media/library/13/Wireshark_Display_Filters.pdf
* 802.11 http://www.willhackforsushi.com/papers/80211_Pocket_Reference_Guide.pdf
