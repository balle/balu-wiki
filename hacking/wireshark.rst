#########
Wireshark
#########

Wifi
====

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


SSL
===

* Edit preferences -> protocols -> SSL
* Put the following into RSA key list

.. code-block:: bash

  192.168.x.x,443,http,/path/to/keyfile.pem;

* One could also specify 0.0.0.0 as ip, 0 as port and data as protocol

.. code-block:: bash

  tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list:,443,http,rsa_private.key" -o "ssl.debug_file:rsa_private.log" -r all.pcap -R "(tcp.port eq 443)" -V


Tshark
======

* Display all payload, dont do dns, dump to all.pcap
* -f "capture filter"
* -R "display filter"

.. code-block:: bash

  tshark -S -n -w all.pcap host www.datenterrorist.de
