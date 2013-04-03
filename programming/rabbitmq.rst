
########
RabbitMQ
########

Overview
========

* Producer sends messages to an exchange
* An exchange decides what to do with a message and maybe forwords it to one or more queues
* A binding binds an exchange to a queue
* A queue store the message until the consumer receives (and acknowledges) it

* Get status

.. code-block:: bash

  rabbitmqctl status
  rabbitmqctl list_connections
  rabbitmqctl list_exchanges
  rabbitmqctl list_queues
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


Enable management plugin
========================

.. code-block:: bash

  /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management

* Restart rabbitmq-server
* Point your browser to `http://localhost:55672`


Troubleshooting
===============

* RabbitMQ server needs `disk_free_limit` space (default 1 Gb) otherwise it wont accept messages

  
Python example
==============

* pip install pika

* Sending

.. code-block:: python

  import pika

  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.queue_declare(queue='hello', duarable=True)
  channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!',
                        properties=pika.BasicProperties(delivery_mode=2))
  print " [x] Sent 'Hello World!'"

* `duarable=True` save queue before restarting / stopping server
* `delivery_mode=2` save messages of this queue

* Receiving

.. code-block:: python

  import pika

  connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
  channel = connection.channel()
  channel.queue_declare(queue='hello')

  print ' [*] Waiting for messages. To exit press CTRL+C'

  def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    channel.start_consuming()
    
* Set `no_ack` to `False` to send acks after task was processes otherwise messages could get lost if worker dies
