##################
Disk & filesystem
##################

List all disks
==============

.. code-block:: bash

  diskutil list


Important Filesystem Locations
==============================

============= ==========
Location      Description
------------- -----------
/Applications User installed applications
/Library      System Libraries
/Network      Network mountpoints
/System       System binaries
/Users        User home directories
/Volumes      Local mount points
/Cores        Core dumps
============= ==========


View APFS metadata
===================

.. code-block:: bash

  ls -l@
  xattr -xl
