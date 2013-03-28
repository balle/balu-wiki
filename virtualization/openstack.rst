##########
Openstack
##########

Overview
========

* Keystone - Identity service (manages user, roles and tenants)
* Tenant is something like an organization or mandant (can have multiple users)
* Glance - Image service (manages kvm, qemu, vmware, amazon s3 etc images)
* Nova - Compute service (manage startup / life of virtual machines using libvirt)
* Quantum - Network configuration service
* Swift - Object store (manages storage and replication)
* Horizon - Admin webfrontend in Django


Installation
============

* Out-of-the-box http://www.devstack.org
* Manually http://docs.openstack.org/install/


Troubleshooting Keystone
========================

* SSL error SSL_CTX_use_Privatekey_file:system lib -> Check permission of /etc/keystone/ssl (maybe chown keystone)
* Unable to authorize user -> edit /etc/keystone/keystone.conf section `[catalog]`

.. code-block:: bash

  driver = keystone.catalog.backends.templated.TemplatedCatalog
  template_file = /etc/keystone/default_catalog.templates
  

Troubleshooting Horizon
=======================

* Disable SeLinux `setenfore 0`
* Permission denied -> Check httpd.conf, add the following to Directory directive

.. code-block:: bash

  Require all granted

* Command node not found -> Install http://www.nodejs.org
