###
Pip
###

* Install module from git repository

.. code-block:: bash

  pip install --upgrade -e "git://server/repo.git#egg=some_name"

* Save all installed modules into file

.. code-block:: bash

  pip freeze > requirements.txt

* Install all modules from file

.. code-block:: bash

  pip install -r requirements.txt

* Config

.. code-block:: bash

  [global]
  timeout = 60

  [freeze]
  timeout = 10

  [install]
  download-cache=~/.pip/cache/
  use-mirrors = true

