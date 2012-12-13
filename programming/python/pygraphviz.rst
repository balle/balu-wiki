##########
Pygraphviz
##########

Simple example
==============

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


DOT code example
================

* DOT code

.. code-block:: python

  digraph testdriven {

  test [label="Write test", shape="box"] // some comment
  run [label="Run test", shape="oval"]
  code [label="Write code", shape="box"]
  green [label="Green", shape="oval", style="filled", color="green"]

  test->run
  run->code
  code->green
  green->test [label="Next iteration", arrowhead="normal", style="solid"]
  }

* Python code to generate image

.. code-block:: bash

  import tempfile
  import pygraphviz as pgv

  tmpfile = tempfile.NamedTemporaryFile(delete=False)
  tmpfile.write(dot_code)
  tmpfile.flush()

  graph = pgv.AGraph(tmpfile.name)
  graph.layout(prog="fdp")
  graph.draw(out_file)
  tmpfile.close()


How to test DOT code
====================

.. code-block:: bash

  dot -Tpng test.dot > output.png
