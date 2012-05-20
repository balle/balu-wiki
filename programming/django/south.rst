######
South
######

copy one field to another
=========================

* django-admin.py datamigration app migration_name
*. edit migration

.. code-block:: python

    def forwards(self, orm):
        "Write your forwards methods here."
        for mod in Model.objects.all():
            mod.field_new = mod_field_old
            med.save()


    def backwards(self, orm):
        "Write your backwards methods here."
        raise RuntimeError("Cannot reverse this migration.")


