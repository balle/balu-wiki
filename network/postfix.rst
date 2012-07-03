#######
Postfix
#######

Masquerade Domain
==================

.. code-block:: bash

  masquerade_domains = foo.example.com


Rewrite an email address
========================

* /etc/postfix/main.cf

.. code-block:: bash

  relocated_maps = hash:/etc/postfix/relocated

* /etc/postfix/relocated

.. code-block:: bash

  username@example.com      otheruser@elsewhere.tld


Delete all mails in queue
==========================

.. code-block:: bash

  for i in `mailq|grep '@' |awk {'print $1'}|grep -v '@'`; do postsuper -d $i ; done
