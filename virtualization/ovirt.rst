#####
Ovirt
#####

Setup controller node
=====================

* Leave all default settings except password and ISO domain (5 after password)

.. code-block:: bash

  yum localinstall -y http://resources.ovirt.org/pub/yum-repo/ovirt-release35.rpm
  yum install ovirt-engine-reports-setup ovirt-engine-dwh-setup ovirt-engine
  engine-setup

* Click on Cluster -> Edit and Check "Enable Gluster Service"
* Choose cpu architecture x86_64
* Click on Storage -> New Domain and add an NFS path


Setup hypervisor node
=====================

.. code-block:: bash

  yum localinstall -y http://resources.ovirt.org/pub/yum-repo/ovirt-release35.rpm

* Login to Ovirt Engine Web frontend as admin user
* Open Cluster tab and click on Default -> Hosts -> New
* Fill out General form
* Click in the right lower corner of the arrows to see event logs


Import an ISO image
===================

.. code-block:: bash

  engine-iso-uploader -r <ovirt-server> -i iiScratch_iso upload <ISO_FILENAME>
