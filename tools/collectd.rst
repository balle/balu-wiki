#########
Collectd
#########

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

* Delete all ~ and other backup files in /etc/collectd.d or you get tons of "Value is too old" error messages
* Graph aggregation http://collectd.org/wiki/index.php/Plugin:Aggregation
* Use Graphite as output plugin

.. code:: bash

  LoadPlugin "write_graphite"
  <Plugin "write_graphite">
   <Carbon>
     Host "127.0.0.1"
     Port "2003"
     Protocol "tcp"
     EscapeCharacter "_"
     SeparateInstances true
     StoreRates false
     AlwaysAppendDS false
   </Carbon>
</Plugin>

