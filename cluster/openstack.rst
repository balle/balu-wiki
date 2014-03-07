##########
Openstack
##########

Overview
========

* Tenant is something like an organization or mandant (can have multiple users) --> In new versions called project

================ ================ ========================================================================
Subsystem        Ports            Description
---------------- ---------------- ------------------------------------------------------------------------
Keystone         5000, 35357      Identity service (manages user, roles, tenants, services and endpoints) Port 5000 for auth, 35357 for service registry
Glance           9191, 9292       Image service (manages kvm, qemu, vmware, amazon s3 etc images)
Nova                              Compute service (manage startup / life of virtual machines using libvirt)
Nova Scheduler   59229            Decide where to create a new instance
Nova API         8773, 8774, 8775 Access Nova functionality
Nova Network                      Configure network if Neutron is not in use
Nova Compute                      Management controller for virtual machines
Nova Conductor                    Encapsulate database api for nova
Nova ObjectStore 3333             File-based Storage system (can be replaced by Swift or Ceph)
Nova Cert                         Nova CA service for x509 certificates
Nova Console                      VNC access support
Nova Consoleauth                  VNC authorization
Cinder           8776             Volumne service (manages additional storage and replication via LVM / iSCSI / Ceph)
Neutron                           Network configuration service - install network client on each vm
Swift                             Distributed File Storage Service (can be used to store images for Glance)
Ceph                              Ceph is a distributed storage system (object store, block store and POSIX-compliant distributed file system)
Horizon          80               Admin webfrontend in Django
================ ================ ========================================================================

* How an instances is started http://ilearnstack.wordpress.com/2013/04/26/request-flow-for-provisioning-instance-in-openstack/?preview=true&preview_id=410&preview_nonce=3618fe51b7
/D

Installation
============

* Out-of-the-box http://openstack.redhat.com/Quickstart

.. code-block:: bash

  packstack --allinone

  # multi node setup with nova network
  packstack --install-hosts=node1,node2,node3 --os-neutron-install=n

  # iterative changes (edit answerfile in home dir)
  packstack --answer-file=<answerfile>

* Manually http://docs.openstack.org/install/
* By using puppet https://wiki.openstack.org/wiki/Puppet-openstack


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

* The privileges of a role are defined in ``/etc/keystone/policy.json``


Adding images
=============

* List

.. code-block:: bash

  glance image-list

* Create

.. code-block:: bash

  glance image-create --name="arch linux" --is-public true --disk-format raw --container-format bare --file "arch_linux.img"


Flavors
=======

* List

.. code-block:: bash

  nova flavor-list

* Create

.. code-block:: bash

  nova flavor-create &lt;name&gt; &lt;id&gt; &lt;ram&gt; &lt;disk&gt; &lt;vcpus&gt;


Configure networking
====================

* FlatManager only connects vms to bridge device `no ip configuration!`
* FlatDHCPManager configure network ip on bridge and starts dnsmasq dhcp server on that ip
* VlanManager creates separate VLANs for each tenant
* http://www.mirantis.com/blog/openstack-networking-flatmanager-and-flatdhcpmanager/

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
  STP=off

* Bring up bridge interface

.. code-block:: bash

  brctl addbr br100

* Configure network in `/etc/nova/nova.conf`
* flat__network_bridge - bridge interface
* flat_interface - where bridge ends up
* public_interface - used for natting floating (public) ips to private ips

.. code-block:: bash

  network_manager=nova.network.manager.FlatDHCPManager
  fixed_range=192.168.100.0/24
  public_interface=eth0
  flat_interface=eth0
  flat_network_bridge=br100

* Check network settings

.. code-block:: bash

  nova-manage network list

* Setup floating ip range

.. code-block:: bash

  nova-manage floating create --pool=nova --ip_range=10.10.100.0/24

* To automatically assign floating ip add the following to nova.conf

.. code-block:: bash

  auto_assign_floating_ip=True

* For manually assigning a floating ip to a vm

.. code-block:: bash

  nova floating-ip-create
  nova add-floating-ip <machine_id> <ip_address>


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


VNC access
===========

* First install requirements `novnc` and `openstack-nova-novncproxy`
* Edit /etc/nova/nova.conf

.. code-block:: bash

  novnc_enabled=true
  vnc_keymap="de-de"

* Make sure `nova-consoleauth` is running

.. code-block:: bash

  nova-manage service list

* ``vncserver_proxyclient_address`` must contain the official ip of the compute node

* Get an access url to throw in your browser

