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


Classes
=======

* Group some code blocks like package, file and service

.. code-block:: bash

  class a_name($param = "default value") {}


Definitions
===========

* Definitions are like functions
* Useful because classes are singletons (can be only instanciated once)

.. code-block:: bash

  define cronjob( $hour = '00', $minute = '00' ) {
    cron { "$name":
      command => "/opt/cronjobs/$name",
      hour    => $hour,
      minute  => $minute,
    }
  }

  cronjob { 'blah':
    hour => 23,
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

* Search for existing modules on puppetlabs

.. code-block:: bash

  puppet module search <term>

* Install / uninstall a module

.. code-block:: bash

  puppet module install puppetlabs-openstack
  puppet module uninstall puppetlabs-openstack
  

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
    require => Package["emacs"]
  }

* File must be on master server in ``/etc/puppet/modules/emacs/files/.emacs``


Change a file
==============

.. code-block:: bash

  file_line {
    'a comment':
      path => '/path/to/a/file',
      match => '^#?some content',
      line => 'New content';
  }

* Or using augeas
  
.. code-block:: bash

  augeas { "nova.conf":
    context => "/files/etc/nova/nova.conf",
    changes => [
                  "set rpc_backend nova.rpc.impl_kombu",
                ],
  }



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
    password => "$hash",
    managehome => true,
  }

* To generate the password hash use

.. code-block:: bash

  openssl passwd
  

SSH keys
========

.. code-block:: bash

  ssh_authorized_key { "testuser":
    ensure => present,
    type => "ssh-rsa",
    key => "",
    user => "testuser",
    require => User["testuser"],
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
* To stop a service use ``ensure => stopped,``


Cronjobs
========

.. code-block:: bash

  cron { 'Make Backup':
    command => 'tar cvzf /data/backup,tgz /home',
    hour    => '00',
    minutes => '00',
  }


Selective Execution
===================

.. code-block:: bash

  exec { 'apache restart':
    command => 'apachectl restart',
    unless  => 'ps ax | grep apache',
  }

* with ``cwd`` one can change working directory
* ``path`` will set PATH env var
* or exec on file change

.. code-block:: bash

  exec { 'myscript':
    command => 'whatever',
    refreshonly => true,
    subscribe => File['/path/to/some_file'],
  }


Deleting stuff
==============

.. code-block:: bash

  ensure => absent,
  

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


Firewall config
===============

* First install firewall module

.. code-block::

  puppet module install puppetlabs-firewall

* Setup firewall in site.pp

.. code-block:: bash

  resources { "firewall":
    purge => true
  }

  Firewall {
    before  => Class['my_fw::post'],
    require => Class['my_fw::pre'],
  }

  class { ['my_fw::pre', 'my_fw::post']: }
  class { 'firewall': }
      
  class my_fw::pre {
    Firewall {
      require => undef,
    }

    # Default firewall rules
    firewall { '00000 accept all icmp':
      proto   => 'icmp',
      action  => 'accept',
    }->
    firewall { '00001 accept all to lo interface':
      proto   => 'all',
      iniface => 'lo',
      action  => 'accept',
    }->
    firewall { '00002 accept related established rules':
      proto   => 'all',
      state   => ['RELATED', 'ESTABLISHED'],
      action  => 'accept',
    }
  }

  class my_fw::post {
    firewall { '99999 drop all':
      proto   => 'all',
      action  => 'drop',
      before  => undef,
    }
  }

* Make sure pluginsync is enabled in ``puppet.conf`` in section ``[main]``

.. code-block:: bash

  pluginsync = true
  
* The comment must contain an index to get the order of the rules

.. code-block:: bash

  firewall { "00001 a comment":
    proto => 'tcp',
    iniface => 'eth0',
    dport => 22,
    action => 'accept',
  }


SELinux
=======

.. code-block:: bash

  selboolean { "a comment":
    name => "httpd_enable_cgi",
    value => 'off',
  }

  selmodule { "load a policy":
    ensure => present,
    selmoduledir => "/path/to/policy",
    name => "filename_without_pp",
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


Environments
============

* Add the following to puppet.conf

.. code-block:: bash

  [main]
    modulepath = $confdir/modules
    manifest = $confdir/manifests/site.pp
  
  [devel]
    modulepath = $confdir/devel/modules
    manifest = $confdir/devel/manifests/site.pp

* Now you can tell a puppet agent to use the devel environment by adding ``--environment devel``


Syntaxcheck a manifest
======================

* Check syntax of a file

.. code-block:: bash

  puppet parser validate <some_file.pp>


* Test a whole module

.. code-block:: bash

  puppet apply --noop <manifests/init.pp>
  

Getting help
============

* http://docs.puppetlabs.com/puppet/3/reference/
* http://www.puppetcookbook.com
* get a list of all known resources

.. code-block:: bash

  puppet describe --list

* doc about a resource

.. code-block:: bash

  puppet describe -s <keyword>
  (+ 1 2)

Debugging
=========

* Master

.. code-block:: bash

  puppet agent --no-daemonize --verbose

* Agent

.. code-block:: bash

  puppet agent --no-daemonize --verbose --test --noop

* Use ``--debug`` instead of ``--verbose`` for even more output
* You can use the ``notice("foo")`` command somewhere to send a log message
* See ``/var/lib/puppet/state/last_run_report.yaml`` for information update last update
