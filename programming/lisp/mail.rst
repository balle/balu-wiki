======================
Sending mail with lisp
======================

* (ql:quickload "cl-smtp")

* Send HTML mail with attachment

.. code-block:: lisp

  (cl-smtp:send-email
   +mail-server+
   "from-email@example.com"
   "to-email@example.com"
    "Subject"
     "<html><body>
     <p>
     Shiny <strong>h</strong><em>t</em><small>m</small>l.
     </p>
     <p>
     </body></html>"
      :extra-headers '(("Content-type" "text/html; charset=\"iso-8859-1\""))
      :attachments '("/path/to/file"))
