#######
Apache
#######

Redirct all HTTP to HTTPS
===========================

.. code-block:: bash

  RewriteCond %{HTTPS} off
  RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}

* or

.. code-block:: bash

  <VirtualHost *:80>
    RedirectMatch ^/(.*)$ https://$SERVER_HOST/$1
  </VirtualHost>


New allow all
=============

.. code:: bash

  <Location "/content/">
      AllowOverride All
      Require all granted
  </Location>


Run in foreground
==================

.. code-block:: bash

  LogLevel info
  ErrorLog "|cat"
  LogFormat "%h %l %u %t \"%r\" %>s %b" common
  CustomLog "|cat" common
