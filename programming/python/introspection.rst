##############
Introspection
##############

* type() returns the class of an object
* hasattr() / getattr() / setattr to query / get / set a property
* issubclass()

.. code-block:: python

  for (n, v) in myobj.__dict__.items(): print "%s: %s" % (n, v)


Import-Hook
===========

.. code-block:: Python

  import __builtin__
  old_import = __builtin__.__import__
  known_imports = []

  def import_hook(name, globals=None, locals=None, fromlist=None):
      if name.startswith("django_chuck") and name not in known_imports:
          if fromlist:
              for symbol in fromlist:
                  print name + "." + symbol
                  known_imports.append(name + "." + symbol)
          else:
              print name
              known_imports.append(name)

      return old_import(name, globals, locals, fromlist)

  __builtin__.__import__ = import_hook


Inrospect imports with compiler
===============================

.. code-block:: Python

  # code borrowed from zope
  class ImportFinder:
      def __init__(self):
          self.imports = []

      def visitFrom(self, statement):
          stmt = statement.asList()
          if stmt[0] == '__future__':
              # we don't care what's imported from the future
              return
          names_dict = {}

          for orig_name, as_name in stmt[1]:
              # we don't care about from import *
              if orig_name == '*':
                  continue

              self.imports.append(stmt[0] + "." + orig_name)

      def visitImport(self, stmt):
          for orig_name, as_name in stmt.names:
              self.imports.append(orig_name)

  ast = compiler.parseFile("django_chuck/commands/create_project.py")
  log = ImportFinder()
  compiler.walk(ast, log)
  print log.imports
