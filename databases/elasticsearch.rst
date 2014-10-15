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


Insert data manually
=====================

.. code-block:: bash

  curl -XPUT 'http://localhost:9200/dept/employee/1' -d '{ "empname": "emp1"}'


Configure Rsyslog to log to Elasticsearch
=========================================

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
        constant(value="\",\"tag\":\"")   property(name="syslogtag" format="
  

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

* Example config

.. code-block:: bash

  # Listen to Syslog
  <source>
    type syslog
    port 42185
    tag hostname.system
  </source>
  
  # Apache Access Logs
  <source>
    type tail
    format apache2
    path /var/log/httpd/access_log
    pos_file /var/log/td-agent/httpd.access.pos
    tag hostname.httpd.access
  </source>
  
  # Apache Error Logs
  <source>
    type tail
    format apache_error
    path /var/log/httpd/error_log
    pos_file /var/log/td-agent/httpd.error.pos
    tag hostname.httpd.error
  </source>

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
  <match *.**>
      type stdout
  </match>

* Last but not least configure your systlog to send messages to fluentd

.. code-block:: bash

  *.* @127.0.0.1:42185

* Start fluentd in foreground for testing purpose

.. code-block:: bash

  fluentd -c /etc/fluent/fluent.conf -vv



Kibana Web Frontend
===================

* Install it http://www.elasticsearch.org/overview/kibana/installation/
* Have a look at https://www.youtube.com/watch?v=hXiBe8NcLPA&index=4&list=UUh7Gp4Z-f2Dyp5pSpLO3Vpg
* For Dashboards see https://github.com/search?utf8=%E2%9C%93&q=kibana+dashboard&type=Repositories&ref=searchresults


  
