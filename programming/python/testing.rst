########
Testing
########

Testing with unittest
=====================

.. code-block:: Python

  class MyTests(unittest.TestCase):
    def setUp(self):
        self.some_value = 23

    def test_addition(self):
        self.assertEqual(2 + self.some_value, 25)

   def test_exception(self):
     with self.assertRaises(ValueError):
         raise ValueError()


Testing with nose
=================

* Nose can use unittest tests but you want do more with nose tests

.. code-block:: Python

  my Tests():
    def setup(self):
      self.some_value = 23

    # assumes function runs without failure
    def test_addition(self):
      assert self.some_value + 2 == 25

    def test_addition_with_nose(self):
      import nose
      nose.tools.assert_equals(self.some_value + 2, 25)

    @raises(ValueError)
    def test_exception(self):
      raise ValueError()


* use nosy to automatically run all tests if code changes

.. code-block:: bash

  pip install nosy
  nosy

* check code coverage of your unittests

.. code-block:: bash

  pip install coverage
  nosetests --with-coverage

* testing performance

.. code-block:: Python

  # test fails if it runs longer than 0.2 seconds
  @timed(0.2)
  def test_something():
    pass

* run profiler on every tested unit

.. code-block:: bash

  nosetests --with-profile


* get a pdb on test failures

.. code-block:: bash

  nosetests --pdb-failures

* get output in xUnit format (usefull for e.g. Jenkins)

.. code-block:: bash

  nosetests --with-xunit --xunit-file=testresults.xml

* Integrate nose into setuptools

.. code-block:: python

  setup (
    # ...
    test_suite = 'nose.collector'
  )


Doctests
========

* Use nose to run Doctests

.. code-block:: Python

  def some_function(a, b):
      """
      >>> some_function(2, 3)
      5
      """
      return a + b

.. code-block:: bash

  nosetests --with-doctest


Mocking
=======

* Using nose and mock

.. code-block:: Python

  @mock.patch('some_module.nasty_method', lambda x: True)
  def test_nasty_method():
    assert some_module.nasty_method()

* Using mock without nose

.. code-python:: Python

  from mock import Mock

  m = SomeModule()
  m.nasty_method = Mock(return_value=42)

* Using flexmock

.. code-python:: Python

  flexmock(SomeObject).should_receive('some_method').and_return('some', 'values')
