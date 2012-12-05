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
