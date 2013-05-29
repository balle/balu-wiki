######
Puppet
######

Overview
========

* Firewall port tcp 8140
* Sample puppet.conf

.. code-block:: bash

  [main]
    vardir = /var/lib/puppet
    logdir = /var/log/puppet
    rundir = /var/run/puppet
    ssldir = $vardir/ssl

  [agent]
    classfile = $vardir/classes.txt
    localconfig = $vardir/localconfig
    listen = True
    runinterval = 3600

  [master]
    manifestdir = /etc/puppet/manifests
    modulepath = /etc/puppet/modules
    autoflush = true
    autosign = true
    

* ``manifests/site.pp`` tells puppet what client configurations to load

.. code-block:: bash

  import 'nodes.pp'
  # import 'nodes/*'
  $puppetserver = "name-of.master.net"
  
* ``manifest/notes.pp`` include the client configuration

.. code-block:: bash

  node base {
     include module1, module2
  }

  node 'full.hostname.tld' inherits base {
    include another_module
  }


Modules
=======

* Create dirs

.. code-block:: bash

  mkdir -p /etc/puppet/modules/$modulename/{files,templates,manifests}

* Create ``manifests/init.pp``

.. code-block:: bash

  class emacs {
    package { emacs:
      ensure => present
    }
  }


Install software
================

.. code-block:: bash

  package { 'emacs': ensure => present }

  
Copy files
==========

.. code-block:: bash

  file { "/root/.emacs":
    owner => "root",
    group => "root",
    mode => 0440,
    source => "puppet://$puppetserver/modules/emacs/.emacs"
    requrie => Package["emacs"]
  }

* File must be on master server in ``/etc/puppet/modules/emacs/files/.emacs``


Adding users
============

.. code-block:: bash

  user { "testuser":
    ensure => present,
    uid => 10001,
    gid => 10001,
    shell => "/bin/zsh",
    home => "/home/testuser",
    comment => "Just a test",
    password => "secret",
    managehome => true,
  }
  

Starting services
=================

.. code-block:: bash

  class ssh::service {
    service { "sshd":
      ensure => running,
      hasstatus => true,
      hasrestart => true,
      enable => true,
    }
  }

* hasstatus and hasrestart tells puppet if the init script understand the parameter status and restart
* A file can trigger a service restart by adding ``notify => Class["ssh::service"]``


Templates
=========

* Templates are used to create files depending on facter and config variables

.. code-block:: bash

  myhostname = <%= hostname %>

  <% if a_flag == 1 -%>
    config_a = 123
  <% elsif a_flag == 2 -%>
    config_b = 321
  <% else -%>
    do something totally different
  <% end -%>
  
* Can be included in files using ``content = template("template_file.erb")``


Config controls
===============

.. code-block:: bash

  if $host == '' {
    $srvname = $title
  } else {
    $srvname = $servername
  }
  case $operatingsystem {
    'centos', 'redhat', 'fedora': { $vdir   = '/etc/httpd/conf.d'
                                    $logdir = '/var/log/httpd'}
    'ubuntu', 'debian':           { $vdir   = '/etc/apache2/sites-enabled'
                                    $logdir = '/var/log/apache2'}
    default:                      { $vdir   = '/etc/apache2/sites-enabled'
                                    $logdir = '/var/log/apache2'}
  }        

  
Defined resource types
======================

* Defines are code-templates

.. code-block:: bash

  # /etc/puppetlabs/puppet/modules/apache/manifests/vhost.pp
  define apache::vhost ($port, $docroot, $servername = $title, $vhost_name = '*') {
    include apache # contains Package['httpd'] and Service['httpd']
    include apache::params # contains common config settings
    $vhost_dir = $apache::params::vhost_dir
    file { "${vhost_dir}/${servername}.conf":
      content => template('apache/vhost-default.conf.erb'),
      # This template can access all of the parameters and variables from above.
      owner   => 'www',
      group   => 'www',
      mode    => '644',
      require => Package['httpd'],
      notify  => Service['httpd'],
    }
  }

* To use it

.. code-block:: bash

  apache::vhost {'homepages':
    port    => 8081,
    docroot => '/var/www-testhost',
  }

  
Cert handling
=============

* List

.. code-block:: bash

  puppet cert --list

* Sign

.. code-block:: bash

  puppet cert --sign <hostname>
  puppet cert --sign --all
  
* Delete

.. code-block:: bash

  puppet cert clean <hostname>


Debugging
=========

* Master

.. code-block:: bash

  puppet agent --no-daemonize --verbose

* Agent

.. code-block:: bash

  puppet agent --no-daemonize --verbose --test --noop

* You can use the ``notice("foo")`` command somewhere to send a log message
