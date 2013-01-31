####
UPNP
####

Overview
========

* Broadcast via 239.255.255.250 UDP port 1900
* Uses SOAP to exchange Information
* Method M-SEARCH to search for other devices
* Method NOTIFY to periodically send information
* GET /ctl/ContentDir returns root dir of a media / file service
* ISG protocol can be used to configure port forwards / nat
* http://www.ethicalhacker.net/content/view/220/1/

Search for devices
==================

* untested

.. code-block:: python

  from scapy.all import IP, UDP, sr1
  payload = "M-SEARCH * HTTP/1.1\r\n"
  r = sr1(IP(dst="239.255.255.250") / UDP(dport= 1900) / payload);
  r.display();


Search for services
===================

* untested

.. code-block:: python

  from scapy.all import IP, UDP, sr1
  target = "192.168.1.1"
  payload = "M-SEARCH * HTTP/1.1\r\nHost:%s:1900\r\nST: upnp:rootdevice\r\nMan:\"ssdp:discover\"\r\n" % target
  r = sr1(IP(dst=target) / UDP(dport= 1900) / payload);
  r.display();


Portforward
===========

* untested

.. code-block:: python

  from scapy.all import IP, UDP, sr1
  target="192.168.1.1"
  payload = "POST /upnp/control/igd/wanpppcInternet HTTP/1.1\r\n"
  payload += "Host: %s\r\n\r\n" % target
  payload += """<?xml version="1.0" ?>
  <s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s=
  "http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <u:AddPortMapping xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1">
            <NewRemoteHost/>
            <NewExternalPort>2200</NewExternalPort>
            <NewProtocol>TCP</NewProtocol>
            <NewInternalPort>22</NewInternalPort>
            <NewInternalClient>192.168.1.2</NewInternalClient>
            <NewEnabled>1</NewEnabled>
            <NewPortMappingDescription>SSH Tunnel</NewPortMappingDescription>
            <NewLeaseDuration>0</NewLeaseDuration>
        </u:AddPortMapping>
    </s:Body>
  </s:Envelope>"""
  r = sr1(IP(dst=target) / UDP(dport= 1900) / payload);
  r.display();


Tools & papers
==============

* https://community.rapid7.com/community/infosec/blog/2013/01/29/security-flaws-in-universal-plug-and-play-unplug-dont-play
* http://finux.co.uk/slides/UPnP-Revisted-BSidesLondon-2012-finux.pdf
* http://code.google.com/p/mirandaupnptool/
* http://www.gnucitizen.org/blog/hacking-the-interwebs/
