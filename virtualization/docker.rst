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


List running containers
=======================

.. code-block:: bash

  docker ps


Save changes
============

.. code-block:: bash

  docker commit <container_id> <image_name>


Export images
=============

.. code-block:: bash

  docker save <image> > <archive_file>
  docker load -i <archive_file>


Port forward
============

* Starts in daemon mode and forwards container port 80 to host port 8888 but only on loopback interface

.. code-block:: bash

  docker run -d -p 127.0.0.1:8888:80 <image>

* Automatically forward all ports

.. code-block:: bash

  docker run -P <image>


Get IP of container
===================

.. code-block:: bash

  docker inspect <container_id> | grep IPAddress


Display CPU / RAM usage of container
====================================

.. code-block:: bash

  docker stats <container_id>


Get STDOUT / STDERR from container
===================================

.. code-block:: bash

  docker log <container_id>

Troubleshooting
===============

* ``Couldn’t create Tag store: unexpected end of JSON input``

.. code-block:: bash

  rm /var/lib/docker/repositories
