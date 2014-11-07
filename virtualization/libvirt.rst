#######
Libvirt
#######

Installation
============

.. code-block:: bash

  yum install libvirt libvirtd python-virtinst qemu-kvm

Set up bridged network for direct access
========================================

* Edit ``/etc//etc/sysconfig/network-scripts/ifcfg-eno1``

.. code-block:: bash

  DEVICE=eno1
  ONBOOT=yes
  BRIDGE=br0
  NM_CONTROLLED=no

* Create ``/etc//etc/sysconfig/network-scripts/ifcfg-br0``

.. code-block:: bash

  DEVICE=br0
  TYPE=Bridge
  BOOTPROTO=dhcp
  ONBOOT=yes
  DELAY=0
  NM_CONTROLLED=no

* Restart network

.. code-block:: bash

  systemctl restart network


Connect to a remote libvirtd via ssh
====================================

.. code-block:: bash

  virsh -c qemu+ssh://username@host/system


Quickinstall
============

* This needs ``libguestfs-tools``

* Build a new disk

.. code-block:: bash

  virt-builder centos-7.0 -o mydisk.img --format qcow2 --size 20G \
		--root-password file:/tmp/rootpw \
		--update \
		--run-command 'rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm' \
		--install cloud-utils,cloud-init

* Install a whole cluster

.. code-block:: bash

  for i in {1..3}; do cp centos7.img node$i.img; virt-install --import --name "Node$i" --os-type=linux --ram=512 --disk path=node$i.img,size=2; done



Create a machine
================

* Configure bridged interface br0
* Create a virtual machine with 20 gb disk and 512 mb ram

* Via ISO file

.. code-block:: bash

  virt-install --name="TestVM" --os-type=linux --ram=512 --disk path=test-vm.img,size=20 --cdrom <path-to-iso-file>

* Using PXE

.. code-block:: bash

  virt-install --name="TestVM" --os-type=linux --os-variant=rhel6 --network bridge=br0,mac=aa:bb:cc:aa:bb:cc --ram=512 --disk path=test-vm.img,size=20 --pxe


Remove a machine
================

.. code-block:: bash

  virsh undefine <machine-name>


List all virtual machines
=========================

.. code-block:: bash

  virsh list

Start or stop a machine
=======================

.. code-block:: bash

  virsh start <machine-name>
  virsh shutdown <machine-name>
  virsh destroy <machine-name>

* To shutdown a machine it must have acpid running


Autostart a machine
===================

.. code-block:: bash

  virsh autostart <machine-name>


Info about a machine
====================

.. code-block:: bash

  virsh dominfo <machine-name>


Info about host system
======================

.. code-block:: bash

  virsh nodeinfo

Connect to a machine
====================

* ``virt-viewer`` or ``virt-manager``


Rename a machine
================

.. code-block:: bash

  virsh dumpxml <machine-name> > muh.xml
  <edit muh.xml, change the name>
  virsh undefine <machine-name>
  virsh define muh.xml


Attach a cdrom image
====================

.. code-block:: bash

  virsh attach-disk <machine-name> <iso-file> hdc --type cdrom --mode readonly

Update boot order
=================

* First dump machine settings as XML

.. code-block:: bash

  virsh dumpxml <machine-name> > blah.xml

* Edit XML file
* Update machine settings

.. code-block:: bash

  virsh define blah.xml


Configure RAM
==============

.. code-block:: bash

  virsh setmem <machine-name> <kbyte>

Configure number of CPUs
========================

.. code-block:: bash

  virsh setvcpus <machine-name> <nr>


Resize disk
===========

* Switch off the machine
* and convert old image to new one and expand sda2 to max size

.. code-block:: bash

  virt-resize --expand /dev/sda2 old-disk.img new-disk.img


Update a machines config
========================

.. code-block:: bash

  virsh edit <machine-name>


Backup
======

* Save a machines RAM state to a file

.. code-block:: bash

  virsh save <machine-name> <file>

* Take a snapshot of disk and ram (must be supported by disk image format e.g. qcow2 and this will PAUSE the machine if ram is backuped! use --disk-only to avoid this)

