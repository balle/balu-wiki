##################
Performace tricks
##################

* For big ranges use ``xrange()`` cause it creates a generator
* Use ``xreadlines()`` for big files cause it also creates a generator
* Setting environment variable ``PYTHONUNBUFFERED`` will force stdout / stderr to be unbuffered
* ``os.fdopen("file", "r", 0)`` to open file without buffering
* Use ``flush()`` on filehandle to flush I/O buffer
