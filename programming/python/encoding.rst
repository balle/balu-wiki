##############
Encoding hell
##############

* encode() liefert hex z.b. \xb6 für ö
* decode() liefert char von hex
* UTF8 CSV Dateien richtig einlesen

.. code-block::  python

  csv.reader(codecs.EncodedFile(file, "rb"), "utf-8")

