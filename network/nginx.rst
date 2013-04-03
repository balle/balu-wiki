#####
Nginx
#####


Check config
=============

.. code-block:: bash

  nginx -t


Gzip compression
================

.. code-block:: bash

  gzip  on;
  gzip_comp_level 3;
  gzip_proxied any;
  # what mimetypes to gzip? otherwise only html gets zipped
  gzip_types      text/plain text/css application/x-javascript text/xml application/xml application/xml+rss text/javascript image/png image/gif image/jpeg image/x-icon image/bmp;
  gzip_disable "MSIE [1-6]\.";
  gzip_min_length 1400; # in bytes
  gzip_vary  on;        # allow the client to cache it

* If nginx is requested a foo.jpg and finds a foo.jpg.gz it will send that file instead of zipping foo.jpg


Keep-alive
===========

.. code-block:: bash

  # let several request be made in one connection
  # hold connection open for max x seconds
  keepalive_timeout 60;


Htaccess
=========

.. code-block:: bash

  auth_basic            "You shall not pass!";
  auth_basic_user_file   /etc/nginx/htpasswd;


SSL config
==========

.. code-block:: bash

  ssl on;
  ssl_certificate /etc/nginx/mycert.pem;
  ssl_certificate_key /etc/nginx/mycert.pem;

  # avoid BEAST attack
  ssl_ciphers RC4:HIGH:!aNULL:!MD5;
  ssl_prefer_server_ciphers on;

  # cache ssl sessions
  ssl_session_cache    shared:SSL:10m;
  ssl_session_timeout  10m;


Redirect
=========

.. code-block:: bash

  location / {
     return       301 https://www.ccc.de$request_uri;
  }


Rewrite
========

.. code-block:: bash

  location /old_stuff/ {
     rewrite   ^/old_stuff/(.*)$  /new_stuff/$1  permanent;
  }


Security tricks
===============

* Dont serve version control files, sql / json dumps

.. code-block:: bash

  location ~ (\.git)|(CVS)|(\.svn)|(\.hg)|(\.ht)|(sql)|(dump)|(json) {
     access_log /var/log/nginx/security.log;
     return 404;
  }

* Dont serve password files

.. code-block:: bash

  location ~ (\.ht)|(pass) {
     access_log /var/log/nginx/security.log;
     return 404;
  }

* Dont serve backup files

.. code-block:: bash

  location ~ (\.old$)|(~$)|(^#)|(\.bak$)|(\.orig$)|(Kopievon)|(tmp) {
     access_log /var/log/nginx/security.log;
     return 404;
  }

* Dont serve logs and docs

.. code-block:: bash

  location ~ /(doc)|(log)|(documentation) {
     access_log /var/log/nginx/security.log;
     return 404;
  }

* Dont serve dot files and dirs

.. code-block:: bash

  location ~ /\. {
     access_log /var/log/nginx/security.log;
     return 404;
  }

* Hide server version number

.. code-block:: bash

  http {
     server_tokens off;
  }

* Web Application Firewall: http://code.google.com/p/naxsi/


Load-Balancing
===============

.. code-block:: bash

  upstream myservers {
    server 192.168.1.1;
    server 192.168.1.2;
  }

 server {
    location / {
      proxy_pass http://myservers;
    }
  }


Traffic shaping
================

.. code-block:: bash

    limit_rate_after 1g;
    limit_rate       50k;


Debugging
==========

.. code-block:: bash

  # [ debug | info | notice | warn | error | crit ]
  error_log  /var/log/nginx.error_log  debug


uWSGI Virtualhost for serving Django
=====================================

.. code-block:: bash

    server {
        listen  80;
	server_name .balle.de;
        root /srv/http/balle/balle;
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        location /static {
            alias /srv/http/balle/static;
            gzip on;
            expires 30m;
        }

        location /media {
            gzip on;
            expires 24h;  # otherwise i client wont cache
        }

        location / {
            #uwsgi_pass 127.0.0.1:5050;
            uwsgi_pass unix:///var/run/uwsgi/balle.sock;
            include uwsgi.params;
        }
    }


uwsgi.params
=============

.. code-block:: bash

  uwsgi_param  QUERY_STRING       $query_string;
  uwsgi_param  REQUEST_METHOD     $request_method;
  uwsgi_param  CONTENT_TYPE       $content_type;
  uwsgi_param  CONTENT_LENGTH     $content_length;

  uwsgi_param  REQUEST_URI        $request_uri;
  uwsgi_param  PATH_INFO          $document_uri;
  uwsgi_param  DOCUMENT_ROOT      $document_root;
  uwsgi_param  SERVER_PROTOCOL    $server_protocol;

  uwsgi_param  REMOTE_ADDR        $remote_addr;
  uwsgi_param  REMOTE_PORT        $remote_port;
  uwsgi_param  SERVER_PORT        $server_port;
  uwsgi_param  SERVER_NAME        $server_name;


Gunicorn as WSGI server
=======================

* pip install gunicorn
* gunicorn -w 4 -D --bind unix:/tmp/gunicorn.sock myproject:app

.. code-block:: bash

  server {
    location / {
      #proxy_pass http://localhost:8000;
      proxy_pass unix:/tmp/gunicorn.sock;
    }
  }
  
  
PHP
====

* Install php-fpm and start server
* Add the following to your server directive

.. code-block:: bash

  location ~ \.php$ {
     include fastcgi.conf;
     fastcgi_intercept_errors on;
     fastcgi_pass    unix:///var/run/php-fpm/php-fpm.sock;
  }


