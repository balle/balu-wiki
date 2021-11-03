################
Metaprogramming
################

Metaclasses
===========

* `Metaclasses demystified <http://cleverdevil.org/computing/78/>`_


Get all attributes of a datatype
================================

code-block:: python

  dir(var)

Dynamically create a new class
==============================

.. code-block:: python

  classobj = type("MyClass", (object,), {})

* Show all attributes and their values of an Python object


Respond to every method call
============================

.. code-block:: python

  import functools

  class Bla:
    def __getattr__(self, name):
      def handleattr(attrname, args):
          print "Hi I am attribute ", attrname, " with arguments ", args
      return functools.partial(handleattr, name)
