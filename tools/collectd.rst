#########
Collectd
#########

General
=======

* Delete all ~ and other backup files in /etc/collectd.d or you get tons of "Value is too old" error messages
* Graph aggregation http://collectd.org/wiki/index.php/Plugin:Aggregation


Check config file
=================

.. code-block:: bash

  collectd -ft


Debugging
=========

* Add this to your config file

.. code-block:: bash

  LoadPlugin logfile
  <Plugin logfile>
    LogLevel debug
      File STDOUT
  </Plugin>

* Start collectd in foreground

.. code-block:: bash

  collectd -f -C /etc/collectd.conf


Example SNMP config
====================

* For single values use ``Table false``

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


Graphite output plugin
=======================

.. code-block:: bash

  LoadPlugin "write_graphite"
  <Plugin "write_graphite">
   <Carbon>
     Host "127.0.0.1"
     Port "2003"
     Protocol "tcp"
     Prefix "collectd."
     EscapeCharacter "_"
     SeparateInstances true
     StoreRates false
     AlwaysAppendDS false
   </Carbon>
  </Plugin>


Mongodb output
==============

.. code-block:: bash

  LoadPlugin write_mongodb
  <Plugin "write_mongodb">
    <Node "default">
        Host "localhost"
        Port     "27017"
        Timeout    2000
        StoreRates true
    </Node>
  </Plugin>


RRD output
============

* For using rrdcached (prefered method)

.. code-block:: bash

  LoadPlugin rrdcached
  <Plugin "rrdcached">
    DaemonAddress "unix:/var/run/rrdcached/rrdcached.sock"
    DataDir "/var/lib/collectd/rrd"
    CreateFiles true
  </Plugin>

* For direct rrd

.. code-block:: bash

  LoadPlugin rrdtool
  <Plugin rrdtool>
     DataDir "/var/lib/collectd/rrd"
     CacheTimeout 120
     CacheFlush   900
     # default 3600, 86400, 604800, 2678400, 31622400
     # RRATimespan <seconds>
  </Plugin>


Example tail file
=================

.. code-block:: bash

  LoadPlugin tail
  <Plugin "tail">
    <File "/var/log/httpd/error_log">
      Instance "httpd_error"
      <Match>
        Regex "python"
        DSType "CounterInc"
        Type "counter"
        Instance "total"
      </Match>
    </File>
  </Plugin>


Example exec plugin
===================

* Source of script (e.g. /usr/bin/count_lines_in_file)

.. code-block:: bash

  #!/bin/bash
  HOSTNAME="${COLLECTD_HOSTNAME:-localhost}"
  INTERVAL="${COLLECTD_INTERVAL:-60}"
  FILE=$1

   while sleep "$INTERVAL"; do
     VALUE=`cat $FILE | wc -l`
     echo "PUTVAL \"$HOSTNAME/"`basename $FILE`"_count/counter\" interval=$INTERVAL N:$VALUE"
   done


* Config for plugin

.. code-block:: bash

  LoadPlugin exec
  <Plugin exec>
    Exec "nobody" "/usr/bin/count_lines_in_file" "/var/log/httpd/error_log"
  </Plugin>
