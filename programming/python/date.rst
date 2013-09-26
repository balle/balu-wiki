###########
Date tricks
###########

* Which date is in a week?

.. code-block:: python

  from datetime import datetime, timedelta
  in_one_week = datetime.today() + timedelta(days=7)
  print in_one_week.strftime("%d.%m.%Y")

* Create datetime object from date

.. code-block:: python

  mydate = datetime(1981, 12, 31, 23, 59)

* Get unix time of a date

.. code-block:: python

  time.mktime(datetime(1982, 12, 31, 16, 32).timetuple())

* Get date from unix time

.. code-block:: python

  datetime.datetime.fromtimestamp(1004260000)

* Format date

.. code-block:: python

  print mydate.strftime("%d.%m.%Y %H:%M")

* Combine date and time

.. code-block:: python

  from datetime import datetime, time
  datetime.combine(datetime.today(), time())

* Check if date is over

.. code-block:: python

    end_date = datetime(2011, 12, 24, 0, 0)

    if datetime.now() > end_date:
