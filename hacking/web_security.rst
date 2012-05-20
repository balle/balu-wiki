#############
Web Security
#############

Information disclosure 
=======================

* CVS/Entries .svn/entries .git/index
* hidden parameter debug / test / trace = true / on / 1
* docs / logs / backup / conf / test


Authentication 
===============

* Common users: admin, test, demo, guest, $company, $product
* Common passwords: test, test123, password, password1, password123, qwertz, qwerty, letmein
* Look at: Password Recovery, Remember me


ACL bypass techniques 
======================

* Try GET instead of POST and vice versa
* Try HEAD instead of GET
* Double-Slash URL
* Hidden Parameter like loggedin / isadmin = true / on / 1
* change userid


Cracking Session Ids 
=====================

* hex / base64 encoding
* predictable token depending on bad algo e.g. +1 or +time
* weak generation e.g. user AND time -> md5


Fooling Filters 
================

* Double the input <scr<script>ipt>
* Bypass by sequence <scri'pt>
* urlencode (double urlencode)
* unicode
* escape / escape escape


SQL injection 
==============

* UNION SELECT NULL, NULL
* ' or double ''
* output von 2 vergleichen mit 1+1
* output vergleichen von order by 1 2 3
* select table_schema, table_name from information_schema.tables
* select into outfile
* select load_file('/etc/passwd')


Ajax 
=====

* var request = new XMLHttpRequest();
* request.open('GET', '/muh', true);
* request.send();

.. code-block:: bash

  var request = new XMLHttpRequest();
  request.onreadystatechange = handler;
  request.open('POST', '/muh', true);
  request.send("name=balle&pass=maeh");


Bypass Same Origin 
===================

* Set header

.. code-block:: bash

  Access-Control-Allow-Origin: *


Webworker 
==========

* Run javascript in the background

.. code-block:: bash

  var worker = new Worker("worker_script.js");
  worker.onmessage = function(e){
    e.data
  };
  worker.postMessage("start");


Client / Session Storage 
=========================

.. code-block:: bash

  sessionStorage.setItem('key', 'value');
  sessionStorage.getItem('key')
  sessionStorage.deleteItem('key')


Web SQL 
========

.. code-block:: bash

  var db = openDatabase('mydb', '1.0', 'my first database', size)
  db.transaction(function (tx) {
   tx.executeSql('CREATE TABLE foo (id unique, text)');
  }


Misc 
=====

* Check negative numbers
* zwei sessions / operationen exakt gleichzeitig ausführen
