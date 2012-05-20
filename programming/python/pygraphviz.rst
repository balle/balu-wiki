##########
Pygraphviz
##########

.. code-block:: python

  import pygraphviz as pgv
  
  G=pgv.AGraph(strict=False,directed=True, rankdir = "LR")
  
  test1 = "Test 1"
  test2 = "Test 2"
  test3 = "Test 3"
  test4 = "Test 4"
  
  G.add_node(test1)
  G.add_node(test2)
  G.add_node(test3)
  G.add_node(test4)
  
  G.add_edge(test1, test2)
  G.add_edge(test2, test3)
  G.add_edge(test2, test4)
  
  e = G.get_edge(test2, test3)
  e.attr["label"] = "no"
  
  e = G.get_edge(test2, test4)
  e.attr["label"] = "yes"
  
  G.node_attr['shape']='box'
  G.node_attr['style']='filled'
  G.node_attr['fillcolor']='grey'
  
  G.layout("dot")
  G.draw('graph.png')


