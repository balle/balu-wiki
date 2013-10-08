#######################
Functional programming
#######################

Basics
======

* lambda - Create an anonymous function
* filter(func, list) - Call func on every list item, return a new list of elements where func returned True
* map(func, list) - Call func on every list item, return new list a returned results
* reduce(func, list) - Call func with first to items of list, than call the result with the third, that result with the forth and so on

.. code-block:: python

  reduce(lambda x,y: x+y, [1,2,3])
  -> (1 + 2) + 3

* zip(list1, list2, listN) - creates list of tuples containing the n-th item of the input lists

* A complete example

.. code-block:: python

  even = lambda x: x % 2
  square = lambda x: x * x
  map(square, filter(even, range(1,100)))
  [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, 1089, 1225, 1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249, 3481, 3721, 3969, 4225, 4489, 4761, 5041, 5329, 5625, 5929, 6241, 6561, 6889, 7225, 7569, 7921, 8281, 8649, 9025, 9409, 9801]

* The same with list comprehensions

.. code-block:: python

  [x*x for x in range(1,100) if x % 2]

* find items contained in both lists

.. code-block:: python

  [x for x in list1 if x in list2]


Generators
==========

* Generator remember it's state and return (yield) the next item

.. code-block:: python

  def gen_even_numbers():
       i = 2

       while True:
           yield i
           i += 2

  gen = gen_even_numbers()
  gen.next()

* yield can be given an argument with send

.. code-block:: python

  def gen_even_numbers():
       i = 2

       while True:
           val = (yield i)
           if val: i = val
           else: i += 2

  gen = gen_even_numbers()
  gen.next()
  gen.send(12)

* Generator expressions (like list comprehensions with round parentheses)

.. code-block:: python

  gen = (x for x in filter(lambda x: x % 2 == 0, range(100)))

Iterators
==========

.. code-block:: python

  class MyIter:
      def __init__(self, i=1):
          self.nr = i
      def __iter__(self):
          return self
      def next(self):
          if self.nr > 100:
              raise StopIteration
          self.nr += 2
          return self.nr

  muh=MyIter()
  muh.next()

Iterators with generators
=========================

  class MyIter:
      def __init__(self, i=1):
         self.nr = (x for x in filter(lambda x: x % 2 == 0, range(100)))
      def __iter__(self):
          return self
      def next(self):
         return self.nr.next()


Functools
=========

* create new function with fixed parameter

.. code-block:: python

  def sum(a,b):
      return a + b

  import functools
  add_two = functools.partial(sum, b=2)


Closure
========

* A closure is a function pointer with saved parameters

.. code-block:: python

  from urllib import urlopen

  def page(url):
    def get():
      return urlopen(url).read()
    return get

  codekid = page("http://www.codekid.net")
  codekid()


Decorators
==========

* A Decorator is a function that wraps another function
* code by hand

.. code-block:: python

  def hello(func):
    def callf(*args, **kwargs):
      print "Hello"
      func(*args, **kwargs)
      print "Bye"
    return callf


* with functools

.. code-block:: python

  from functools import wraps
  def my_decorator(func):
      @wraps(func)
      def wrapper(*args, **kwds):
          print 'Calling decorated function'
          return func(*args, **kwds)
      return wrapper

* http://rxwen.blogspot.com/2010/12/python-decorators.html


Memoize Decorator
==================

* Caches function results for inputs

.. code-block:: python

  def memoize(f):
      cache = {}

      @wraps(f)
      def helper(x):
          if x not in cache:
              cache[x] = f(x)
          return cache[x]
      return helper
