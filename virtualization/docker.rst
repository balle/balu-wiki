######
Docker
######

Search for images
=================

* Goto `https://hub.docker.com`

* Or run

.. code-block:: bash

  docker search <whatever>
  

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


List images
===========

* All
  
.. code-block:: bash

  docker images

* All without container

.. code-block:: bash

  docker images -f "dangling=true"

List containers
===============

* Only running
  
.. code-block:: bash

  docker ps

* All
  
.. code-block:: bash

  docker ps -a

* All container for one image

.. code-block:: bash
		
  docker ps -a -q --filter "ancestor=<image-id-or-name>"

* All not running

.. code-block:: bash

  docker ps -a -q --filter "status=exited"

  
Save changes done in an container
==================================

.. code-block:: bash

  docker commit <container_id> <image_name>


Export images
=============

.. code-block:: bash

  docker save <image> > <archive_file>
  docker load -i <archive_file>


Upgrade images
=============

* Only one

.. code-block:: bash

  docker pull <image>

* All images

.. code-block:: bash

  docker images | awk '{print $1}' | xargs -L1 docker pull


Delete images and containers
============================

* A specific ontainer

.. code-block:: bash

  docker rm <container_id>

* All container for one image

.. code-block:: bash
		
  docker rm -f $(docker ps -a -q --filter "ancestor=<image-id-or-name>")

* All not running containers

.. code-block:: bash

  docker container prune

* All containers

.. code-block:: bash

  docker rm -f $(docker container ls -q)

* A specific image
  
.. code-block:: bash

  docker rmi <image_id>

* All images without a container

.. code-block:: bash

  docker image prune -a
  
* All containers

.. code-block:: bash

  docker rmi $(docker image ls -q)

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

* Or by volume name automatically created by docker

.. code-block:: bash

  -v my-volume:/path/in/container

* To automatically map the current source code directory as /code directory in the container to see code updates immediately

.. code-block:: bash

  docker run -d --name dev-container -v $(pwd):/code <image_name_or_id>

  
Allow docker container to access DISPLAY
========================================

.. code-block:: bash

  xhost +local:docker

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

Show layers of image
====================

.. code-block:: bash

  docker historty <image_id>

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


Image from scratch
==================

.. code-block:: bash

  debootstrap bullseye bullseye
  tar -C bullseye -c . | docker import - mydebian

* Or via Dockerfile

.. code-block:: bash

  FROM scratch
  COPY some_static_binary /
  ENTRYPOINT ["/some_static_binary"]

Tag an image
============

.. code-block:: bash

  docker image tag <tag_name_or_image_id> <new_tag_name>
  docker image tag example-app:latest example-app:1.0

Troubleshooting
===============

* ``Couldn’t create Tag store: unexpected end of JSON input``

.. code-block:: bash

  rm /var/lib/docker/repositories
