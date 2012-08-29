####
CSS3
####

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
  