.. code-block:: bash

  virsh snapshot-create-as <machine-name> <snapshot-name>

* or by using qemu tools (but only when vm is off!)

.. code-block:: bash

  qemu-img snapshot -c my-backup disk.img
  qemu-img snapshot -l disk.img

* Extract snapshot of qcow2 image file

.. code-block:: bash

  qemu-img convert -f qcow2 -s <snapshot> -O qcow2 <image_file> <backup_file>


* Another possibility is to install libguestfs-tools and create a tar archive of /

.. code-block:: bash

  virt-tar -z -x <machine_name> / machine-backup.tgz


Restore
=======

.. code-block:: bash

  virsh snapshot-list <machine_name>
  virsh snapshot-revert <machine_name> <snapshot>


Disk tricks
===========

* Install libguestfs-tools

.. code-block:: bash

  virt-df
  virt-df -d <machine_name>

* Get content of a file

.. code-block:: bash

  virt-cat -d <machine_name> <filename>

* Edit a file (vm must be off)

.. code-block:: bash

  virt-edit -d <machine_name> <filename>

* Or even get a shell on a disk image

.. code-block:: bash

  guestfish \
            add disk.img : run : mount /dev/vg_guest/lv_root / : \
                      write /etc/resolv.conf "nameserver 8.8.8.8"


Convert VirtIO to IDE disk and vice versa
==========================================

* Make sure the machine is powered off

.. code-block:: bash

  virsh edit <machine-name>

* For IDE disk

.. code-block:: bash

   <disk type='file' device='disk'>
      <driver name='qemu' type='raw'/>
      <source file='/whatever.img'/>
      <target dev='hda' bus='ide'/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>

* For VirtIO disk

.. code-block:: bash

    <disk type='file' device='disk'>
      <driver name='qemu' type='raw' cache='writethrough'/>
      <source file='/whatever.img'/>
      <target dev='vda' bus='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
    </disk>

* Afterwards update the systems ``/etc/fstab``

.. code-block:: bash

  virt-edit /path/to/image-file /etc/fstab


Cloning
=======

* Will copy a whole machine and its properties and gives it a new mac address
* The machine must be switched off

.. code-block:: bash

  virt-clone -o <machine-name> -n <new-machine-name>


Migration
=========

* By default, migration only transfers in-memory state of a running domain (memory, CPU state, ...). Disk images are not transferred during migration but they need to be accessible at the same path from both hosts.
* Live migration needs shared network storage via NFS, iSCSI, GFS2 or Fibre Channel

.. code-block:: bash

  virsh migrate --live <machine-name> qemu://example.com/system


Performance overview
=====================

* Use ``virt-top``


Performance tuning
==================

* Use virtio driver for disk and net this will give a machine direct hardware access (no emulation - only for linux guests)
* Maybe you have to load the kernel modules

.. code-block:: bash

  modprobe virtio_blk
  modprobe virtio_net
  modprobe virtio_pci

* If one dont want to use snapshots use `raw` as image type
* Use `Writethrough` as caching type
* Use MacVtab bridge as network device with virtio model
* Use Spice and QXL driver for display


Grant normal user permission to qemu:///system
==============================================

* Create file ``/etc/polkit-1/localauthority/30-site.d/libvirt.pkla``

.. code-block:: bash

  [User update perms]
  Identity=unix-user:basti
  Action=org.libvirt.unix.manage
  ResultAny=no
  ResultInactive=no
  ResultActive=yes


Scripting with Python2
======================

* Just a sample script to shutdown all active instances and boot all that were inactive

.. code-block:: python

  import libvirt

  #conn=libvirt.open("qemu:///system")
  conn = libvirt.open("qemu+ssh://root@127.0.0.1/system")

  print "Active instances"
  active_instances = []

  for id in conn.listDomainsID():
    instance = conn.lookupByID(id)
    instance_name = instance.name()
    active_instances.append(instance_name)
    print "Deactivating ", instance_name
    instance.destroy()

  print "Activating inactive instances"
  inactive_instances = [instance for instance in conn.listDefinedDomains() if instance not in active_instances]

  for instance_name in inactive_instances:
    print "Activating ", instance_name
    instance = dom = conn.lookupByName(instance_name)
    instance.create()

  conn.close()

