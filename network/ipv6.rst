####
IPv6
####

Special addresses
=================

================== ================================================
Address            Description
================== ================================================
::                 Any address / Whole net
::1                Loopback
2000::/3           Global unicast addresses (like public ipv4 addresses, can start with a 2 or 3)
fe80::/10          Link local address (not routable, mostly based on devices mac)
fc00::/7           IPv6 equivalent to 10.0.0.0/8 (unique local addresses can start with fc or fd)
fec0::/10          Deprecated site local address range now also used for private local networks
ff00::/8           Multicast
================== ================================================

Anycast
=======

The same IPv6 address can be assigned to multiple devices making the address an anycast address than the packet would be send to the closest device with that address.
