#######
 Apache
#######

 Redirct all HTTP to HTTPS
===========================

.. code-block:: bash

  RewriteCond %{HTTPS} off
  RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}

