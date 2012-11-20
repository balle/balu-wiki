############
PF (OpenBSD)
############

PF the BSD Firewall 
====================

All you will find here may as well work on freeBSD or netBSD but some thinks may work on ''openBSD''  only.

To let the openBSD a firewall between 2 or more networks you first have to set it up to forward traffic like defined in the routing table this is must off the time referred  as a gateway or router. 

Exec the following commands to enable IP Forwarding temporarily.

.. code-block:: bash

 sysctl net.inet.ip.forwarding=1

To make this setting permanent add the following line to the file /etc/sysctl.conf

.. code-block:: bash

 net.inet.ip.forwarding=1


pfctl 
=====

This utility is provided with every PF installation and controls the PF demon. The following commands can be used to control the PF firewall.

.. code-block:: bash

 pfctl -e # enable pf
 pfctl -ef <file-name> # load PF ruleset in file-name
 pfctl -d # disable pf
 pfctl -v # verbose output
 pfctf -nf <file-name> # compiles PF ruleset but do not load them (got for testing)

PF boot up 
==========

To start PF at boot up you have to add the following lines to the ''/etc/rc.conf.locale''

.. code-block:: bash

 pf=YES

PF reload 
==========

To restart, stop or start PF in a running system use:

.. code-block:: bash
 
 /etc/rc.dpf restart

PF Debugging 
============

PF could be simply debugged via the pflog0 interface that behaves as a normal interface. To see all traffic and its PF state use the command:

.. code-block:: bash
 
 tcpdump -netttti pflog0 
 
pf rules 
========

If not defined other in the ''/etc/rc.conf.locale'' the PF ruleset is configured in the file ''/etc/pf.conf'' 

processing the rules 
====================

Since version 4.2 die Option ''set rulset-optimization'' is set to ''basic'' which activates PF to optimize the ruleset when loading it into the kernel. 
 * remove duplicate rules
 * remove shadowing rules
 * put rules together for easy handling
 * resort the quick rules for better passing
If this Option is set to “profile” PF will use the loaded ruleset as a profile for the real network traffic to set the order for the quick rules to be most effective. 

simple client rule set
======================

From the client point of view the simplest ruleset would be to allow everything out to the internet but noting in from the internet.

.. code-block:: bash

 block in all
 pass out all keep state

You could even leave the ''keep state'' option away, because the PF firewall is keeping the state of the connections in default mode.

lists, macros and tables 
========================

To make you PF rules more readability you can us lists, macros and tables. 

.. code-block:: bash

 pass proto { tcp http https  } to port 80 # a list is defined in { } 
 ext_if = bxn0 # defines the macro ext_if 
 pass proto tcp on $ext_if # uses the macro ext_if
 testclient = 192.168.2.13
 table <client> persist {192.168.2.0, 192.168.2.5, $testclient} #defines the table client with a list of clients
 table <server> persist file "/etc/servers" # loads the line separated list of servers into the table server

To see the input in a table of a running PF firewall use:

.. code-block:: bash

 sudo pfctl -t clients -T -T show

keep it simple (IN ON, OUT ON or ALL) 
=====================================

If you change your point of view from the client side to the network as a gateway you will start to think about how to allow traffic between networks. For this you could have a rule like this:

.. code-block:: bash

 pass IN proto tcp ON server1 from server1:network to server2.network

If you like to let the traffic into the network of the server2, you will will have to define a second rule like this:

.. code-block:: bash

 pass OUT proto tcp ON server1 from server1:network to server2.network

To make your configuration more simple at this point you could define the following rule, which includes bout off the rules above.

.. code-block:: bash
 
 pass proto tcp from server1:network to server2:network

For every rule part that is not defined PF will set in ALL, that could be tricky at some times. SO be careful where and when to reduce you rules.

first small network rule set 
=============================

.. code-block:: bash

 # First define lists macros and tables
 ext_if = em0 # external interface
 int_if = em1 # internal interface
 int_net = $int_if:network # local network
 icmp_echoreq =  "echoreq"

 # start the rule set 
 block ALL # always the block rule first
 pass from { lo0, $int_net } # in loopback we trust
 
 # let everything pass from the internal network a nat rule is needed
 nat on $ext_if from $int_net to any -> ($ext_if)

 # troubleshooting friends

 # icmp if not allow all icmp allow echo requests for ping
 pass inet proto icmp icmp-type $icmp_echo_echoreq

 # allow traceroute to pass
 pass out on $ext_if inet proto udp port 33433 >< 33626 # opens the udp ports between 334433 and 33626 from the local network

