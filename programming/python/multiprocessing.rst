################
Multiprocessing
################

* For real concurrency on mutli-core cpus use the package `multiprocessing <http://docs.python.org/library/multiprocessing.html>`_ due to the `global-interpreter-lock <http://docs.python.org/glossary.html#term-global-interpreter-lock>`_ in the python interpreter

* `Celery is an asynchronous task queue/job queue <http://celeryproject.org/>`_

Parallel map
=============

.. code-block:: bash

  import urllib2
  import multiprocessing

  def fetch(url):
    print "GET " + url
    body = urllib2.urlopen(url).read()
    print "FIN " + url; return (url, body)

  urls = ['http://www.google.de', 'http://www.ccc.de', 'http://www.heise.de', 'http://www.codekid.net']
  pool = multiprocessing.Pool()

  for url, body in pool.imap(fetch, urls):
    print "GOT body for " + url


Gevent
======

.. code-block:: bash

  import gevent
  import urllib2

  def fetch(url):
    print "GET " + url
    body = urllib2.urlopen(url).read()
    print "FIN " + url
    return (url, body)

  urls = ['http://www.google.de', 'http://www.ccc.de', 'http://www.heise.de', 'http://www.codekid.net']
  jobs = [gevent.spawn(fetch, url) for url in urls]

  gevent.joinall(jobs, timeout=2)
  [job.get() for job in jobs]


Multiprocessing with Queues
============================

.. code-block:: python

  from multiprocessing import Process, Queue
  import commands

  nr_of_threads = 4

  def do_work(work_queue, result_queue):
      while work_queue.qsize():
        job = work_queue.get()
        result_queue.put(["what", "ever"])

  def parallel_work(jobs, nr_of_threads):
    work_queue = Queue()
    result_queue = Queue()
    result = {}

    for job in jobs:
        work_queue.put(job)

    if nr_of_threads > len(jobs):
        nr_of_threads = len(jobs)

    for i in range(nr_of_threads):
        worker = Process(target=do_work, args=(work_queue,result_queue))
        worker.start()

    while len(result.keys()) < len(jobs):
        data = result_queue.get()
        print data
        result[data[0]] = data[1]

    return result


Fork Decorator
==============

.. code-block:: python

  def forked(func):
    def wrapped(*args, **kwargs):
      import os

      pid = os.fork()
      if pid > 0: func(*args, **kwargs)

    return wrapped


Thread Decorator
================

.. code-block:: python

  def threaded(name):
    def callf(func):
      def wrapped(*args, **kwargs):
        import thread

        def newfunc():
          func(*args, **kwargs)
        thread.start_new_thread(newfunc, ())
      return wrapped
    return callf


MapReduce
==========

* `Disco <http://discoproject.com/>`_ MapReduce Framework with Python API
* Local example for multi-core cpu

.. code-block:: python

  import sys
  from multiprocessing import Pool

  def split_words(line):
      return [x.rstrip("\n") for x in line.split(" ")]


  def myreduce(mylist):
      """
      gets [['word1'], ['word1', 'word2', 'word1']]
      returns {'word1': 3 'word2': 1}
      """
      result = {}

      for sublist in mylist:
          for word in sublist:
              try:
                  result[word] += 1
              except KeyError:
                  result[word] = 1

      return result


  if len(sys.argv) < 2:
      print sys.argv[0] + ": <file>"
      sys.exit(1)

  pool = Pool(processes=10)
  lines = file(sys.argv[1]).xreadlines()

  words = pool.map(split_words, lines)
  word_count = myreduce(words)

  for (word, count) in word_count.items():
      print word + ": " + str(count)
