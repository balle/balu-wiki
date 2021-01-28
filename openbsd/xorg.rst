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

* Create file

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


