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
