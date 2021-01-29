############
Base system
############

Set clock to localtime
======================

.. code-block:: bash

  ln -sf /usr/share/zoneinfo/right/CET /etc/localtime
  rdate -ncv time.fu-berlin.de

  
UTF-8 system-wide
=================

.. code-block:: bash

  echo 'export LC_ALL="en_US.UTF-8"' >> /etc/profile
  echo 'export LC_ALL="en_US.UTF-8"' >> ~/.xsession


Adjust max memory size
======================

* Edit /etc/login.conf

.. code-block:: bash

  :datasize-max=1024M:\
  :datasize-cur=1024M:\

* Or set `infinity:` as value


Automatically adjust cpufreq
=============================

* Edit /etc/rc.conf.local

.. code-block:: bash

  apmd_flags="-A"

  
Ksh config
==========

* ~/.kshrc

.. code-block:: bash

  export PS1='\[\t\] \u@\h:\w\$ '
  export EDITOR=/usr/bin/mg

  set -o emacs

  alias cp='cp -i'
  alias mv='mv -i'
  alias rm='rm -i'

* If you use tmux or screen put the following into ~/.profile

.. code-block:: bash

  export ENV=~/.kshrc



Login using Google authenticator or freeotp
============================================

.. code-block:: bash

  pkg_add login_oath

* Edit `/etc/login.conf`

.. code-block:: bash

  otp:\
        :auth=-totp-and-pwd:\
        :tc=default:

* Change users login class

.. code-block:: bash

  usermod -L otp username

* Generate random key

.. code-block:: bash

  openssl rand -base64 20 > ~/.totp-key
  chmod 700 /home/username
  chmod 700 /home/username/.totp-key
