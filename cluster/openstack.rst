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

  # alternativly generate an answer file and edit it
  packstack --gen-answer-file /root/answers.txt

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


Create images
=============

* Install your system with libvirt
* Install cloud-init
* Take the disk image
* For more information http://docs.openstack.org/image-guide/content/centos-image.html


Adding images
=============

* List

.. code-block:: bash

  glance image-list

* Create

.. code-block:: bash

  glance image-create --name="arch linux" --is-public true --disk-format raw --container-format bare --file "arch_linux.img"

* Share an Image with another tenant (--can-share defines it can be reshared)

.. code-block:: bash

  glance member-create --can-share <image> <tenant>

* Download an image (e.g. for testing purpose)

.. code-block:: bash

  glance image-download <image>


Flavors
=======

* List

.. code-block:: bash

  nova flavor-list

* Create

.. code-block:: bash

  nova flavor-create &lt;name&gt; &lt;id&gt; &lt;ram&gt; &lt;disk&gt; &lt;vcpus&gt;


Host Aggregates
===============

* Group hypervisors and assign metadata to it to combine it with a flavor so you can start e.g. some vms on monster machines and some on slow ones
* Create a new group

.. code-block:: bash

  nova aggregate-create <name>
  nova aggregate-add-host <group_name> <hypervisor>
  nova aggregate-list
  nova aggregate-details <group_name>

* Assign metadata to group

.. code-block:: bash

  nova aggregate-add-metadata <group_name> key=value (e.g. highspec=1)

* Assign metadata to flavor

.. code-block:: bash

  nova flavor-key <flavor> set highspec=true

* To isolate tenants in a certain host aggregation use ``AggregateMultiTenancyIsolation`` as ``scheduler_default_filters`` in ``/etc/nova/nova.conf`` and set metadata ``filter_tenant_id=<tenant_id>`` to your aggregation

.. code-block:: bash

  nova aggregate-add-metadata <group_name> filter_tenant_id=<tenant_id>


Cells (untested)
================

* Seperate compute nodes into independent groups with its own db, amqp, network and scheduler servers which share single services like nova-api, keystone, glance, cinder, ceilometer and heat
* Useful to avoid clustering amqp and db servers if load gets to high on very large deployments
* Activated in ``/etc/nova/nova.conf`` in section ``[cells]``

.. code-block:: bash

  [cells]
  enable = true
  name = MyCellName


Configure networking (old style nova networking)
================================================

* FlatManager only connects vms to bridge device `no ip configuration!`
* FlatDHCPManager configure network ip on bridge and starts dnsmasq dhcp server on that ip
* VlanManager creates separate VLANs for each tenant
* http://www.mirantis.com/blog/openstack-networking-flatmanager-and-flatdhcpmanager/
* Configure network in `/etc/nova/nova.conf`
* flat_network_bridge - bridge interface
* flat_interface - where bridge ends up
* public_interface - used for natting floating (public) ips to private (fixed) ips

.. code-block:: bash

  network_manager=nova.network.manager.FlatDHCPManager
  fixed_range=192.168.100.0/24
  public_interface=eth0
  flat_interface=eth0
  flat_network_bridge=br100

* Check network settings

.. code-block:: bash

  nova-manage network list

* Setup floating ip range manually

.. code-block:: bash

  nova-manage floating create --pool=nova --ip_range=10.10.100.0/24

* To automatically assign floating ip add the following to nova.conf

.. code-block:: bash

  auto_assign_floating_ip=True

* For manually assigning a floating ip to a vm

.. code-block:: bash

  nova floating-ip-create
  nova add-floating-ip <machine_id> <ip_address>


Configure Neutron
=================

