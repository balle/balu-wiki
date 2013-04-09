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


Configure networking
====================

* Setup bridge interface (install bridge-utils)

.. code-block:: bash

  ip link set eth0 promisc on

* Create `/etc/sysconfig/network-scripts/ifcfg-br100`

.. code-block:: bash

  DEVICE=br100
  TYPE=Bridge
  ONBOOT=yes
  DELAY=0
  BOOTPROTO=static
  IPADDR=192.168.100.1
  NETMASK=255.255.255.0

* Bring up bridge interface

.. code-block:: bash

  brctl addbr br100

* Congigure network in `/etc/nova/nova.conf`

.. code-block:: bash

  network_manager=nova.network.manager.FlatDHCPManager
  fixed_range=192.168.100.0/24
  public_interface=eth0
  flat_interface=eth0
  flat_network_bridge=br100

* Check network settings

.. code-block:: bash

  nova-manage network list

Managing security groups
========================

* Security groups define access rules for virtual machines

.. code-block:: bash

  nova secgroup-list
  nova secgroup-create mygroup "test group"
  nova secgroup-add-rule mygroup tcp <from-port> <to-port> 0.0.0.0/0
  nova secgroup-list-rules mygroup
  

Injecting SSH keys
==================

.. code-block:: bash

  nova keypair-list
  nova keypair-add --pub_key ~/.ssh/id_dsa.pub a_name


Handling instances
==================

* Instances can be found in `/var/lib/nova/instances`

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

* Connect to machines display

.. code-block:: bash

  nova get-vnc-console <machine_id> novnc


Adding additional storage
=========================

* Cinder uses LVM2 + ISCI
* Can only attach a block device to one vm

.. code-block:: bash

  cinder create --display_name test 1
  cinder list
  nova volume-list
  nova volume-attach <device_id> <volume_id> auto
  <


Configure logging  
=================

* E.g. open /etc/nova/nova.conf and add the following line

.. code-block:: bash

  log-config=/etc/nova/logging.conf

* Now create /etc/nova/logging.conf with the following content

.. code-block:: bash

  [logger_nova]
  level = DEBUG
  handlers = stderr
  qualname = nova
  

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

* HTTP 400 Permission denied? -> Edit /etc/cinder/api-paste.ini section `[filter:authtoken]`

.. code-block:: bash

  admin_tenant_name=service
  admin_user=cinder
  admin_password=cinder

* Cannot connect to AMQP server -> Edit /etc/cinder/cinder.conf

.. code-block:: bash

  rpc_backend = cinder.rpc.impl_kombu
  
* Check nova is using cinder (edit /etc/nova/nova.conf)

.. code-block:: bash

  volume_api_class=nova.volume.cinder.API
  

Troubleshooting Nova
====================

* Use `virsh` / `virt-manager` or `virt-viewer` for debugging purpose
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

* `libvirt unable to read from monitor`  -> check vnc settings in `/etc/nova/nova.conf`
* nova list returns `[Errno 111] Connection refused` -> Check that nova-compute is running, maybe configure its port in /etc/nova/nova.conf

.. code-block:: bash

  osapi_compute_listen_port=8774
  

Troubleshooting Horizon
=======================

* Disable SeLinux `setenfore 0`
* Permission denied -> Check httpd.conf, add the following to Directory directive

.. code-block:: bash

  Require all granted

* Command node not found -> Install http://www.nodejs.org
