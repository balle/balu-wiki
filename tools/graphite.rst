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
* Or in Bash script

.. code:: bash

  echo "localhost.hello.world `ps ax | wc -l` `date +%s`" | nc <graphite-srv> 2003
