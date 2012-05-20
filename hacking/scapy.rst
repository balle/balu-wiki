#####
Scapy
#####

Basics 
=======

* Get all protocols

.. code-block:: bash

  ls()

* Get all options of a protocol

.. code-block:: bash

  ls(TCP)

* Get all commands

.. code-block:: bash

  lsc()

* Show description of function

.. code-block:: bash

  help(sniff)


=== Sending packets ===

* Just a simple Ping

.. code-block:: bash

  send(IP(dst="192.168.1.1")/ICMP())

* send() send on layer 3 (IP)
* sendp() send on layer2 (Ethernet)

* Send a packet on layer 3 and wait for response

.. code-block:: bash

  (resp, unans) = sr(IP(dst="192.168.1.1")/ICMP(), timeout=3)

* print destination packet

.. code-block:: bash

  print resp[0][1].show()

* sr1 for sending on layer2


Sniffing 
=========

.. code-block:: bash

  def handle_packet(packet):
      ip = packet.getlayer(scapy.IP)
      tcp = packet.getlayer(scapy.TCP)

      print "%s:%d -> %s:%d" % (ip.src, tcp.sport
                                ip.dst, tcp.dport)

  scapy.sniff(iface=dev, filter="tcp and port 80", prn=handle_packet)

* other way to decode the packet

.. code-block:: bash

  print packet[IP].src


Useful utils 
=============

* Generate random mac / ip

.. code-block:: bash

  RandMAC("*:*:*:*:*:*")
  RandIP("*.*.*.*")

* Get your own mac / ip

.. code-block:: bash

  get_if_hwaddr("eth0")
  get_if_addr("eth0")


Awesome oneliners 
==================

* Find sniffers on your network

.. code-block:: bash

  promiscping("192.168.1.0/24")

* SYN portscan

.. code-block:: bash

  ans, unans = sr(IP(dst="www.chaostal.de")/TCP(dport=range(1,1024), flags="S"), timeout=1)

* TCP fuzzer

.. code-block:: bash

  send(IP(dst="192.168.1.1") / fuzz(TCP()), loop=1)

* mac flooder

.. code-block:: bash

  sendp(Ether(src=RandMAC("*:*:*:*:*:*"), dst=RandMAC("*:*:*:*:*:*")) / IP(src=RandIP("*.*.*.*"), dst=RandIP("*.*.*.*")) / ICMP(), loop=1)
