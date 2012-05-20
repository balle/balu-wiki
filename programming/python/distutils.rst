###########
Distutils
###########

Simple example 
===============

.. code-block:: python

  from distutils.core import setup

  CLASSIFIERS = [
        'Development Status :: 5 - Production/Stable',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                'Topic :: Software Development',
                'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]

  setup(name="myproject",
      version="1.0",
      description="some description",
      author="me",
      packages=["mypackage"],
      scripts=["myscript"],
      install_requires=["some_module>=version"],
  )


Complex example 
=================

.. code-block:: python

  import os
  import sys
  from distutils.command.build_py import build_py as _build_py
  from distutils.core import setup
  from distutils.dir_util import copy_tree


  class build_py(_build_py):
    setup(name="myproject",
      version="1.0",
      description="some description",
      author="me",
      packages=["mypackage"],
  )

    copy_tree("dir_of_dirs", os.path.join(sys.prefix, "share", "foo", "bar"), update=1, verbose=1)
