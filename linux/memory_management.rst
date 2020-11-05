#################
Memory Management
#################

What is the Linux Page Cache 
=============================

* http://www.linux-tutorial.info/modules.php?name=MContent&pageid=310

Page cache and swap config 
===========================

* http://www.westnet.com/~gsmith/content/linux-pdflush.htm

Large page support 
===================

* http://linuxgazette.net/155/krishnakumar.html

choosing an i/o scheduler 
==========================

* http://www.redhat.com/magazine/008jun05/features/schedulers/

Misc 
=====

* openbook: understanding the linux virtual memory manager
http://www.kernel.org/doc/gorman/html/understand/

* die anzeige bei cached steht für den disk cache


Page cache 
===========

* To free pagecache:

.. code-block:: bash

  echo 1 > /proc/sys/vm/drop_caches

* To free dentries and inodes:

.. code-block:: bash

  echo 2 > /proc/sys/vm/drop_caches

* To free pagecache, dentries and inodes:

.. code-block:: bash

  echo 3 > /proc/sys/vm/drop_caches

Configs 
========

* /proc/sys/vm/dirty_writeback_centisecs 500 - 5 sekunden wann der disk cache aufgeräumt wird
* /proc/sys/vm/dirty_expire_centiseconds 3000 - 30 sekunden wann die page auf dirty gesetzt wird
* /proc/sys/vm/dirty_ratio - maximal % für disk cache
* dirty_background_ratio - % von ram ab wann pdflush aufräumt
* vfs_cache_pressure - wenn 0 gibt nach möglichkeit keinen vfs cache frei wenn 100 oder mehr gib lieber vfs cache frei


Memory dump for forensics
=========================

* Microsoft AVML (Acquire Volatile Memory for Linux)
* Linux Memory Extractor LiME https://github.com/504ensicsLabs/LiME
