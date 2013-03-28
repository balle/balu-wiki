#######
Inotify
#######

* React on file change events
* Install incron
* incrontab -e

.. code-block:: bash

  <directory> <file change mask> <command or action>  options
  /var/www/html IN_CREATE /root/scripts/backup.sh
  /sales IN_DELETE /root/scripts/sync.sh
  /var/named/chroot/var/master IN_CREATE,IN_ATTRIB,IN_MODIFY /sbin/rndc reload
  /tmp IN_ALL_EVENTS logger "file $@ changed"  


Recursive inotify
=================

* https://github.com/splitbrain/Watcher
* http://www.splitbrain.org/blog/2011-01/07-watcher_a_recursive_incron_alternative

.. code-block:: bash

  [DEFAULT]
  logfile=/var/log/watcher.log
  pidfile=/var/run/watcher.pid

  [data]
  watch=/data
  events=create,delete,modify
  recursive=true
  autoadd=true
  command=rsync -a --delete $filename /media/backup
