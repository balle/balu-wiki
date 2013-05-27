###
MPI
###

Overview
========

* MPI is an parallel programming API to execute processes over multiple cores / computers
* You must install mpich2 and run ``mpd``
* Remote processes are usually executed via ssh


Source sample
=============

* pip install mpi4py
* Run with ``mpiexec -n 4 ./test.py``

.. code-block:: python

  #!/usr/bin/python

  from mpi4py import MPI

  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()

  print "Hello world from process ", rank, " of ", comm.Get_size(), " processes"

  if rank == 1:
    data = [1, 5, 7, 13]
    comm.send(data, dest=0, tag=11)
    print rank, " sending data to process 0"

  elif rank == 0:
    data = comm.recv(source=1, tag=11)
    print rank, " got ", data
    comm.bcast("thanks for all the fish!", root=0)
