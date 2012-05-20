######
Nagios
######

Define a service check for all hosts of a group except one 
===========================================================

.. code-block:: bash

  define service{
        service_description     CPU Stats
        servicegroups   sysres
        use             generic
        hostgroup_name  linux
        host_name       !server1
        check_command   check_iostat
  }


Auto create a host and services configs by scanning ports with nmap 
====================================================================

* `Get Nmap2Nagios <http://sourceforge.net/projects/nmap2nagios/>`_

.. code-block:: bash

  nmap -sS -O -oX nmap.xml myserver.mydomain.com
  nmap2nagios.pl -v -r nmap.xml -o new.cfg
  

Define OS of a host 
====================

.. code-block:: bash

  define hostextinfo{
      host_name       server1
      icon_image      debian.png
      icon_image_alt  Debian
      vrml_image      debian.png
      statusmap_image debian.gd2
  }


Check config for errors 
========================

.. code-block:: bash

  nagios -v /etc/nagios/nagios.cfg
