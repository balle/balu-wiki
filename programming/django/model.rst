##########
Modelling
##########

Automatic created and modified timestamps
==========================================

.. code-block:: python

  from django_extensions.db.models import TimeStampedModel
  class MyModel(TimeStampedModel)

Tree-based models
=================

* https://github.com/django-mptt/django-mptt
* get ancestors / get_descendants

.. code-block:: python

  mptt_model.get_ancestors()
  mptt_model.get_descendants()

Get UML for models
==================

.. code-block:: bash

  django-admin.py graph_models app -o app.png

Introspection
=============

* Get all attributes

.. code-block:: python

  User._meta.fields()

* Check attribute type

.. code-block:: python

  isinstance(field, models.ForeignKey)

* Where is the foreign key pointing to?

.. code-block:: python

  field.rel.to

* More on http://www.b-list.org/weblog/2007/nov/04/working-models/

* Filter dynamically

.. code-block:: python

  search_column = "name_" + lang
  search_value = self.kwargs.get("category")
  Category.objects.filter(**{ search_column: search_value })
