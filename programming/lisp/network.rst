==========
Networking
==========

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

