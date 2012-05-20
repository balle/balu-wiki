##################
String Conversion
##################

* Convert char to int

.. code-block:: python

  ord("A")

* Convert char to hex

.. code-block:: python

  hex(ord("A"))

* Convert int to char

.. code-block:: python

  chr(42)

* Convert string to hex

.. code-block:: python

  import binascii
  binascii.hexlify("test")

* Convert hex to string

.. code-block:: python

  binascii.unhexlify("74657374")

* String to unicode html

.. code-block:: python

  "".join(["&#" + str(hex(ord(x))) + ";" for x in "script"])
  python2 -c 'import sys; print "".join(["&#" + str(hex(ord(x))) + ";" for x in sys.argv[1]])' script

* String to url encoding

.. code-block:: python

  python2 -c 'import sys; print "".join(["%" + str(hex(ord(x))).replace("0x","") for x in sys.argv[1]])' "javascipt:alert('BUH');"


