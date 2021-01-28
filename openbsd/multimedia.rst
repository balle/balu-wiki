###########
Multimedia
###########

Increase / derease volumne
===========================

.. code-block:: bash

  mixerctl outputs.master=100,100


Enable audio recording
======================

* Edit /etc/sysctl.conf and add

.. code-block:: bash

  kern.audio.record=1

