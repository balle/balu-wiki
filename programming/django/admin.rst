######
Admin
######

Prefill an admin field
=======================

* In ModelAdmin do

.. code-block:: python

prepopulated_fields = {"slug": ("title",)}


WYSIWYG-TextField-Editor
========================

* In admin.py

.. code-block:: python

  ModelAdmin:
      class Media:
          js = ('scripts/libs/tinymce/tiny_mce.js',
                'scripts/textareas.js',)

* Copy http://www.tinymce.com/ to static/scripts/lib
* Create static/scripts/textareas.js

.. code-block:: javascript

  tinyMCE.init({
        mode : "textareas",
        theme : "advanced",
    theme_advanced_buttons1 : "bold,italic,underline,separator,undo,redo,link,unlink,anchor,separator,cleanup,help,separator,code",
    theme_advanced_buttons2 : "",
    theme_advanced_buttons3 : ""
  });

* In the template remember to use |safe filter

