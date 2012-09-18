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
* http://munin-monitoring.org/wiki/HowToWriteSNMPPlugins -> Monitoring unusual OIDs is awful 
* Aggregate graphs http://munin-monitoring.org/wiki/aggregate_examples
* Tons of plugins https://github.com/munin-monitoring/contrib/


Collectd
========

* Activate plugins in /etc/collectd.conf
* Restart daemon
* Install collectd-snmp for snmp monitoring


Cluster graphing
================

* http://ganglia.sourceforge.net/
* Install gmond on all nodes
* Install gmetad and php webfrontend on monitor host