.. code-block:: bash

  nova get-vnc-console <machine_id> novnc


Adding additional storage
=========================

* Cinder uses LVM2 + ISCI
* Can only attach a block device to one vm
* Activate Cinder in /etc/nova/nova.conf (restart nova-api and cinder-api afterwards)

.. code-block:: bash

  volume_api_class=nova.volume.cinder.API
  enable_apis=ec2,osapi_compute,metadata

* Create and attach a new columne

.. code-block:: bash

  cinder create --display_name test 1
  cinder list
  nova volume-list
  nova volume-attach <device_id> <volume_id> auto


Quotas
======

* A value of -1 means unlimited
* Show all quotas of a tenant / project

.. code-block:: bash

  nova quota-show --tenant <tenant>

   * To configure default quota for all tenants edit ``/etc/nova/nova.conf`` and set the desired quota like

.. code-block:: bash

  quota_instances=100

   * To update the quota of just one tenant execute

.. code-block:: bash

  nova quota-update <tenant-id> --instances 100


Automatically backup instances
==============================

* You can choose weekly instead of daily

.. code-block:: bash

  nova backup <device_id> <backup_name> daily <keep_x_copies>


Live migration
==============

* Setup as described in http://docs.openstack.org/grizzly/openstack-compute/admin/content/configuring-migrations.html
* Migrate a vm to another hypervisor

.. code-block:: bash

  nova live-migration <machine_id> <new_hypervisor>


Where to find which service?
============================

.. code-block:: bash

  nova host-list
  nova hypervisor-list


Where to find which instance?
=============================

* Get hypervisor of an instance

.. code-block:: bash

  nova show <machine_id> | grep OS-EXT-SRV-ATTR:host


* List all instances of a hypervisor

.. code-block:: bash

  nova hypervisor-servers <host>


Statistics
==========

.. code-block:: bash

  nova hypervisor-stats


Updating to a new version
=========================

* Every service has a db sync command 

.. code-block:: bash

  keystone-manage -vvv db_sync


Logging & Debugging
====================

* Get an overall overview about the status of openstack

.. code-block:: bash

  openstack-status

* Every manage command like `nova-manage` or `cinder-manager` has a parameter `logs errors`

* You can add the following lines to all `[DEFAULT]` config sections of all subsystems like nova or keystone etc

.. code-block:: bash

  verbose=True
  debug=True

* Every command has a `--debug` parameter

.. code-block:: bash

  nova --debug list

* Configure logging e.g. open /etc/nova/nova.conf and add the following line in `[DEFAULT]` secion

.. code-block:: bash

  log-config=/etc/nova/logging.conf

* Now create /etc/nova/logging.conf with the following content (syntax is `python logging <http://docs.python.org/3/library/logging.html>`)

.. code-block:: bash

  [logger_nova]
  level = DEBUG
  handlers = stderr
  qualname = nova

* Got a `Malformed request url (HTTP 400)` -> Check keystone (user / service / endpoint configuration) and service config for `auth_strategy=keystone`

.. code-block:: bash

  keystone service-list
  kestone endpoint-list

* Got a `ERROR n/a (HTTP 401)` -> thats an auth failure check service and api config for same as above + tenant / user / password


Compute node crashed
=====================

* If the did not crash completely but openstack-nova-compute service is broken, the machine will still be running and you can ssh into them but not use vnc
* If you decide to nevertheless migrate all vms first halt them otherwise the disk images will get crushed 

.. code-block:: bash

  ssh <HOSTNAME_OF_CRASHED_NODE>
  for VM in $(virsh list --uuid); do virsh shutdown $VM; done
  sleep 10
  for VM in $(virsh list --uuid); do virsh destroy $VM; done

* Connect to the master node and execute the following (dont forget to replace the two variables!) 

.. code-block:: bash

  echo "select uuid from instances where host = 'HOSTNAME_OF_CRASHED_NODE' and deleted = 0;" | mysql --skip-column-names nova > broken_vms
  echo "update instances set host = 'HOSTNAME_OF_NEW_NODE' where host = 'HOSTNAME_OF_CRASHED_NODE' and deleted = 0;" | mysql nova
  for VM in $(cat broken_vms); do nova reboot $VM; done

* The following command should return no results 

.. code-block:: bash

  nova list --host <HOSTNAME_OF_CRASHED_NODE>


Troubleshooting Keystone
========================

* SSL error SSL_CTX_use_Privatekey_file:system lib -> Check permission of /etc/keystone/ssl (maybe chown keystone)
* User / services etc doesnt appear in the database -> edit /etc/keystone/keystone.conf section `[catalog]`

