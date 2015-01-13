########
Graphite
########

Setup graphite-web
==================

* After installation append the following to ``/etc/graphite/local_settings.py``

.. code:: bash

  from graphite.app_settings import *

  SECRET_KEY='eiThoo6/biephe7Fs.o7aiZeu=eD8sho!ahQuah2+yiegh9Ai,6euP8hAequa7ee'

* Of course make sure to generate your own secret key
* Adjust apache configuration file ``/etc/httpd/conf.d/graphite-web.conf`` and add 

.. code:: bash
 
   <Location "/">
      AllowOverride All
      Require all granted
  </Location>

* Last but not least add graphite-web as hostname to localhost in ``/etc/hosts`` or whatever ip you like


Send data to graphite
=====================

* Via Collectd
* Using Statsd
* With Icinga
* By help of Diamond
* Or in Bash script

.. code:: bash

  echo "localhost.hello.world `ps ax | wc -l` `date +%s`" | nc <graphite-srv> 2003

* For windows systems use SSC Serv


Carbon config
==============

* `/etc/carbon/carbon.conf` defines limits for caching, flush interval, forwarding and aggregation
* `/etc/carbon/storage-schemas.conf` configures how long the data will be stored, in which frequency and when it gets overwritten (remember its a round-robin like RRD)

.. code:: bash

  [collectd]
  pattern = ^collectd\..*
  rententions = 1s:1d,1m:7d,1h:30d,1d:2y

