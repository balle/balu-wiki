##########
Web stuff
##########

Share dir with simple webserver
===============================

.. code-block:: bash

  python -m SimpleHTTPServer 8080

Grep in url
===========

.. code-block:: bash

  python -c "import sys,urllib2; print filter(lambda line: sys.argv[2] in line, urllib2.urlopen(sys.argv[1]).readlines())" http://www.codekid.net "Network Hacks"


Web Crawling
============

* `Scapy <http://scrapy.org>`_


Hello world in WSGI
===================

.. code-block:: python

  from wsgiref.simple_server import make_server

  def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!']

  make_server('localhost', 8000, hello_world).serve_forever()
