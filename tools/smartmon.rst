###############
Smartmon Tools
###############

* health check

.. code-block:: bash

  smartctl -H <dev>

* short self test

.. code-block:: bash

  smartctl -t short <dev>

* long self test (better run at night)

.. code-block:: bash

  smartctl -t long <dev>

* test results

.. code-block:: bash

  smartctl -l selftest <dev>


