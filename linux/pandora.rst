###########
OpenPandora
###########

Firmware update 
================

* http://www.openpandora.org/index.php?option=com_content&view=article&id=199&Itemid=40&lang=en
* hold right shoulder button
* boot from sd-card


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
* Maybe you have to add ``-I$PNDSDK/usr/include`` to CFLAGS in Makefile


Setting up complete development environment
===========================================

* http://blogs.distant-earth.com/wp/?p=90