shaping and bandwidth spliting queues 
=====================================

IN PF you could define 3 difrent types of ALTQ (Alternate Queueing). To see the stats of a queue you could use the following command. IF you like to have the traffic from a pas rule put into a queue you will have to add the queue after the pass rule with 'queue (queunames)' breakets

.. code-block:: bash

 systat queues

With priq (priority-based queues) ALTQ you could define 16 difrent prioritys from 0 - 1. Every queue rule needs a pass rule to so that the traffic could pass throuw the queue.

.. code-block:: bash

 # define a ALTQ priq
 ext_if="bnx0"
  altq on $ext_if priq bandwidth 10M queue { priorityQ, defaultQ }
    queue priorityQ priority 7
    queue defaultQ priority 1 priq(default)

 pass quick $ext_if proto tcp queue (defaultQ, priorityQ) 

With cbq (class-based queues) ALTQ you could define 8 diffrent prioritys with a procentage of the total bandwidth.

.. code-block:: bash

 # define a ALTQ cdq
 ext_if="bnx0"
  altq on $ext_if cdp bandwidth 10M { default, ssh, icmp }
    queue default bandwidth 65% cdq(default, borrow red)
    queue ssh bandwidth 30% cdq(borrow red) { ssh_default, ssh_bulk }
       queue ssh_default priority 7 bandwidth 30%
       queue ssh_bulk priority 0 bandwidth 70
    queue icmp bandwidth 5% cbq

With the 'borrow' argument the queue could borrow bandwidth from its parent queue while the 'RED' agument avoids  to borrow bandwidth from the parent queue.  Within a cbq you could also define a other queue like the ssh-default aund ssh_bulk queue.

With hfsc (hierachical Fair Service Curve) ALTQ allows you to define guarantions for minimum bandwidth allocation and hard upper limits. You could define 8 diffrent prioritys from 0 to 7. You even could allocate bandwidth over a spezified time.

.. code-block:: bash

 # define a ALTQ hfsc
 ext_if="bnx0"
  altq on $ext_if hfsc queue { default, icmp }
    queue default bandwidth 95% priority 7 qlimit 100 hfsc (realtime 60%, linkshare 90%) { defaultQ, webQ, sshQ, dnsQ }
       queue defaultQ bandwidth 10% priority 3 hfsc (realtime 20%, linkshare 50% red)
       queue webQ bandwidth 75% priority 7 hfsc (realtime 70%, linkshare 10% red)
       queue sshQ bandwidth 10% prioity 5 hfsc /realtime (realtime 50%, linkshare 30%)
       queue dnsQ bandwisth 5% priority 7 qlimit 100 hfsc (realtime (20Kb 3000 6Kb), linkshare 5%)
    queue icmp bandwidth 5% priority 0 qlimit 200 hfsc (realtime 0, upperlimit 2%, linkshare 90%)

With the 'realtime' agument you spezify the minimum bandwidht limit. The 'qlilit' argument spezify how many packets will be queueed if they could not be transmitted directly. 


Redundancy and Failover (CARP) 
==============================

The Common Address Redundancy Protocol (CARP) is open source and under the openbsd license it was developed as an alternative to the HSRP (Hot Standby Router Protocol) RFC 2281 from Cisco and the VRRP (Virtual Router Redundancy Protokol) RFC 3768 from Nikia.

The main funktion of the CARP protocol is to allow tow or more systms to be in charge for the same ip address and share it or to automaticaly take it over. If CARP is in active passive mode, the avtice maschine ist called the master and all passive maschines are called backup.

The CARP protocol like the HSRP and the VRRP protocol, is a multicast protocol. CARp and HSRP usees the mulitcast address asiend be IANA 224.0.0.18 to exchange there informations. This makes it extremly risky to not set a password for the carp comunication for hte security point of view. 

To exchange the pf states (mostly TCP states) the tool pfsync is needed. This allowes all systems to handel active connections correctly. The main disadvatage of pfsync is that its traffic is not authentified or encrypted. So the best way to use pfsec is to use dedicated ports and connect them over a cross over cable or use a host to host vpn to encrypt the traffic beetween the firewalls. Any way you shall not use the same IP frame used for your internal or external networks for the pfsync connection so that this inforamtions are not exchanged be mistake over the wrong interface.

To be able to use CARP with OpenBSD you will have to enable the following sysctl values.

.. code-block:: bash

 sysctl net.inet.carp.allow=1