* Most of the time based on Open vSwitch (http://openvswitch.org/)
* Uses network namespaces and gre tunnel or vlan to seperate tenants (projects)
* You need an interface for host and one for neutron
* Flat network is like nova network flat dhcp network (doesnt seperate tenants)

* Create a new network and subnet

.. code-block:: bash

  neutron net-create <name>
  neutron subnet-create --name bastiSubnet --no-gateway --host-route destination=0.0.0.0/0,nexthop=10.10.1.1 --dns-nameserver 8.8.8.8 <net_uuid> 10.10.1.0/24

* List existing networks

.. code-block:: bash

  neutron net-list

* Get ips / mac of vms

.. code-block:: bash

  neutron port-list

* Routing between two nets

.. code-block:: bash

  neutron router-create <name>
  neutron router-interface-add <router_name> <net_name_1>
  neutron router-interface-add <router_name> <net_name_2>
  neutron router-list

* Delete an interface from a router

.. code-block:: bash

  neutron router-interface-delete <router_name> <net_name>


* Create a floating net

.. code-block:: bash

  neutron net-create --router:external=True floatingNet
  neutron subnet-create --name floatingNet --allocation-pool start=192.168.1.2,end=192.168.1.100 --enable_dhcp=False floatingNet 192.168.1.0/24
  neutron router-gateway-set <router_name> floatingNet

* Find agent hosting a network

.. code-block:: bash

  neutron dhcp-agent-list-hosting-net <net_name>

* Find network namespace of a vm

.. code-block:: bash

  nova show <vm_id> # get tenant id
  neutron net-list --tenant-id <tenant_id>
  neutron dhcp-agent-list-hosting-net <net_name> # find host where net is served
  ip netns exec <net_id> # on serving host

* Find fixed ips for tenant

.. code-block:: bash

  neutron port-list -f csv -c fixed_ips --tenant_id <tenant_id> | grep subnet | cut -d ' ' -f 4 | sed 's/["}]//g'

* Firewall rule handling

.. code-block:: bash

  neutron security-group-list
  neutron security-group-create --protocol ICMP --direction ingress <group_id>
  neutron security-group-rule-list

* Quota (independent from nova network quotas!)

.. code-block:: bash

  neutron quota-update --network 0 --router 0 --floatingip 5 --tenant-id <tenant_id>
  neutron quota-list

* Complete example

.. code-block:: bash

  neutron net-create external --router:external=True
  neutron subnet-create --disable-dhcp external 10.10.10.0/24
  neutron net-create net0
  neutron subnet-create --name net0-subnet0 --dns-nameserver 8.8.8.8 net0 192.168.100.0/24
  neutron router-create extrouter
  neutron router-gateway-set extrouter external
  neutron router-interface-add extrouter net0-subnet0
  neutron security-group-rule-create --protocol icmp default
  neutron security-group-rule-create --protocol tcp --port-range-min 22 --port-range-max 22 default
  ip netns exec qdhcp-<subnet_uuid> ssh <user>@<machine_ip>
  ip a add 10.10.10.1/24 dev br-ex
  iptables -t nat -A POSTROUTING -s 10.10.10.0/24 -j MASQUERADE


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
  nova boot --poll --flavor <flavor_id> --image <image_id> --key_name <key_name> --security_group mygroup <machine_name>
  nova list --all-tenants

* Logfile `/var/log/nova/compute.log`
* Get console output

.. code-block:: bash

  nova console-log <machine_id>

* Remove a machine

.. code-block:: bash

  nova delete <machine_id>

* If it cannot be removed use

.. code-block:: bash

  nova force-delete <machine_id>

* Start / stop / suspend existing machine

.. code-block:: bash

  nova [start|stop|suspend] <machine_id>

* Show details about a machine

.. code-block:: bash

  nova show <machine_id>

* Connect to machines display

.. code-block:: bash

  nova get-vnc-console <machine_id> novnc

* Show all vms and where they are running

.. code-block:: bash

  nova-manage vm list

* Connect to a neutron network

.. code-block:: bash

  nova boot --nic net-id=<subnet_id>

* Execute a script after creation (image needs to support cloud init and nova metadata must be running)

.. code-block:: bash

  nova boot --user-data ./myscript.sh --flavor ...

* In user-data scripts cloud-config can be used to configure the machine in yaml or by invoking puppet (see http://docs.openstack.org/user-guide/content/user-data.html)


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

* Cinder uses LVM2 (or Ceph, NetApp, ...) + ISCSI
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

* Create a snapshot

.. code-block:: bash

  nova volume-detach <machine_id> <volumne_id>
  cinder snapshot-create --display-name <name> <volumne_id>

* Restore a snapshot

.. code-block:: bash

  cinder snapshot-list
  cinder create <size> --snapshot-id <snapshot_uuid> --display-name <name>

* Boot from image in cinder

.. code-block:: bash

  cinder create <size> --display-name <name> --image-id <glance_image_id>
  nova boot --block-device-mapping vda=<volume_id> --flavor ...

* Resize a volumne offline

.. code-block:: bash

  cinder extend <volumne_id> <new_size>

* QoS

.. code-block:: bash

  cinder qos-create standard-iops consumer="front-end" read_iops_sec=400 write_iops_sec=200
  cinder qos-associate <qos_id> <volumne_id>


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


Ceilometer
==========

* Collects data for statistics, alarmings ("monitoring as a service") or interaction with Heat
* Compute agent polls libvirt, central agent polls Openstack infrastructure, collector collects data in ampq or database, alarm evaluator decides if an alarm should take place, alarm notifier sends the alarm
* QuickStart guide http://openstack.redhat.com/CeilometerQuickStart
* List all what can be monitored

.. code-block:: bash

  ceilometer meter-list

* List collected data

.. code-block:: bash

  ceilometer sample-list --meter cpu


Heat
====

* http://docs.openstack.org/developer/heat/template_guide/hot_guide.html
* http://docs.openstack.org/developer/heat/template_guide/openstack.html
* Examples can be found on https://github.com/openstack/heat-templates/tree/master
* Execute a heat template with parameters from console

.. code-block:: bash

  heat stack-create mystack --template-file=<filename> --parameters="Param1=value;Param2=value"

* Example script

.. code-block:: bash

  heat_template_version: 2013-05-23

  description: Create a network and an instance attached to it

  parameters:
    public_net_id:
      type: string
      description: >
        ID of floating network

  resources:
    private_net:
      type: OS::Neutron::Net
      properties:
        name: Privatenet

    private_subnet:
      type: OS::Neutron::Subnet
      properties:
        network_id: { get_resource: private_net }
        cidr: 192.168.1.0/24
        gateway_ip: 192.168.1.1
        allocation_pools:
          - start: 192.168.1.2
            end: 192.168.1.254

    router:
      type: OS::Neutron::Router

    router_gateway:
      type: OS::Neutron::RouterGateway
      properties:
        router_id: { get_resource: router }
        network_id: { get_param: public_net_id }

    router_interface:
      type: OS::Neutron::RouterInterface
      properties:
        router_id: { get_resource: router }
        subnet_id: { get_resource: private_subnet }

    server1:
      type: OS::Nova::Server
      properties:
        name: Server1
        image: Test Image
        flavor: m1.small
        networks:
          - port: { get_resource: server1_port }

    server1_port:
      type: OS::Neutron::Port
      properties:
        network_id: { get_resource: private_net }
        fixed_ips:
          - subnet_id: { get_resource: private_subnet }



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

* Maybe you can use `nova evacuate <server> <vm>` instead of plain sql
* Connect to the master node and execute the following (dont forget to replace the two variables!)

.. code-block:: bash

  echo "select uuid from instances where host = 'HOSTNAME_OF_CRASHED_NODE' and deleted = 0;" | mysql --skip-column-names nova > broken_vms
  echo "update instances set host = 'HOSTNAME_OF_NEW_NODE' where host = 'HOSTNAME_OF_CRASHED_NODE' and deleted = 0;" | mysql nova
  for VM in $(cat broken_vms); do nova reboot $VM; done

* The following command should return no results

.. code-block:: bash

  nova list --host <HOSTNAME_OF_CRASHED_NODE>


Disable a service on a host
===========================

* For example disable a compute node

.. code-block:: bash

  nova-manage service disable <host> nova-compute


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

  curl -i 'http://127.0.0.1:5000/v2.0/tokens' -X POST -H "Content-Type: application/json" -H "Accept: application/json"  -d '{"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": "admin"}}}'


Troubleshooting Neutron
=======================

* What is for what? l2-agent (DHCP), l3-agent (floating ips and routers)
* Check the neutron metadata agent is running and accessible (lives on 169.254.0.0/16)

.. code-block:: bash

  nova console-log <machine_id>

* Status overview

.. code-block:: bash

  neutron agent-list

* Make sure the short hostname is not on loopback ip in ``/etc/hosts``
* Check br-int and br-ext exist and br-tun for gre tunnel setup

.. code-block:: bash

  ovs-vsctl show

* Check ``/var/log/neutron`` logs and that iproute tool support netns
* Get a shell in the network namespace

.. code-block:: bash

  ip netns list
  ip netns exec <namespace> bash

* ``Timeout while waiting on RPC response - topic: "network"`` -> check neutron config in ``/etc/nova/nova.conf`` on your compute nodes
* ``Error: Local ip for ovs agent must be set when tunneling is enabled`` -> network device is not up / configured or name used is not in dns / /etc/hosts


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


Cool addons
===========

* http://zerovm.org
