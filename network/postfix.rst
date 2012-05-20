#######
Postfix
#######

Masquerade Domain 
==================

.. code-block:: bash

  masquerade_domains = foo.example.com


=== Delete all mails in queue ===

.. code-block:: bash

  for i in `mailq|grep '@' |awk {'print $1'}|grep -v '@'`; do postsuper -d $i ; done
