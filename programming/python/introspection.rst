##############
Introspection
##############

* type() gibt die Klasse eines Objekts aus
* dir() zeigt alle Attribute
* hasattr() / getattr() / setattr zum Abfragen / Lesen / Schreiben eines Attributes
* issubclass() 
* dynamische instanz einer klasse

.. code-block:: python 

  classobj = getattr('modulename', 'classname')

* Alle Attribute samt Werte eines Python Objects ausgeben
  
.. code-block:: python 

  for (n, v) in u.__dict__.items(): print "%s: %s" % (n, v)
