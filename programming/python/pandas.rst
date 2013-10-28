######
Pandas
######

Tutorials
=========

* http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
* http://pyvideo.org/video/2330/diving-into-open-data-with-ipython-notebook-pan


Parse Excel or CSV into DataFrame
=================================

.. code-block:: bash

  import pandas as pd
  # data = pd.read_excel('example.xlsx', 'sheet1')
  data = pd.read_csv("example.csv", sep=';', header=None, names=['host', 'speed', 'time'])
  print data[data.speed <= 950]


Get data from SQL
=================

.. code-block:: bash

  from pandas.io import sql
  import sqlite3

  conn = sqlite3.connect('example.sqlite3')
  query = "SELECT * FROM mytable WHERE mycol = 'MUH';"

  data = sql.read_frame(query, con=conn)
  print data.describe()


Read data from the web
======================

.. code-block:: bash

  from urllib2 import urlopen
  from StringIO import StringIO

  url = urlopen('http://www.codekid.net/data_file.txt').read()
  data = pd.read_table(StringIO(url), sep='\t')


Converter
=========

* replace all $ in salary column with nothing

.. code-block:: bash

  data = pd.read_csv('example.csv',
                     converters={'salary': lambda x: float(x.replace('$', ''))})


Selecting stuff
===============

* where

.. code-block:: bash

  print data[(data.speed <= 950) | (data.time > 0.2)]
  print data[(data.speed > 950) & (data.time < 0.2)]

* join

.. code-block:: bash

  pd.merge(left_frame, right_frame, on='key', how='inner')
  pd.merge(left_frame, right_frame, on='key', how='left')
  pd.merge(left_frame, right_frame, on='key', how='right')


Merging
=======

.. code-block:: bash

  data_full = pd.concat([data, data_set2])
  data_full = pd.merge(data, data_set2)


Aggregation
===========

* Group data by column title
* Run np.size and np.mean functions on column rating

.. code-block:: bash

  data.groupby('title').agg({'rating': [np.size, np.mean]})


Graphing
========

.. code-block:: bash

  import pandas as pd
  import matplotlib.pyplot as plt

  data = pd.read_excel('example.xlsx', 'sheet1')
  data.set_index("name", inplace=True)
  plt.figure()
  plt.title("Just a simple test")
  data.plot(kind="barh")
  plt.show()
