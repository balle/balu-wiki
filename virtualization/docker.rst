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


Update images
=============

* Only one

.. code-block:: bash

  docker pull <image>

* All images

.. code-block:: bash

  docker images | awk '{print $1}' | xargs -L1 docker pull


Port forward
============

* Starts in daemon mode and forwards container port 80 to host port 8888 but only on loopback interface

.. code-block:: bash

  docker run -d -p 127.0.0.1:8888:80 <image>

* Automatically forward all ports

.. code-block:: bash

  docker run -P <image>


Set fixed IP for container
==========================

.. code-block:: bash

  docker run --ip=<container_ip> --default-gateway=<gw_ip>


Get IP of container
===================

.. code-block:: bash

  docker inspect <container_id> | grep IPAddress


Share directory between host and container
==========================================

* Via Dockerfile

.. code-block:: bash

  VOLUME        ["/var/volume1", "/var/volume2"]

* Via command-line

.. code-block:: bash

  -v /path/on/host:/path/in/container


Display CPU / RAM usage of container
====================================

.. code-block:: bash

  docker stats <container_id>


Get STDOUT / STDERR from container
===================================

.. code-block:: bash

  docker log <container_id>


Get a shell on a running container
==================================

.. code-block:: bash
  docker exec -it <container_id> bash


Example docker file
===================

.. code-block:: bash

  #
  # base image is latest official redhat rhel7
  #
  from rhel7:latest

  # Update the system
  RUN yum update -y

  # Install web server
  RUN yum install -y httpd

  # Copy files to image
  #COPY ./public-html/ /usr/local/apache2/htdocs/
  #COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf

  # Start the service
  EXPOSE 80
  CMD ["-D", "FOREGROUND"]
  ENTRYPOINT ["/usr/sbin/httpd"]


Troubleshooting
===============

* ``Couldn’t create Tag store: unexpected end of JSON input``

.. code-block:: bash

  rm /var/lib/docker/repositories
