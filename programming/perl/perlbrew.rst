########
Perlbrew
########

List perl versions
==================

.. code-block:: bash

  perlbrew available


Install a new interpreter
=========================

.. code-block:: bash

  perlbrew install perl-5.17.10


Use new interpreter
===================

.. code-block:: bash

  perlbrew list
  perlbrew use perl-5.17.10


Switch default interpreter
==========================

.. code-block:: bash

  perlbrew switch perl-5.17.10


Upgrade to latest perl version
==============================

.. code-block:: bash

  perlbrew upgrade-perl


Create virtualenv
=================

.. code-block:: bash

  perlbrew lib create <name>
  perlbrew use @<name>


Install modules in virtualenv
=============================

.. code-block:: bash

  perlbrew use @<virtualenv>
  perlbrew install-cpanm
  cpanm <module>
  
