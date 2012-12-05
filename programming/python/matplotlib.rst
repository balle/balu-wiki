###########
Matplotlib
###########

A simple line graph
===================

.. code-block:: python

  import matplotlib.pyplot as plt
  a=[1,2,3,4,5]
  b=[100,25,70,80,100]
  plt.plot(a,b)
  plt.show()


A bar graph
===========

.. code-block:: python

  import matplotlib.pyplot as plt
  a=[1,2,3,4,5]
  b=[100,25,70,80,100]
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.bar(a,b)
  plt.savefig("graph.png")


Two bar diagrams beside
=======================

.. code-block:: python

  import numpy as np
  import matplotlib.pyplot as plt

  a=[1,2,3,4,5]
  b=[100,25,70,80,100]
  c=[90,35,80,80,90]

  width=0.25
  fig = plt.figure()
  ax = fig.add_subplot(111)

  plt.bar(np.array(a), b, width, color="r")
  plt.bar(np.array(a) + width, c, width)
  plt.show()
