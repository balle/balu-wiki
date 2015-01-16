######
Erlang
######

Setup a cluster on a LAN
=========================

* Make sure UDP / TCP port 4369 is open

.. code:: bash

  erl -name muh -setcookie somesecret
  erl -name maeh -setcookie somesecret


Setup a cluster over SSH
========================

* On master node (make sure your user can connect to the slaves by passwordless ssh key e.g. ssh-copy-id)

.. code:: bash

  erl -rsh ssh -sname master

* Compile and load cluster module on master

.. code:: erlang

  -module(cluster).
  -export([slaves/1]).
  
  slaves([]) -> ok;
  slaves([Host|Hosts]) ->
      {ok, Node} = slave:start_link(Host, "slave", "-rsh ssh"),
      io:format("Erlang node started = [~p]~n", [Node]),
      slaves(Hosts).

* Start the cluster from master node

.. code:: bash

  erl> cluster:slaves(["node1", "node2", "node3"]).


List all processes
==================

.. code:: bash

  i().
  regs().


List all connected nodes
========================

.. code:: bash

  nodes().


Spawn process on remote node
============================

.. code:: erlang

  rpc:spawn(Node, Mod, Fun, Args).


Call function on remote node
============================

.. code:: erlang

  rpc:call(Node, Pid, Fun, Args).


Call a function on all connected nodes
======================================

.. code:: erlang 

  rpc:multicall(nodes(), Mod, Fun, Args).


Concurrent program template
===========================

.. code:: erlang

  -module(ctemplate).
  -compile(export_all).

  start() -> spawn(ctemplate, loop, []).

  rpc(Pid, Request) -> 
      Pid ! {self(), Request},
      receive
          {Pid, Response} -> Response.
      end.

  loop() ->
      receive
          Any ->
              io:format("Help me do something"),
              loop()
       end.