.. code-block:: bash

  driver = keystone.catalog.backends.sql.Catalog

* Unable to communicate with identity service "Invalid tenant" "Not authorized" -> check that the os-username and -tenant you use have a corresponding admin role

.. code-block:: bash

  keystone user-role-add --role-id <id_of_admin_role> --user-id <userid> --tenant-id <tenantid>

* Select role in db

.. code-block:: bash

  select m.data from user u join user_project_metadata m on u.id=m.user_id join project p on p.id=m.project_id where u.name="nova";
  select * from role where id="a4b2afdf62baifgafaifga7f";

* Check ``token_format`` in keystone.conf should be ``UUID`` by default

* `` 'Client' object has no attribute 'auth_tenant_id'``

.. code-block:: bash

  export SERVICE_TOKEN=
  export SERVICE_ENDPOINT=

* Manually receive an auth token by executing ``keystone token-get`` or 

.. code-block:: bash

  curl -i 'http://127.0.0.1:5000/v2.0/tokens' -X POST -H "Content-Type: application/json" -H "Accept: application/json"  -d '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "devstack"}}}'


Troubleshooting Glance
======================

* Invalid OpenStack identity credentials -> Comment out `flavor=keystone`


Troubleshooting Cinder
======================

* Check the LVM volumne group

.. code-block:: bash

  vgdisplay cinder-volumes

* Check that tgtd is running

* HTTP 401 Permission denied? -> Edit /etc/cinder/api-paste.ini section `[filter:authtoken]`

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


Troubleshooting Instances
=========================

* Check nova logs for errors

.. code-block:: bash

  nova-manage logs errors

* Get information about the instance

.. code-block:: bash

  nova show <device_id>
  nova diagnostics <device_id>

* Instance in an broken task state?

.. code-block:: bash

  nova reset-state <device_id>
  nova reset-state --active <device_id>

* Qemu disk image is broken?

.. code-block:: bash

  qemu-img check check <disk_file>


Troubleshooting Nova
====================

* Read `Nova disaster recovery process <http://docs.openstack.org/trunk/openstack-compute/admin/content/nova-disaster-recovery-process.html>`

* ``Instance instance-XXXXXXXX already exists`` --> the instance is running check with ``virsh list --all``

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

  [nova.service]
  osapi_compute_listen_port=8774


Troubleshooting Horizon
=======================

* Disable SeLinux `setenfore 0`
* Permission denied -> Check httpd.conf, add the following to Directory directive

.. code-block:: bash

  Require all granted

* Command node not found -> Install http://www.nodejs.org


Programming
===========

* Overview about Openstack APIs http://www.ibm.com/developerworks/cloud/library/cl-openstack-pythonapis/index.html
* Keystone

.. code-block:: bash

  import keystoneclient.v2_0.client as ksclient
  conn = ksclient.Client(auth_url="http://127.0.0.1:35357/v2.0", username="nova", password="nova", tenant_name="services")
  print conn.auth_token

* Nova

.. code-block:: bash

  import sys
  import time
  import novaclient.v1_1.client as nvclient

  username = "admin"
  password = "admin"
  tenant = "admin"
  auth_url = "http://127.0.0.1:5000/v2.0/"

  def get_hypervisor_for_host(hostname):
    try:
      hypervisor = nova.hypervisors.search(hostname, servers=True)[0]
    except Exception:
      hypervisor = None

    return hypervisor

  nova = nvclient.Client(username, password, tenant, auth_url)
  hypervisor = get_hypervisor_for_host(sys.argv[1])

  if not hypervisor:
    print "Hypervisor " + sys.argv[1] + " cannot be found"
    sys.exit(1)

  if hasattr(hypervisor, "servers"):
    waiting_for_migrations = True

    for vm_dict in hypervisor.servers:
      vm = nova.servers.get(vm_dict.get('uuid'))
      print "Migrating " + vm.name
      vm.live_migrate()

    # wait for migration to complete
    sys.stdout.write("\nWaiting for migrations to finish ...")

    while waiting_for_migrations:
      sys.stdout.write(".")
      hypervisor = get_hypervisor_for_host(sys.argv[1])

      if not hypervisor or not hasattr(hypervisor, "servers"):
        waiting_for_migrations = False
        sys.stdout.write("\n")
      else:
        time.sleep(1)
  else:
    print "Hypervisor " + sys.argv[1] + " serves no vms"
