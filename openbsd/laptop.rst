#######
Laptop
#######

Enable Power Management
=======================

* Edit /etc/rc.conf.local and add

  apmd_flags=


Enable CPU frequency adjustment
===============================

* Edit /etc/rc.conf.local and add

  apmd_flags=-A

  
Do not suspend on lid close
===========================

.. code-block:: bash

  sysctl machdep.lidaction=0
