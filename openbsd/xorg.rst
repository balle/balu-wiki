#####
Xorg
#####

Configure keyboard layout
=========================

* Create file /etc/X11/xorg.conf.d/keyboard.conf

.. code-block:: bash

  Section "InputClass"
      Identifier "keyboard"
      MatchIsKeyboard "yes"
      Option "XkbLayout" "us"
      Option "XkbVariant" "nodeadkeys"
      Option "XkbVariant" "altgr-intl"
  EndSection


Configure touchpad
===================

* Create file /etc/X11/xorg.conf.d/synaptics.conf

.. code-block:: bash

  Section "InputClass"
    Identifier "touchpad"
    Driver "synaptics"
    MatchIsTouchpad "on"
    Option "VertEdgeScroll" "on"
    Option "VertTwoFingerScroll" "on"
    Option "HorizEdgeScroll" "on"
    Option "HorizTwoFingerScroll" "on"
  EndSection


Add a second monitor
====================

* Scan for devices

.. code-block:: bash

  xrandr -q

* Add the second monitor temporarly right of the firt one

.. code-block:: bash

  xrandr --output HDMI-1 --right-of eDP-1 --mode 1920x1080

* Or make it permanent by adding a file in /etc/X11/xorg.conf.d/ with the following content

.. code-block:: bash

  Section "ServerLayout"
      Identifier     "X.org Configured"
      Screen      0  "Screen0" 0 0
      Screen      1  "Screen1" RightOf "Screen0"
      Option         "Xinerama" "true"
  EndSection


Mirror displays
===============

.. code-block:: bash

  xrandr --output eDP-1 --mode 1920x1080 --output HDMI-1 --mode 1920x1080 --same-as eDP-1


Fix arrow keys in Emacs under Xorg
==================================

.. code-block:: lisp

  (if (not window-system)                        ;; Only use in tty-sessions.
    (progn
      (defvar arrow-keys-map (make-sparse-keymap) "Keymap for arrow keys")
      (define-key esc-map "[" arrow-keys-map)
      (define-key arrow-keys-map "A" 'previous-line)
      (define-key arrow-keys-map "B" 'next-line)
      (define-key arrow-keys-map "C" 'forward-char)
      (define-key arrow-keys-map "D" 'backward-char)))


