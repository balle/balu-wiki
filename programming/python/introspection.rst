##############
Introspection
##############

* type() returns the class of an object
* dir() shows all available properties
* hasattr() / getattr() / setattr to query / get / set a property
* issubclass()
* dynamically create a new class

.. code-block:: python

  classobj = type("MyClass", (object,), {})
* Show all attributes and their values of an Python object

.. code-block:: python

  for (n, v) in myobj.__dict__.items(): print "%s: %s" % (n, v)
