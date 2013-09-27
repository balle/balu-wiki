###
AWK
###

Useful variables
================

======== =========================
Variable Description
======== =========================
FS       Field seperator
RS       Records seperator
NR       nr of records
NF       nr of fields
OFS      output field seperator
ORS      output record seperator
======== =========================

Split lines in file on delimiter after matching it to regexp
============================================================

.. code-block:: bash

  cat some_file.txt | awk -F ': ' '/^regexp/ {print $2 " - " $1}'


Match a colum
=============

.. code-block:: bash

  awk '$1 ~ /^regexp/ {print $2}'


Multiple matches
================

.. code-block:: bash

  awk '/regexp1/ {print $1} /regexp2/ {print $2}'


Conditional statements
======================

.. code-block:: bash

  awk '{if($1 == "muh") && ($3 != "maeh") { print $2 } }'


Counter
=======

.. code-block:: bash

  cat some_file | awk 'BEGIN { x=1 } { print x; x += 1 }'

* Or just use the variable `NR` the line counter (counts all lines not only matching ones)


Sum up a column
===============

.. code-block:: bash

  cat some_file.txt| awk '{ sum+=$3} END {print sum}'


String replacement
==================

.. code-block:: bash

  cat some_file.txt | awk 'sub(/regexp/, "replace", $1)'


Defining external variables / Limiting
======================================

.. code-block:: bash

  cat some_file.txt| awk -v LIMIT=30 '{a=$1; sub(/user/, "", a); if(a <= LIMIT){print}}'
