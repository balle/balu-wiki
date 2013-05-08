##########
Networking
##########

Get hostname
============

* Local

.. code-block:: lisp

  (machine-instance)

* Remote

.. code-block:: lisp

  (require 'sb-bsd-sockets)
  (in-package 'sb-bsd-sockets)
  (host-ent-name (get-host-by-name "www.lisp.org"))


Example socket client
=====================

* (ql:quickload "usocket")

.. code-block:: lisp

  (require :usocket)
  (setq sock (usocket:socket-connect "www.codekid.net" 80))
  (format (usocket:socket-stream sock) "~A~C~C~A~C~C~A~C~C~C~C"
  	                               "GET / HTTP/1.1"
	  	  		       #\Return #\Newline
				       "Host: www.codekid.net"
				       #\Return #\Newline
				       "Connection: close"
				       #\Return #\Newline #\Return #\Newline)
  (force-output (usocket:socket-stream sock))

  (loop for line = (read-line (usocket:socket-stream sock))
     while line do
     (format t "~A~%" line))


SNMP
====

* (ql:quickload "snmp")

.. code-block:: lisp

  (snmp:with-open-session (s "192.168.1.1" 
                             :version :v1 
                             :community "public") 
     (snmp:snmp-walk s "system"))

* For more see http://cl-net-snmp.svn.sourceforge.net/viewvc/cl-net-snmp/snmp/branches/6/doc/papers/ILC09-SNMP.pdf
