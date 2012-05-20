#######
Screen
#######

Basics 
=======

* ctrl+a c - new window
* ctrl+a n - next window
* ctrl+a p - previous window
* ctrl+a a - last window
* ctrl+a <nr> - switch to window <nr>
* ctrl+a A - rename window
* ctrl+a k - kill window

Splitting 
==========

* ctrl+a S - split window
* ctrl+a tab - switch between splittet screens
* ctrl+a X - close window

Detatching 
===========

* ctrl+a d - detach
  screen -r # attach
* ctrl+a x - lock screen


Copy & paste 
=============

* ctrl+a esc - get into copy mode
* space - set marker begin / end
* W - mark whole word
* Y - mark whole line
* ctrl+a ] - paste


Searching 
==========

* ctrl+a esc - get into copy mode
* ctrl+r - search backward
* ctrl+s - search forward


Example .screenrc 
==================

.. code-block:: bash

  startup_message off
  vbell on
  autodetach on
  defscrollback 10000

  bindkey -m ' ' eval 'msgwait 0' 'stuff \040' writebuf 'exec !!! xclip /tmp/screen-exchange' 'msgwait 2'
  bindkey -m Y eval 'msgwait 0' 'stuff Y' writebuf 'exec !!! xclip /tmp/screen-exchange' 'msgwait 2'
  bindkey -m W eval 'msgwait 0' 'stuff W' writebuf 'exec !!! xclip /tmp/screen-exchange' 'msgwait 2'

  bind r eval 'echo "Resize window"' 'command -c resize'""
  bind -c resize "+" eval 'resize +1' 'command -c resize'
  bind -c resize "-" eval 'resize -1' 'command -c resize'

  caption always  "%{=b kw} $LOGNAME@%H %c %D %d/%m/%Y %{=b kr}|%{-} %l %u %{=b kr}|%{-} %-Lw%{=b kr} %50>%n%f*%t %{-}%+Lw%<"


