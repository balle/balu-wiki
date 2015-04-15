#####
Redis
#####

Connect
=======

* TCP socket

.. code-block:: bash

  redis-cli -h my-host -p 1234 -a mypassword

* UNIX socket

.. code-block:: bash

  redis-cli -s <path/to/unix.sock>


List all keys
=============

.. code-block:: bash

  redis> KEYS *

* With types

.. code-block:: bash

  for KEY in $(redis-cli KEYS "*" | cut -d " " -f 2); do echo -en "$KEY - "; redis-cli TYPE "$KEY"; done


Show type of keys
=================

.. code-block:: bash

  redis> type "key"


Read keys
=========

* Normal key

.. code-block:: bash

  redis> GET "key"

* set key

.. code-block:: bash

  redis> SMEMBERS "key"

* hash key

.. code-block:: bash

  redis> HGETALL "key"


Write keys
==========

* Normal key

.. code-block:: bash

  redis> SET "key" "value"

* set key

.. code-block:: bash

  redis> SADD "key" "value"

* hash key

.. code-block:: bash

  redis> HSET "key" "field" "value"


Delete a key
============

.. code-block:: bash

  redis> DEL "key"
  

Drop database
=============

.. code-block:: bash

  redis> FLUSHDB


Save changes to disk
====================

.. code-block:: bash

  redis> SAVE

* You can define a periodic interval in ``redis.conf``

.. code-block:: bash

  save 60 99999
  

Monitor realtime requests
=========================

.. code-block:: bash

  redis> MONITOR


