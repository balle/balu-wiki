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
* Cinder - Volumne service (manages storage and replication)
* Horizon - Admin webfrontend in Django


Installation
============

* Out-of-the-box http://www.devstack.org
* Manually http://docs.openstack.org/install/


Configfile to source
====================

.. code-block:: bash

  export OS_USERNAME=admin
  export OS_PASSWORD=<whatever>
  export OS_TENANT_NAME=<whatever>
  export OS_AUTH_URL=http://127.0.0.1:35357/v2.0

  
User management
===============

* Either source configfile above or use `--token <your_secret> --endpoint http://127.0.0.1:35357/v2.0/`
* List

.. code-block:: bash

  keystone tenant-list
  keystone user-list

* Create

.. code-block:: bash

  keystone user-create --name USERNAME --pass PASSWORD
  keystone user-role-add --user-id <user_id> --role-id <role_id> --tenant-id <tenant_id>


Adding images
=============

* List

.. code-block:: bash

  glance image-list

* Create

.. code-block:: bash

  glance image-create --name="arch linux" --is-public true --disk-format raw --container-format bare --file "arch_linux.img"


Managing security groups
========================

* Security groups define access rules for virtual machines

.. code-block:: bash

  nova secgroup-list
  nova secgroup-create mygroup "test group"
  nova secgroup-add-rule mygroup tcp <from-port> <to-port> 0.0.0.0/0


Injecting SSH keys
==================

.. code-block:: bash

  nova keypair-list
  nova keypair-add --pub_key ~/.ssh/id_dsa.pub a_name


Handling instances
==================

* Create a new machine

.. code-block:: bash

  nova flavor-list
  nova image-list
  nova boot --flavor <flavor_id> --image <image_id> --key_name <key_name> --security_group mygroup <machine_name>
  nova list

* Logfile `/var/log/nova/compute.log`
* Get console output

.. code-block:: bash

  nova console-log <machine_id>

* Remove a machine

.. code-block:: bash

  nova delete <machine_id>

* Start / stop / suspend existing machine

.. code-block:: bash

  nova [start|stop|suspend] <machine_id>

* Show details about a machine

.. code-block:: bash

  nova show <machine_id>
  

Troubleshooting Keystone
========================

* SSL error SSL_CTX_use_Privatekey_file:system lib -> Check permission of /etc/keystone/ssl (maybe chown keystone)
* User / services etc doesnt appear in the database -> edit /etc/keystone/keystone.conf section `[catalog]`

.. code-block:: bash

  driver = keystone.catalog.backends.sql.Catalog

* Unable to communicate with identity service "Invalid tenant" "Not authorized" -> check that the os-username and -tenant you use have a corresponding admin role

.. code-block:: bash

  keystone user-role-add --role-id <id_of_admin_role> --user-id <userid> --tenant-id <tenantid>
  

Troubleshooting Glance
======================

* Invalid OpenStack identity credentials -> Comment out `flavor=keystone`


Troubleshooting Cinder
======================

* Check the LVM volumne group

.. code-block:: bash

  vgdisplay cinder-volumes
  

Troubleshooting Nova
====================

* Check nova services (ensure ntp is running on all nova nodes)

.. code-block:: bash

  nova-manage service list

* Restart all nova services

.. code-block:: bash

  for svc in api objectstore compute network volume scheduler cert; do service openstack-nova-$svc restart ; done

* Check cpu properties / kernel

.. code-block:: bash

  egrep '(vmx|svm)' /proc/cpuinfo
  lsmod | grep kvm


* libvirtError: internal error no supported architecture for os type 'hvm'

.. code-block:: bash

  modprobe kvm

* xxx in server list / Unable to connect to amqp server -> check that rabbitmq or qpid server is running

* RabbitMQ config in `/etc/nova/nova.conf`

.. code-block:: bash

  rpc_backend = nova.rpc.impl_kombu
  rabbit_host=127.0.0.1

* Unable to connect to AMQP server client: 0-10 -> rpc_backend in nova.conf doesnt match used server

* AMQP server is unreachable: Socket closed -> Check credentials if socket is reachable

.. code-block:: bash

  rabbitmqctl list_users
  rabbitmqctl change_password guest guest

* or configure user / pass for rabbitmq access in `/etc/nova/nova.conf`

.. code-block:: bash

  rabbit_userid=guest
  rabbit_password=guest

* nova image-list returns `HTTP 401` -> thats auth failed check `/etc/nova/api-paste.ini` section `[filter:authtoken]` for

.. code-block:: bash

  admin_tenant_name=service
  admin_user=nova
  admin_password=nova

* All nova commands return `Malformed request url (HTTP 400)` -> check that openstack-nova-compute is running
* compute manager `nova [-] list index out of range` -> you're doomed with the nova-compute cannot restart because you have machine in ERROR state bug. only way is to manually delete the machine from the database nova (table instances and all constraints)

  
Troubleshooting Horizon
=======================

* Disable SeLinux `setenfore 0`
* Permission denied -> Check httpd.conf, add the following to Directory directive

.. code-block:: bash

  Require all granted

* Command node not found -> Install http://www.nodejs.org
