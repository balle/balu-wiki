===
Web
===

Full featured http client
=========================

* (ql:quickload "drakma")

* GET with auth

.. code-block:: Lisp

  (require 'drakma)
  (setq resp (drakma:http-request "http://www.codekid.net"
                                  :basic-authoization '("user" "password")))
  (print resp)

* POST

.. code-block:: Lisp

  (drakma:http-request "http://some.secure.website/with-login"
                       :method :post
                       :parameters '(("username" "hans")
                                      ("password" "wurst")))
                                      
* If you want to read the respone from a stream set ``:want-stream t``
* More examples on http://weitz.de/drakma/#examples


Web frameworks
==============

* mod_lisp
* http://wookie.beeets.com
* https://github.com/fukamachi/caveman/
* http://weblocks.viridian-project.de


Web server
==========

* http://weitz.de/hunchentoot/
