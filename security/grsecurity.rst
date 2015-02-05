###########
Grsecurity
###########

Activate RBAC
=============

.. code:: bash

  gradm -P
  gradm -P admin
  gradm -P shutdown
  gradm -E
  

Learn policy for special program
================================

* Add the following to ``/etc/grsec/policy``

  .. code:: bash

  subject /path/of/binary ol
      / h
      -CAP_ALL
      connect disabled
      bind disabled

* Start learning mode

 .. code:: bash

  gradm -L /etc/grsec/learning.logs -E

* Switch to admin role and dump learning.log to policy.new

 .. code:: bash

  gradm -a admin
  gradm -L /etc/grsec/learning.logs -O /etc/grsec/policy.new

* Review policy.new, add it to policy and reload it

 .. code:: bash

  gradm -R

* Leave admin role

  .. code:: bash

  gradm -u


Explenation of PaX flags
========================

========== ======================
Flax       Description
---------- ----------------------
PAX_NOEXEC This option enables the protection of allocated pages of memory as non-executable if they are not part of the text segment of the running process. It is needed for PAGEEXEC, SEGMEXEC and KERNEXEC.
PAGEEXEC The kernel will protect non-executable pages based on the paging feature of the CPU. This is sometimes called "marking pages with the NX bit" in other OSes. This feature can be controlled on a per ELF object basis by the PaX P and p flags.
SEGMEXEC This is like PAGEEXEC, but based on the segmentation feature of the CPU and it is controlled by the PaX S and s flags. Note that SEGMEXEC is only available on CPUs that support memory segmentation, namely x86.
EMUTRAMP The kernel will emulate trampolines (snippets of executable code written on the fly) for processes that need them, e.g. nested functions in C and some JIT compilers. Since trampolines try to execute code written by the process itself to memory marked as non-executable by PAGEEXEC or SEGMEXEC, the PaX kernel would kill any process that tries to make use of one. EMUTRAMP allows these processes to run without having to fully disable enforcement of non-executable memory. This feature can be controlled on a per ELF object basis by PaX E and e flag.
MPROTECT The kernel will prevent the introduction of new executable pages into the running process by various techniques: it will forbid the changing of the executable status
RANDMMAP The kernel will use a randomized base address for mmap() requests that do not specify one via the MAP_FIXED flag. It is controlled by the PaX R and r flags.
========== ======================
