###########
OpenPandora
###########

Emulator handbook
=================

* http://dl.openhandhelds.org/pandora//uploads/Home/Pandora%20-%20Emulators/yoshis_pandora_emulator_fact_sheets_v07.pdf


Firmware update
===============

* Install and run http://repo.openpandora.org/?page=detail&app=szupdater1.openpandora.org


Firmware update (old way)
=========================

* http://www.openpandora.org/index.php?option=com_content&view=article&id=199&Itemid=40&lang=en
* hold right shoulder button
* boot from sd-card


Start SSH server
================

.. code:: bash

  /etc/init.d/dropbear start


Deactivate boot splash
======================

* Edit /boot/autoboot.txt and append ``psplash=false`` at the end of the ``setenv bootargs`` parameter
* Or hit ``Alt + D-pad right`` to disable it temporarily

Turn wifi off
=============

* pandora-ctl stop wifi


Handling PND Files
===================

* Run in console with pnd_run
* Mount PND File
* /usr/pandora/scripts/pnd_run.sh -m -p <pnd_file>


Installing software
====================

* opkg install <ipk-file>
* Or use `Milky <http://apps.openpandora.org/cgi-bin/viewapp.pl?/Other/milkyhelper.inf>`_ (pacman for pandora)


Setting up cross-compile environment
=====================================

* Download http://git.openpandora.org/cgi-bin/gitweb.cgi?p=pandora-misc.git;a=blob_plain;f=sdk_installer/openpandora_toolchain.sh;hb=HEAD
* dos2unix openpandora_toolchain.sh
* chmod a+x openpandora_toolchain.sh
* Execute openpandora_toolchain.sh

Cross compile some source
=========================

* Go to the source tree and Execute

.. code-block:: bash

  pandora-dev/sdk_utils/pandora_configure.sh --prefix=/data/muh/
  make
  make install
  pandora-dev/sdk_utils/pnd_make.sh -p zsh.pnd -d /data/muh

* pnd_make.sh must run as root
* Maybe you have to add ``-I$PNDSDK/usr/include`` to CFLAGS in Makefile or pandora_configure.sh


Building PND file
=================

.. code-block:: bash

  pandora-dev/sdk_utils/pnd_make.sh -p some-new-app.pnd -d /dir-to-compress

* Maybe you want to edit PXML.xml to specify exec script

.. code-block:: bash

  <exec command="scripts/install.sh"/>

* To rebuild a mounted pnd on pandora use

.. code-block:: bash

  mksquashfs . /tmp/new.pnd ; cat PXML.xml icon.png >> /tmp/new.pnd


Setting up complete development environment
===========================================

* http://blogs.distant-earth.com/wp/?p=90
