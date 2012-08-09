##################
Performace tricks
##################

* For big ranges use ``xrange()`` cause it creates a generator
* Use ``xreadlines()`` for big files cause it also creates a generator
* Setting environment variable ``PYTHONUNBUFFERED`` will force stdout / stderr to be unbuffered
* ``os.fdopen("file", "r", 0)`` to open file without buffering
* Use ``flush()`` on filehandle to flush I/O buffer
* Use a list and ``join`` instead of string concatenation
* Prefer ``while 1`` instead of `` while True``
* Write "x < y < z" instead of "x < y and y < z"
* ``"test " + var`` is slower than ``"test %s" % (var,)``
* ``map()`` and list comprehension are faster than a loop
* put your global variables into a ``main`` function and call it by:

.. code-block:: Python

  if __name__ == '__main__':
    main()

* profile your code

.. code-block:: Python

  import profile
  profile.run(“any_python_expression”)
