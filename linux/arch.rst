###########
Arch Linux
###########

Install yaourt 
==============

* Edit /etc/pacman.conf

.. code-block:: bash

  [archlinuxfr]
  Server = http://repo.archlinux.fr/$arch

* Install yaourt
  
.. code-block:: bash

  pacman -Sy yaourt

* Now you can install packages from aur.archlinux.org with

.. code-block:: bash

  yaourt -S <pkg>
