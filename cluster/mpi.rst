###
MPI
###

Overview
========

* MPI is an parallel programming API to execute processes over multiple cores / computers
* Possible implementations are openmpi or mpich2
* Remote processes can be e.g. executed via torque, slurm or ssh

.. code-block:: bash

  mpirun --hostfile my_hostfile -np 4 my_parallel_application

* http://mpitutorial.com/tutorials/


Terminology
============

* A communicator defines a group of processes
* Each process in a group has a unique rank
* An optional tag can be used to uniquely identify a message 

  
Python source sample
=====================

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
