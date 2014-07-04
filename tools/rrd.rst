###
RRD
###

Overview
========

* RRDs (Round Robin Databases) consist of DS (Data Source) that will be saved in RRAs (Round Robin Archives)
* Each RRA has a fixed size of slots, that will be automatically rotated
* Every update on a rrd triggers every RRA to be updated by a consolidation function (CF) like MIN, MAX or AVERAGE


Create a rrd
============

* DS defines Data Source with name load, type GAUGE (just save the value as is), every 60 seconds we expect a value between 0 and unlimited
* The first RRA has 60 slots and saves a single value in it if it greater than 0.1
* The second RRA has 4 slots and saves the MAX value of the last 15 values

.. code-block:: bash

  rrdtool create some.rrd DS:load:GAUGE:60:0:U RRA:AVERAGE:0.1:1:60 RRA:MAX:0.1:15:4


Show meta data about a rrd
==========================

.. code-block:: bash

  rrdtool info some.rrd


Insert values
=============

.. code-block:: bash

  rrdtool update some.rrd `date +%s`:`cat /proc/loadavg| cut -d " " -f 1`


Display values
==============

* from yesterday till now

.. code-block:: bash

  rrdtool fetch some.rrd AVERAGE --start `date +%s -d "yesterday"` --end `date +%s`

* from specific timespan

.. code-block:: bash

  rrdtool fetch some.rrd MAX --start `date +%s -d "2013-02-15 18:00:00"` --end `date +%s -d "2013-02-15 19:00:00"`


Create a graph image
====================

 * The graph will be drawn as LINE with a width of 2 pixel and the color red

.. code-block:: bash

  rrdtool graph test.png  --start `date +%s -d "yesterday"` --end `date +%s` DEF:myload=some.rrd:load:AVERAGE LINE2:myload#FF0000


Calculating stuff
=================

* Graph values multiplied by 10
* Add the following to your graph command

.. code-block:: bash

  CDEF:myvalue=myload,10,\*

* To really graph the ne myvalue add

.. code-block:: bash

  LINE2:myvalue#0000ff


Aggregate two graphs
====================

* First define two DEFs
* Add both by using a CDEF

.. code-block:: bash

  rrdtool graph test.png --start `date +%s -d "yesterday"` --end `date +%s` DEF:load1=some.rrd:load:AVERAGE DEF:load2=another.rrd:load:AVERAGE CDEF:total=load1,load2,\+ LINE2:total#0000ff


Export data as XML
==================

* Everything

.. code-block:: bash

  rrdtool dump some.rrd

* Or specific

.. code-block:: bash

  rrdtool xport --start `date +%s -d "yesterday"` --end `date +%s` DEF:load1=some.rrd:load:AVERAGE XPORT:load1


Resize Databases
==================

.. code-block:: bash

  for DIR in $(ls); do echo "Entering $DIR"; cd $DIR/snmp; for RRD in $(find . |grep rrd|grep -v resize); do echo "Resizing $RRD"; rrdtool resize $RRD 12 GROW 10800; mv -f resize.rrd $RRD; rrdtool resize $RRD 13 GROW 10800; mv -f resize.rrd $RRD; rrdtool resize $RRD 14 GROW 10800; mv -f resize.rrd $RRD; done; cd ../..; done
