####
IPv6
####

Special addresses
=================

================== ================================================
Address            Description
================== ================================================
\:\:                 Any address / Whole net
::1                Loopback
2000::/3           Global unicast addresses (like public ipv4 addresses, can start with a 2 or 3)
fe80::/10          Link local address (not routable, mostly based on devices mac)
fc00::/7           IPv6 equivalent to 10.0.0.0/8 (unique local addresses can start with fc or fd)
fec0::/10          Deprecated site local address range now also used for private local networks
ff00::/8           Multicast
ff01::1            Multicast address for all nodes (interface local scope)
ff01::2            Multicast address for all router (interface local scope)
ff01::fb           Multicast address for MDNSv6 (interface local scope)
ff02::1            Multicast address for all nodes (link local scope, like IPv4 broadcast)
ff02::2            Multicast address for all router (link local scope)
ff02::fb           Multicast address for MDNSv6 (link local scope)
ff05::2            Multicast address for all router (site local scope)
ff05::fb           Multicast address for MDNSv6 (site local scope)
================== ================================================

Anycast
=======

The same IPv6 address can be assigned to multiple devices making the address an anycast address than the packet would be send to the closest device with that address.
