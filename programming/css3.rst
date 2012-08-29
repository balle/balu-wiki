####
CSS3
####

Rounded corners
===============

.. code-block:: css

  input {
    border-radius: 5px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
  }


Box Shadow
==========

.. code-block:: css

  #content {
    -moz-box-shadow: 5px 5px 5px #ccc;
    -webkit-box-shadow: 5px 5px 5px #ccc;
    -o-box-shadow: 5px 5px 5px #ccc;
    -box-shadow: 5px 5px 5px #ccc;
  }


Text Shadow
===========

.. code-block:: css

  #content {
    text-shadow: 2px 2px 2px #ccc;
  }


Rotations
=========

.. code-block:: css

  #content {
    -moz-transform: rotate(-2.3deg)
    -o-transform: rotate(-2.3deg)
    -webkit-transform: rotate(-2.3deg)
    -ms-transform: rotate(-2.3deg)
    -transform: rotate(-2.3deg)
  }


Transparency
============

.. code-block:: css

  #content {
     background-color: rgba(255, 255, 255, 0.80)
  }

  
Striped tables
==============

.. code-block:: css

  tr:nth-of-type(even) {
    background-color: white;
  }

  tr:nth-of-type(odd) {
    background-color: black;
  }

  
Last line bold
==============

.. code-block:: css

  tr:last-child {
    font-weight: bolder;
  }


Two column content
==================

.. code-block:: css

  #content {
    -moz-column-count: 2;
    -webkit-column-count: 2;
    -moz-column-gap: 20px;
    -webkit-column-gap: 20px;
  }
  

