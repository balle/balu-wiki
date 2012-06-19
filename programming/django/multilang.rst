##########
Multilang
##########

Convert PO-Files to CSV
=======================

* http://translate.sourceforge.net/wiki/toolkit/using_csv2po

.. code-block:: bash

  po2csv -i locale/en/LC_MESSAGES/django.po -o translations.csv
  iconv -f UTF-8 -t WINDOWS-1252 translations.csv > translations_new.csv

Make Messages without Django-Cms etc
====================================

.. code-block:: bash

  django-admin.py makemessages -l de -e html,txt -i *cms/* -i *menus/* -i *cmsplugin_filer_file/* -i *cmsplugin_filer_folder/* -i *cmsplugin_filer_image/* -i *cmsplugin_filer_video/* -i *easy_thumbnails/* -i *filer/* -i *mptt/*

* django-modeltranslation
* PO-File Admin Editor https://github.com/mbi/django-rosetta
