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
