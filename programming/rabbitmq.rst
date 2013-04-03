########
RabbitMQ
########

Overview
========

* Get status

.. code-block:: bash

  rabbitmqctl status
  rabbitmqctl list_connections
  rabbitmqctl list_channels
  rabbitmqctl list_users


User management
===============

* Add a new user

.. code-block:: bash

  rabbitmqctl add_user <username> <password>

* Change password

.. code-block:: bash

  rabbitmqctl change_password <username> <newpassword>

* Delete user

.. code-block:: bash

  rabbitmqctl delete_user <username>

  
Python example
==============

* pip install pika

* Sending

.. code-block:: python

  import pika

  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.queue_declare(queue='hello')
  channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
  print " [x] Sent 'Hello World!'"
                                              
* Receiving

.. code-block:: python

  import pika

  connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
  channel = connection.channel()
  channel.queue_declare(queue='hello')

  print ' [*] Waiting for messages. To exit press CTRL+C'

  def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    channel.start_consuming()
    
