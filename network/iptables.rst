###########
IPtables
###########

Example script
==============

.. code-block:: bash

  #!/bin/bash

  ###[ Config ]###

  LOGLIMIT=20
  IPTABLES=/usr/sbin/iptables
  IP6TABLES=/usr/sbin/ip6tables


  ###[ CLEANUP RULE ]###

  # Erstmal alle Rules loeschen...
  echo "Deleting old rules"
  $IPTABLES -F
  $IPTABLES -t nat -F
  $IP6TABLES -F


  ###[ CREATING NEW CHAINS ]###

  echo "Creating chains"

  # Chain to log and reject a port by ICMP port unreachable
  $IPTABLES -N LOGREJECT
  $IPTABLES -A LOGREJECT -m limit --limit $LOGLIMIT/minute -j LOG --log-prefix "FIREWALL REJECT " --log-level notice --log-ip-options --log-tcp-options
  $IPTABLES -A LOGREJECT -j REJECT --reject-with icmp-port-unreachable


  ###[ PROC MANIPULATION ]###

  # Enable IP Forwarding
  #echo "Enabling IP forwarding"
  #echo 1 > /proc/sys/net/ipv4/ip_forward

  # Dont respond to broadcast pings
  echo "Disabling broadcast pings"
  echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts

  # Halt die Klappe bei komischen ICMP Nachrichten
  echo "Enabling bogus ICMP message protection"
  echo 1 > /proc/sys/net/ipv4/icmp_ignore_bogus_error_responses

  # Enable SYN Flood protection
  echo "Enabling SYN FL00D protection"
  echo 1 > /proc/sys/net/ipv4/tcp_syncookies

  # Kick all IP Spoofing shit
  # (Enable source validation)
  echo "Disabling IP Spoofing attacks"
  echo 1 > /proc/sys/net/ipv4/conf/all/rp_filter

  # Logge seltsame Pakete
  echo 1 > /proc/sys/net/ipv4/conf/all/log_martians

  # Set default TTL to 61 (default for Linux is 64)
  echo "Setting default TTL to 61"
  echo 61 > /proc/sys/net/ipv4/ip_default_ttl

  # Sende RST Pakete raus, wenn der Buffer voll ist
  echo 1 > /proc/sys/net/ipv4/tcp_abort_on_overflow

  # Warte max. 30 Sekunden auf ein FIN/ACK.
  # Schliesse danach den Socket
  echo 30 > /proc/sys/net/ipv4/tcp_fin_timeout

  # Gib nach 3 SYN/ACK Paketen den Verbindungsaufbau auf
  # Default ist 6
  echo 3 > /proc/sys/net/ipv4/tcp_synack_retries


  ###[ MAIN PART ]###

  # Set default policy
  echo "Setting default policy DROP"
  $IPTABLES -P INPUT DROP
  $IPTABLES -P FORWARD DROP
  $IPTABLES -P OUTPUT ACCEPT
  $IP6TABLES -P INPUT DROP
  $IP6TABLES -P FORWARD DROP
  $IP6TABLES -P OUTPUT ACCEPT

  # Be stateful
  echo "Be stateful"
  $IPTABLES -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
  $IPTABLES -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
  $IPTABLES -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

  # In the loopback device we trust all other we monitor ;)
  echo "Trust loopback"
  $IPTABLES -A INPUT -i lo -j ACCEPT
  $IP6TABLES -A INPUT -i lo -j ACCEPT

  $IPTABLES -A INPUT -i tap0 -j ACCEPT

  # ICMP is ok
  echo "ICMP"
  $IPTABLES -A INPUT -p icmp -j ACCEPT

  # Erlaube SSH Logins
  echo "SSH"
  $IPTABLES -A INPUT -p tcp --dport 22 -j ACCEPT

  # Verbindungsversuche loggen und rejecten
  # Der Rest wird eh per Default Policy gedroppt
  echo "Reject and log all other packets"
  $IPTABLES -A INPUT -p tcp --syn -j LOGREJECT
  $IPTABLES -A FORWARD -p tcp --syn -j LOGREJECT

Showing rules 
=============

* Show all rules with interfaces

.. code-block:: bash

  iptables -L -n -v

* Show all NAT rules

.. code-block:: bash

  iptables -L -t nat -n -v
