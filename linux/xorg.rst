####
Xorg
####

Dual View / Beamer
==================

* Via config

.. code-block:: bash

  Section "ServerLayout"
	Identifier     "X.org Configured"
	Screen      0  "Screen0" 0 0
	Screen      1  "Screen1" RightOf "Screen0"
        Option         "Xinerama" "true"
  EndSection

* Or command

.. code-block:: bash

  xrandr --output HDMI2 --right-of eDP1 --mode 1920x1200
  

Nvidia Xorg config
==================

* Install nvidia driver and tools
* Use nvidia-xconfig
* Use nvidia driver not nv


Add new resolution
==================

.. code-block:: bash

  $ cvt 1024 600
  # 1024x600 59.85 Hz (CVT) hsync: 37.35 kHz; pclk: 49.00 MHz
  Modeline "1024x600_60.00"   49.00  1024 1072 1168 1312  600 603 613 624 -hsync +vsync
  $ xrandr --newmode "1024x600"   49.00  1024 1072 1168 1312  600 603 613 624 -hsync +vsync
  $ xrandr --addmode default "1024x600"

* To activate the new mode execute

.. code-block:: bash

  xrandr --output eDP1 --mode 1280x720
  

Keyboard config for German layout
==================================

* Paste into /etc/X11/xorg.conf.d/10-keyboard.conf

.. code-block:: bash

  Section "InputClass"
        Identifier "keyboard"
        MatchIsKeyboard "yes"
        Option "XkbLayout" "de"
        Option "XkbVariant" "nodeadkeys"
  EndSection


Change Keyboardlayout to dvorak
================================

* setxkbmap dvorak
* setxkbmap de -variant dvorak

  
Learn dvorak
============

.. image:: http://ulf.zeitform.de/images/dvorak.png

* http://learn.dvorak.nl
