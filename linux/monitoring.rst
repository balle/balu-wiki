###########
Monitoring
###########

Cacti
=====

* Create new host: Console -> Create devices -> Add (right top corner)
* Add host to graph tree: Graph Trees -> Add -> Tree Item Type Host
* Reconfiguring data sources doesnt seem to work. Better delete and recreate.
* Cumulative graphs: Install Aggregate Plugin than Graph Management -> Select graphs -> Action Create Aggregate Graph


Munin
=====

* http://munin-monitoring.org/wiki/Using_SNMP_plugins
* http://munin-monitoring.org/wiki/HowToWriteSNMPPlugins
* value (and only value!) must be returned after config section

.. code-block:: perl

  #!/usr/bin/perl -w

  =head1 MAGIC MARKERS

    #%# family=snmpauto
    #%# capabilities=snmpconf

  =cut

  use strict;
  use Munin::Plugin::SNMP;

  my $oid = "1.3.6.1.4.1.34097.9.77.1.1.17.1";

  if (defined $ARGV[0] and $ARGV[0] eq "snmpconf") {
        print "require $oid.0 [0-9]\n"; # Number
        exit 0;
  }

  if (defined $ARGV[0] and $ARGV[0] eq "config") {
    my ($host) = Munin::Plugin::SNMP->config_session();
        print "host_name $host\n" unless $host eq 'localhost';
        print "graph_title Power A Total
  graph_vlabel A
  graph_category power
  graph_info Power in A
  ";

     print "power_total_a.label Total\n";
     print "power_total_a.info Total\n";
     print "power_total_a.draw LINE2\n";
   
     exit 0;
  }

  my $session = Munin::Plugin::SNMP->session();

  my $power_a = $session->get_single ("." . $oid . ".0") || 'U';

  if($power_a ne "U")
  {
      $power_a /= 1000;
  }

  print "power_total_a.value ", $power_a, "\n";

* Aggregate graphs http://munin-monitoring.org/wiki/aggregate_examples
* Tons of plugins https://github.com/munin-monitoring/contrib/


Collectd
========

* Activate plugins in /etc/collectd.conf
* Restart daemon
* Install collectd-snmp for snmp monitoring
* Example SNMP config (for single values use ``Table false``)

.. code-block:: bash

  <Plugin snmp>
    <Data "a_value">
          Type "gauge"
          Table true
          Values ".1.3.6.1.4.1.34097.9.80.1.1.6.1"
     </Data>
     <Host "some-host.domain.tld">
           Address "1.2.3.4"
           Version 1
           Community "public"
           Collect "a_value"
           Interval 5
     </Host>
  </Plugin>

* Graph aggregation http://collectd.org/wiki/index.php/Plugin:Aggregation


Cluster graphing
================

* http://ganglia.sourceforge.net/
* Install gmond on all nodes
* Install gmetad and php webfrontend on monitor host
