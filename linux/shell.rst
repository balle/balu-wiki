################
Shell Scripting
################

Quote Spaces in Filenames
==========================

.. code-block:: bash

  echo $FILE | sed 's/ /\\ /g'


Get yesterdays date
===================

.. code-block:: bash

  date +%Y:%m:%d -d "1 day ago"


Now in unix time
================

.. code-block:: bash

  date +%s -d "now"

Get lines where the nth element is bigger than x
=================================================

.. code-block:: bash

  perl -n -e '@a=split(/\s/,$_); print $_ if $a[3] > 2;'