* A script to create / delete a new instances

.. code-block:: bash

  import sys
  import libvirt

  dom_name = "testme"
  dom_mem = 512
  dom_cpu = 1
  dom_disk = "/data/virtualbox/centos64.img"
  qemu_disk_type = "raw"

  if len(sys.argv) < 2:
    print sys.argv[0], " up/down"
    sys.exit(0)

  conn = libvirt.open("qemu+ssh://root@127.0.0.1/system")

  if sys.argv[1] == "down":
    dom = conn.lookupByName(dom_name)

    if dom:
        dom.undefine()
    else:
        print "Cannot find domain ", dom_name
        conn.close()
        sys.exit(1)
  else:
    xml = """<domain type='kvm'>
      <name>""" + dom_name + """</name>
      <memory unit='KiB'>""" + str(dom_mem * 1024) + """</memory>
      <vcpu placement='static'>""" + str(dom_cpu) + """</vcpu>
      <os>
        <type arch='x86_64' machine='rhel6.4.0'>hvm</type>
        <boot dev='hd'/>
      </os>
      <features>
        <acpi/>
        <apic/>
        <pae/>
      </features>
      <clock offset='utc'/>
      <on_poweroff>destroy</on_poweroff>
      <on_reboot>restart</on_reboot>
      <on_crash>restart</on_crash>
      <devices>
        <emulator>/usr/libexec/qemu-kvm</emulator>
        <disk type='file' device='disk'>
          <driver name='qemu' type='""" + qemu_disk_type + """' cache='none'/>
          <source file='""" + dom_disk + """'/>
          <target dev='hda' bus='ide'/>
          <address type='drive' controller='0' bus='0' target='0' unit='0'/>
        </disk>
        <disk type='block' device='cdrom'>
          <driver name='qemu' type='raw'/>
          <target dev='hdc' bus='ide'/>
          <readonly/>
          <address type='drive' controller='0' bus='1' target='0' unit='0'/>
        </disk>
        <controller type='usb' index='0'>
          <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x2'/>
        </controller>
        <controller type='ide' index='0'>
          <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
        </controller>
        <interface type='bridge'>
          <mac address='52:54:00:f8:56:2a'/>
          <source bridge='br0'/>
          <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
        </interface>
        <serial type='pty'>
          <target port='0'/>
        </serial>
        <console type='pty'>
          <target type='serial' port='0'/>
        </console>
        <input type='mouse' bus='ps2'/>
        <graphics type='spice' port='5900' autoport='yes' listen='127.0.0.1'>
          <listen type='address' address='127.0.0.1'/>
          <clipboard copypaste='no'/>
          <image compression='auto_glz'/>
        </graphics>
        <video>
          <model type='qxl' ram='65536' vram='65536' heads='1'/>
          <alias name='video0'/>
          <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
        </video>
        <memballoon model='virtio'>
          <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
        </memballoon>
      </devices>
    </domain>"""

    #print xml
    conn.createXML(xml, libvirt.VIR_DOMAIN_START_AUTODESTROY)

  conn.close()

* Accessing virtual disks with guestfs

.. code-block:: bash

  import guestfs

  gfs = guestfs.GuestFS()
  gfs.add_drive_opts(dom_disk)
  gfs.launch()
  root_device = None

  for root in gfs.inspect_os():
    for mountpoint in gfs.inspect_get_mountpoints(root):
      if mountpoint[0] == "/":
        root_device = mountpoint[1]
        break

  if root_device:
    gfs.mount(root_device, "/")
    gfs.sh("dhclient eth1 && yum install puppet")
  else:
    print "Cannot find root device :("

  gfs.umount_all()


Failover
========

* http://code.google.com/p/ganeti/


Troubleshooting
===============

* Intel virtualisation support must be activated in bios to use kvm
* Maybe Vbox modules should be unloaded
* Use `virt-rescue` (from libguestfs-tools) as live-rescue system

.. code-block:: bash

  virt-rescue -d <machine_name>
