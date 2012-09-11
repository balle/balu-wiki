####
Xorg
####

Dual View
=========

.. code-block:: bash

  Section "ServerLayout"
	Identifier     "X.org Configured"
	Screen      0  "Screen0" 0 0
	Screen      1  "Screen1" RightOf "Screen0"
        Option         "Xinerama" "true"
  EndSection

  
Change Keyboardlayout
======================

* setxkbmap dvorak
* setxkbmap de -variant dvorak

Learn dvorak
============

.. image:: http://ulf.zeitform.de/images/dvorak.png

* http://learn.dvorak.nl
