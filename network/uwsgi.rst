#####
UWSGI
#####

uwsgi.xml 
==========

.. code-block:: bash

  <uwsgi>
    <!-- <socket>127.0.0.1:5050</socket> -->
    <socket>/var/run/uwsgi/balle.sock</socket>
    <chown-socket>www-data</chown-socket>
    <uid>www-data</uid>
    <gid>www-data</gid>
    <master/>
    <!-- <daemonize>/var/log/uwsgi/balle.log</daemonize> -->
    <max-requests>5000</max-requests>

    <!-- max seconds an app will after its being killed -->
    <harakiri>120</harakiri>

    <!-- restart the server after x seconds of inactivity -->
    <inactivity>300</inactivity>

    <!-- name of wsgi app file -->
    <module>django_wsgi</module>

    <!-- reload server after touching that file -->
    <touch-reload>/srv/http/balle/uwsgi/django_wsgi.py</touch-reload>

    <!-- setup python environment -->
    <autoload/>
    <plugins>python</plugins>
    <pythonpath>/srv/http/balle/</pythonpath>
    <pythonpath>/srv/http/balle/uwsgi</pythonpath>
    <pythonpath>/srv/virtualenvs/balle/lib/python2.7/site-packages</pythonpath>

    <!-- use virtualenv -->
    <pyhome>/srv/virtualenvs/balle/</pyhome>


    <!-- Number of processes. Set this to number of cpus not cores -->
    <processes>1</processes>

    <!-- number of threads. Set this to the total number of cores -->
    <enable-threads/>
    <threads>4</threads>
  </uwsgi>


django_wsgi.py 
===============

.. code-block:: python

  import os
  import django.core.handlers.wsgi
  
  os.environ['DJANGO_SETTINGS_MODULE'] = 'balle.settings'
  application = django.core.handlers.wsgi.WSGIHandler()


start uWSGI process 
====================

.. code-block:: bash

  uwsgi -x uwsgi.xml
