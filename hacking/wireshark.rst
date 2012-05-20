#########
Wireshark
#########

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
