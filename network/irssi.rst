#####
Irssi
#####

Auto join
=========

.. code-block:: bash

  /SERVER ADD -auto -network Freenode irc.freenode.net
  /NETWORK ADD -autosendcmd "/^nick yourname;/^msg nickserv identify passwordgoeshere;wait 2000" Freenode
  /CHANNEL ADD -auto #emacs Freenode


Shortcuts 
=========

* alt + 1-0 -> change window


Commands 
=========

* /names -> list users of channel
* /window new split
* /window shrink / grow <lines>
* /wc -> close window
* /go <nick/channel> - jump to the specified nick or channel


ICQ / Jabber integration
========================

  * install and configure bitlbee


Plugins
=======

* bitlbee_join_notice.pl  
* bitlbee_typing_notice.pl  
* go.pl  
* hilightwin.pl  
* trackbar.pl  
* urlgrab.pl
* notify - https://raw.github.com/lmacken/irssi-libnotify/master/notify.pl
