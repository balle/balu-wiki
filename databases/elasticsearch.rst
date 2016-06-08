##############
Elasticsearch
##############

Overview
=========

* http://elasticsearchtutorial.blogspot.ch/


Install browser plugin
=======================

.. code-block:: bash

  /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head

* Now point your browser to http://localhost:9200/_plugin/head/


Dump database
=============

.. code-block:: bash

  curl -XPUT 'http://localhost:9200/_snapshot/my_backup' -d '{ "type": "fs", "settings": { "location": "/mount/backups/my_backup", "compress": true }}'


Configure cluster
=================

* Edit ``/etc/elasticsearch/elasticsearch.yml``
* Set cluster.name, node.name and network.host
* Make sure TCP port 9300 is open


Cluster autodiscovery is not working
====================================

* Edit ``/etc/elasticsearch/elasticsearch.yml``
* Make one node the master node

.. code-block:: bash

  node.master: true
  node.data: true
  discovery.zen.ping.multicast.enabled: false
  discovery.zen.ping.unicast.hosts: ["node1.example.com"]

* Let the others connect to the master node

.. code-block:: bash

  node.master: false
  node.data: true
  discovery.zen.ping.multicast.enabled: false
  discovery.zen.ping.unicast.hosts: ["node1.example.com"]


Add security to Elasticsearch
=============================

* Need user and rights management or encryption and authentication?
* Install the plugin shield
* https://www.elastic.co/products/shield


Insert data manually
=====================

.. code-block:: bash

  curl -XPUT 'http://localhost:9200/dept/employee/1' -d '{ "empname": "emp1"}'


Configure Rsyslog to log to Logstash
====================================

* Create file /etc/rsyslog.d/logstash.conf

.. code-block:: bash

  *.* @127.0.0.1:5544


Configure Rsyslog to log to Fluentd
====================================

* Create file /etc/rsyslog.d/fluentd.conf

.. code-block:: bash

  *.* @127.0.0.1:42185


Configure Rsyslog to log directly to Elasticsearch
===================================================

* For RHEL7 / CentOS 7 the rsyslog-elasticsearch plugin is included
* For RHEL6 use repo http://rpms.adiscon.com/v5-stable/rsyslog.repo

.. code-block:: bash

  yum install rsyslog-elasticsearch

* Now edit ``/etc/rsyslog.conf``

.. code-block:: bash

  module(load="imuxsock")             # for listening to /dev/log
  module(load="omelasticsearch") # for outputting to Elasticsearch
  # this is for index names to be like: logstash-YYYY.MM.DD
  template(name="logstash-index"
    type="list") {
      constant(value="logstash-")
      property(name="timereported" dateFormat="rfc3339" position.from="1" position.to="4")
      constant(value=".")
      property(name="timereported" dateFormat="rfc3339" position.from="6" position.to="7")
      constant(value=".")
      property(name="timereported" dateFormat="rfc3339" position.from="9" position.to="10")
  }

  # this is for formatting our syslog in JSON with @timestamp
  template(name="plain-syslog"
    type="list") {
      constant(value="{")
        constant(value="\"@timestamp\":\"")     property(name="timereported" dateFormat="rfc3339")
        constant(value="\",\"host\":\"")        property(name="hostname")
        constant(value="\",\"severity\":\"")    property(name="syslogseverity-text")
        constant(value="\",\"facility\":\"")    property(name="syslogfacility-text")
        constant(value="\",\"tag\":\"")   property(name="syslogtag" format="on")
        constant(value="\",\"message\":\"")    property(name="msg" format="on")
      constant(value="\"}")
  }
  # this is where we actually send the logs to Elasticsearch (localhost:9200 by default)
  action(type="omelasticsearch"
      template="plain-syslog"
      searchIndex="logstash-index"
      dynSearchIndex="on")


Let Elasticsearch listen only on loopback
==========================================

* Edit /etc/elasticsearch/elasticsearch.yml

.. code-block:: bash

  network.host: 127.0.0.1


Use logstash as log aggregator
==============================

* Create /etc/logstash/conf.d/10-syslog.conf

.. code-block:: bash

  input {
    syslog {
      type => syslog
      port => 5544
    }
  }

  filter {
    if [type] == "syslog" {
      grok {
        match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?: %{GREEDYDATA:syslog_message}" }
        add_field => [ "received_at", "%{@timestamp}" ]
        add_field => [ "received_from", "%{host}" ]
      }
      syslog_pri { }
      date {
        match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
      }
    }
  }

* Create /etc/logstash/conf.d/30-elasticsearch-output.conf

.. code-block:: bash

  output {
    elasticsearch { host => localhost }
    stdout { codec => rubydebug }
  }


