################
Multiprocessing
################

* For real concurrency on mutli-core cpus use the package `multiprocessing <http://docs.python.org/library/multiprocessing.html>`_ due to the `global-interpreter-lock <http://docs.python.org/glossary.html#term-global-interpreter-lock>`_ in the python interpreter

* `Celery is an asynchronous task queue/job queue <http://celeryproject.org/>`_

Multiprocessing with Queues 
============================

.. code-block:: python

  from multiprocessing import Process, Queue
  import time

  def f(q):
      time.sleep(3)
      q.put([42, None, 'hello'])

  if __name__ == '__main__':
      q = Queue()
      p = Process(target=f, args=(q,))
      p.start()
      print q.get()
      p.join() # wait for process to terminate


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