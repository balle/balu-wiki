################
Shell Scripting
################

Quote Spaces in Filenames 
==========================

.. code-block:: bash

  echo $FILE | sed 's/ /\\ /g'