Use fluentd as log aggregator
=============================

* Can collecd and parse log from many sources (200+)
* Is written in Ruby and needs no Java like Logstash
* Can output to many directions including files, mongodb and of course elasticsearch
* For installation see http://docs.fluentd.org/categories/installation
* Install Elasticsearch plugin

.. code-block:: bash

  gem install fluent-plugin-elasticsearch

* If your ruby version is too old or buggy install fluentd inside rvm

.. code-block:: bash

  curl -sSL https://get.rvm.io | bash -s stable --ruby
  source /usr/local/rvm/scripts/rvm
  gem install fluentd
  gem install fluent-plugin-elasticsearch

* Regular expressions for parsing logs can be tested on http://rubular.com/
* Time format options can be looked up here http://www.ruby-doc.org/core-1.9.3/Time.html#method-i-strftime
* Example config

.. code-block:: bash

  # live debugging agent
  #<source>
  #  type debug_agent
  #  bind 127.0.0.1
  #  port 24230
  #</source>

  # Listen to Syslog
  <source>
    type syslog
    port 42185
    tag system.raw
  </source>

  # Apache Access Logs
  <source>
    type tail
    format apache2
    path /var/log/httpd/access_log
    pos_file /var/log/fluentd/httpd.access.pos
    tag httpd.access
  </source>

  # Apache Error Logs
  <source>
    type tail
    format apache_error
    path /var/log/httpd/error_log
    pos_file /var/log/fluentd/httpd.error.pos
    tag httpd.error
  </source>

  # Tag kernel messages
  <match system.raw.**>
    type rewrite_tag_filter
    rewriterule1 ident ^kernel$  kernel.raw # kernel events
    rewriterule2 ident .* system.unmatched     # let all else through
  </match>

  # Identify iptables messages
  <match kernel.raw.**>
    type rewrite_tag_filter
    rewriterule1 message ^IN=.* OUT=.+$ iptables.raw  # iptables events
    rewriterule2 message .* kernel.unmatched      # let all else through
 </match>

  # Parse iptables messages
  # IN=eno1 OUT= MAC=aa:bb:cc:aa:bb:cc:aa:bb:cc:aa:bb:cc:aa:00 SRC=192.168.10.42 DST=192.168.10.23 LEN=148 TOS=0x00 PREC=0x00 TTL=255 ID=53270 DF PROTO=UDP SPT=5353 DPT=5353 LEN=128
  <match iptables.raw.**>
    type parser
    key_name message # this is the field to be parsed!
    format /^IN=(?<iface>.*) OUT=(?<oface>.*) MAC=(?<mac>.*?) (SRC=(?<srcip>.*))? (DST=(?<dstip>.*))? LEN=(?<pkglen>.+) TOS=(?<pkgtos>.+) PREC=(?<pkgrec>.+) TTL=(?<pkgttl>.+) ID=(?<ipid>.+) \w{0,2}\s?PROTO=(?<pkgproto>.+)( SPT=(?<srcport>.+) DPT=(?<dstport>.+) LEN=(.*))?$/
    time_format %b %d %H:%M:%S
    tag iptables.parsed
  </match>

  # write to file
  #<match iptables.parsed>
  #  type file
  #  path /var/log/td-agent/iptables.log
  #</match>

  # Write to elasticsearch
  <match *.**>
      type elasticsearch
      host localhost
      port 9200
      include_tag_key true
      tag_key _key
      logstash_format true
      flush_interval 10s
  </match>

  # Log to stdout for debugging
  #<match *.**>
  #    type stdout
  #</match>

* Last but not least configure your systlog to send messages to fluentd

.. code-block:: bash

  *.* @127.0.0.1:42185

* Start fluentd in foreground for testing purpose

.. code-block:: bash

  fluentd -c /etc/fluent/fluent.conf -vv



Kibana Web Frontend
===================

* Install it http://www.elasticsearch.org/overview/kibana/installation/
* Run bin/kibana
* Or use this systemd service file

.. code-block:: bash

  [Service]
  ExecStart=/opt/kibana4/bin/kibana
  Restart=always
  StandardOutput=syslog
  StandardError=syslog
  SyslogIdentifier=kibana4
  User=root
  Group=root
  Environment=NODE_ENV=production

  [Install]
  WantedBy=multi-user.target

* Have a look at https://www.youtube.com/watch?v=hXiBe8NcLPA&index=4&list=UUh7Gp4Z-f2Dyp5pSpLO3Vpg
* For Dashboards see https://github.com/search?utf8=%E2%9C%93&q=kibana+dashboard&type=Repositories&ref=searchresults
