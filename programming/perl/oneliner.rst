######################
Useful Perl one liners
######################

Search and replace
==================

* Search in file and replace a with b

.. code-block:: perl

  perl -p -e 's/a/b/g' datei

* Replace and make backup before

.. code-block:: perl

  perl -p -i.old -e 's/a/b/g' datei

* Recursivly replace files

.. code-block:: perl

  find . -type f | xargs perl -p -e 's/a/b/g'


ASCII, Hex and Binary conversion
================================

* ASCII2Hex (urlencoded)

.. code-block:: perl

  perl -e 'map { print "%"; printf("%x",ord($_)); } split(//,$ARGV[0]); print"\n";'

* Hex2ASCII

.. code-block:: perl

  perl -e 'map { print chr(hex($_)); } split(/%/,$ARGV[0]); print "\n";'

* ASCII2Binary

.. code-block:: perl

  perl -e 'map { print "$_ "; printf("%08b",ord($_)); print "\n"; } split(//,$ARGV[0]);'

* Binary2ASCII

.. code-block:: perl

  perl -e 'print chr(ord(pack("B*",$ARGV[0])))."\n";'


Base64
======

* Encoding

.. code-block:: bash

  perl -MMIME::Base64 -e 'print MIME::Base64::encode_base64($ARGV[0]) . "\n"' "BLA BLA BLA"

* Decoding

.. code-block:: bash

  perl -MMIME::Base64 -e 'print MIME::Base64::decode_base64($ARGV[0]) . "\n"' "QkxBIEJMQSBCTEE="


Make /etc/hosts to domain names
===============================

.. code-block:: bash

   perl -n -e 'my @a=split(/\s*\s/,$_); print "$a[1]\tIN\tA\t$a[0]\n";' /etc/hosts >> domain.name.fwd