To enable it over an reboot you will have to enable it in the /etc/sysctl.conf.

.. code-block:: bash

 net.inet.carp.allow=1

Passiv Active Mode 
==================

Here we are going to set up a active firewall and a identical secound firewall that should take over if the active firewall failes. The take over will work with no interuption of the active connection and no noticeable downtime.

IF you do not have a console based access to each maschine you should first of all assign a IP address to each interface that is not the virtual CARP IP. Otherweath you could could never know to with maschine you are connected and allows only get accesss to the maschie that is the avtice on in the CARP group and holds the virtual CARP IP.

For the following exaples we assume that we have the internal IP frame 192.168.0/24 and the external IP Frame 10.10.10/24. We will configure the IPs 192.168.0.1 as the internal CARP address and the IPs 10.10.10.1 as the external CARP address. To be able to communicate with the maschines we will give the active firewall the IP 192.168.0.2 and the passiv maschine the IP 192.168.0.3. The external interface we will just give an CARP IP to share between each other. For the pfsync connection we will configure 2 more Interfaces with the IPs 172.16.0.1/30 and 172.16.0.2/30. 

Setup pysikal internal interfaces 
=================================

To set up the IPs for the internal physikal interface add the following line in a file named /etc/hostname.<interface_name> with your faviried editor.  

.. code-block:: bash

 zile /etc/hostname.bnx1
 up description external interface
 zile /etc/hostname.bnx2
 192.168.0.2/24 description internal communication 
 
On the other maschien we do the same with the other ip

.. code-block:: bash

 zile /etc/hostname.bnx1
 up description external interface
 zile /etc/hostname.bnx2
 192.168.0.3/24 description internal communication 
 

To activate the interface execute the following command on both maschienes.

.. code-block:: bash

 /etc/netstart 

If you do not specify the interface name all interfaces will be configured as discribed in the /etc/hostname.* files.  You could also configure all interfaces via the ifconfig command but then the configration will be lost after an reboot.

Setup the CARP virtual interfaces 
=================================

A CARP interface is configured like other interfaces in /etc/hostname.carp<nummer>. It has needed parameters and optional parameters.

 * vhid (virtual host ID) hast to unique within the network broadcast domain. It is needed to identify the interfaces that shared the virtual IP address.
 * advbase This is the internal clock pulse generator of the carp connection. Eeach carp memebr sends its helo paket after this counter. The default value is 1. 
 * advskew This Parameter should be set for each backup. It is added to the advbase parameter so that the backend sends its helo packets slower then the master maschine. For this it also indicates how much less perferred a maschine is to take ofer the master. The higher the value the less likely it is that the maschien takes over the master state. The default value of this parameter is 0.
 * pass This specifies a password that if set is needed for all CARP interfaces that have the same vhid

With all this parameters the external and internal carp interface could be configured like this.

.. code-block:: bash

 zile /etc/hostname.carp1 
 10.10.10.1/24 vhid 2 advskew 20 carpdev bnx1  pass ppppp
 description external carp master
 zile /etc/hostname.carp2 
 192.168.0.1/24 vhid 1 advskew 20 carpdev bnx2 pass PPPPP
 description internal carp master

 zile /etc/hostname.carp1 
 10.10.10.1/24 vhid 2 advskew 120 carpdev bnx1 pass ppppp
 description external carp backup
 zile /etc/hostanme.carp2 
 192.168.0.1/24 vhid 1 advskew 120 carpdev bnx2 pass PPPPP
 description internal carp backup

To up this interfaces we need again to execute the command /etc/netstart

With this config the master is sending ist helo pakets each 1,20 secounds and the backend is sending the helo packet every 2,20 secounds.

State Synchronization (pfsync) 
==============================

To have a pf state-table synchronization, you will only need to configure a pysikal interface and a virtual pfsync interface to have the state synchronisation in openbsd, since pfsync is an virtual network interface.

.. code-block:: bash

 zile /etc/hostname.bnx0
 172.16.0.1/30
 description pysical sync interface
 zile /etc/hostname.pfsync0
 up syncdev bnx0 syncpeer 172.16.0.1

If you put a syncpeer option in the syncdev configuration the sync device will only exapte traffic from this ip and send the sync traffic to this IP. BUt this is only possible if you have only 1 backup maschie in your carp group. A other way to protect your sync traffic if to create a ipsec tunnel between the servers and run the sync traffic over it.

PF Rule Set 
============

Last but not least you will need a pf ruleset to be able to allow the traffic betweenn the interfaces.
