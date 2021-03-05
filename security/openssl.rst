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

  openssl x509 -in <cert_file> -noout -text

* Show expiry date of cert

.. code-block:: bash

   openssl x509 -in <cert_file> -noout -enddate

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

* Check that private key matches certificate (both hashes must match)

.. code-block:: bash

  openssl rsa -noout -modulus -in /etc/pki/tls/private/my-private.key | openssl sha512
  openssl x509 -noout -modulus -in /etc/pki/tls/certs/my-cert.pem | openssl sha512

* Check cert signature with CA cert

.. code-block:: bash

  openssl verify -CAfile ca.pem client.pem
  
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

* View the details of a certificate revocation list (CRL)

.. code-block:: bash

  openssl crl -in filename.crl  -noout -text

* Verify a cert and check crl

.. code-block:: bash

  openssl verify -crl_check -CApath /etc/ssl/certs cert.pem


Build your own CA
==================

.. code-block:: bash

  openssl genrsa -aes256 -out ca.key 4096
  openssl req -x509 -new -key ca.key -days 1825 -out ca-root.crt -sha512

* Create a new key and certificate signing request

.. code-block:: bash

  openssl genrsa -aes256  -out client.key 4096
  openssl req -new -key client.key -out client.csr

* Sign the CSR

.. code-block:: bash

  openssl x509 -req -days 365 -in client.csr -CA ca-root.crt -CAkey ca.key -CAcreateserial -out client.crt
  

Usage of CA.pl
===============

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


More CA stuff
==============

* Create a Certificate Revocation List (CRL)

.. code-block:: bash

  openssl ca -gencrl -keyfile ca_key -cert ca_crt -out my_crl.pem

* Revoke a certificate

.. code-block:: bash

  openssl ca -revoke bad_crt_file -keyfile ca_key -cert ca_crt
  openssl crl -in crl_file -noout -text


Java keystore
==============

* How to convert a PEM cert and RSA key to PKCS12 and import it into a java keystore

.. code-block:: bash

  openssl pkcs12 -export -in mycert.pem -inkey my.key -out mycert.pkcs12
  keytool -importkeystore -deststorepass mypassword -destkeystore keystore.jks -srckeystore mycert.pkcs12 -srcstorepass mypassword

* add -ext san=dns:www.example.com for alternative names


Generate random bytes
=====================

.. code:: bash

  openssl rand <nr_of_bytes>
