#######
OpenSSL
#######

Basic stuff 
============

* Check a certificate

.. code-block:: bash

  openssl x509 -in <cert_file> -noout

* Show a certificates properties

.. code-block:: bash

  openssl -in <cert_file> -text

* Generate a certificate request (CSR)

.. code-block:: bash

  openssl req -new -newkey rsa:1024 -nodes -keyout key.pem -out cert.pem

* Generate CSR with existing key

.. code-block:: bash

  openssl req -new -key key.pem -out cert.pem

* Generate a self signed cert

.. code-block:: bash

  openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

* Check a private key

.. code-block:: bash

  openssl rsa -in <key_file> -check

* Remove password from a private key

.. code-block:: bash

  openssl rsa -in <key_file> -out <key_file>

* Test an SSL port

.. code-block:: bash

  openssl s_client -connect localhost:443 -state -debug
  GET / HTTP/1.0

* Convert PFX (IIS) to PEM

.. code-block:: bash

  openssl pkcs12 -in mycert.pfx -out mycert.pem


CA stuff 
=========

* Build your own CA

.. code-block:: bash

  /usr/lib/ssl/misc/CA.pl -newca

  on Arch Linux /etc/ssl/misc/CA.pl

* Create a new certificate

.. code-block:: bash

  /usr/lib/ssl/misc/CA.pl -newcert

* Sign a certificate

.. code-block:: bash

  /usr/lib/ssl/misc/CA.pl -sign

* Create a Certificate Revocation List (CRL)

.. code-block:: bash

  openssl ca -gencrl -keyfile ca_key -cert ca_crt -out my_crl.pem

* Revoke a certificate

.. code-block:: bash

  openssl ca -revoke bad_crt_file -keyfile ca_key -cert ca_crt
  openssl crl -in crl_file -noout -text 