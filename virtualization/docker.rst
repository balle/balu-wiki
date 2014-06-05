######
Docker
######

Install a new image
===================

.. code-block:: bash

  docker search <whatever>
  docker pull <image>


Run image
=========

* Runs a new container of image in interactive mode and starts a bash

.. code-block:: bash

  docker run -i -t <image> bash

* Start an existing container

.. code-block:: bash

  docker start -i <container_id>


List installed images
=====================

.. code-block:: bash

  docker images


Save changes
============

.. code-block:: bash

  docker commit <container_id> <image_name>


Export images
=============

.. code-block:: bash

  docker save <image>
  docker load <image>


Port forward
============

* Starts in daemon mode and forwards container port 80 to host port 8888

.. code-block:: bash

  docker run -d -p 8888:80 <image>


Troubleshooting
===============

* ``Couldn’t create Tag store: unexpected end of JSON input``

.. code-block:: bash

  rm /var/lib/docker/repositories
