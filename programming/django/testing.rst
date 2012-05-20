#######
Testing
#######

* https://github.com/ericholscher/django-test-utils
* https://github.com/kmmbvnr/django-jenkins
* https://github.com/gregmuellegger/django-autofixture
* http://readthedocs.org/docs/django-test-utils/en/latest/testmaker.html

* Get emails to stdout

.. code-block:: python 

  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

* Change language for test client

.. code-block:: python 

  self.client.cookies["django_language"] = 'fr'

* Test an AJAX request

.. code-block:: python 

  client.get('/url/',{},HTTP_X_REQUESTED_WITH='XMLHttpRequest')
