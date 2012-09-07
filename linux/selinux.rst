#######
SELinux
#######

Update policy
=============

.. code-block:: bash

  grep qemu-system-x86 /var/log/audit/audit.log | audit2allow -M mypol
  semodule -i mypol.pp
