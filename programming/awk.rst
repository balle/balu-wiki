###
AWK
###

Split lines in file on delimiter after matching it to regexp
============================================================

.. code-block:: bash

  cat some_file.txt | awk -F ': ' '/^regexp/ {print $2 " - " $1}'


Match a colum
=============

.. code-block:: bash

  awk '$1 ~ /^regexp/ {print $2}'


Conditional statements
======================

.. code-block:: bash

  awk '{if($1 == "muh") && ($3 != "maeh") { print $2 } }'


Counter
=======

.. code-block:: bash

  cat some_file | awk 'BEGIN { x=1 } { print x; x += 1 }'
