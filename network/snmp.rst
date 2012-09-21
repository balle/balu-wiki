####
SNMP
####

get all info
============

.. code-block:: bash

  snmpwalk -Os -c public -v 1 $host .

print numeric OIDs
==================

.. code-block:: bash

  snmpwalk -On -c public -v 1 $host .
  
set a special info
==================

.. code-block:: bash

  snmpset -c public -v 1 192.168.1.1 ipDefaultTTL.0 i 66

Exceute command via snmp (in snmpd.conf)
========================================

.. code-block:: bash

  exec muh /some/command

Install a new MIB file
=======================

* Copy the file (e.g. MY-MIB.txt) to /usr/share/snmp/mibs

.. code-block:: bash

  snmpwalk -Of -v 1 -c public -m +MY-MIB 192.168.1.1 .
  
Translate a MIB to its number
=============================

* maybe you need to delete the last .0

.. code-block:: bash

  snmptranslate -m ALL -On <mib>
  

Scripting with Perl
===================

.. code-block:: perl

#!/usr/bin/perl

use strict;
use Net::SNMP;
use Time::HiRes qw(usleep nanosleep);

my $snmp_host = "127.0.0.1";
my $snmp_version = 1;
my $snmp_community = "public";

my $oid = "";

my ($snmp, $error) = Net::SNMP->session(-hostname => $snmp_host,
                                        -version => $snmp_version,
                                        -community => $snmp_community);

die "SNMP connect to $snmp_host failed: $error\n" if $error;

while (1)
{
    my $results = $snmp->get_request(-varbindlist => [ $oid_a_total, $oid_w_total, $oid_kwh_total, $oid_pf_total ]);
    print join("", values(%$results)) . "\n";

    # Request every millisecond
    usleep(1);
    
    # Request every nanosecond
    #nanosleep(1);
}

$snmp->close();
