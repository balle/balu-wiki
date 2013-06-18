######
Augeas
######

Overview
========

* Edit configuration files on the command line


Printing
========

* All known config files an values

.. code-block:: bash

  augtool print

* One value of a config file

.. code-block:: bash

  augtool print /files/etc/ssh/sshd_config/MaxSessions


Add / change a value
====================

.. code-block:: bash

  augtool -s set /files/etc/ssh/sshd_config/MaxSessions

* To change the third title in grub.conf

.. code-block:: bash

  augtool -s set /files/etc/grub.conf/title[3] "Arch Linux"


Remove an entry
===============

.. code-block:: bash

  augtool -s rm /files/etc/ssh/sshd_config/MaxSessions

