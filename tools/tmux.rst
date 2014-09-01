#####
Tmux
#####

Overview
========

Tmux is a terminal multiplexer like screen.

To attach to a running tmux session type

.. code-block:: bash

   tmux attach -t sessionid or name

If no session exists a new one will be created.

To start Tmux togehter with your shell you can put the following into your .zshrc or .bashrc

.. code-block:: bash

   [[ $TERM != "screen" ]] \&\& tmux \&\& exit


Shortcuts
==========

* Ctrl + b   d    -> dettach
* Ctrl + b   c    -> new window
* Ctrl + b   0    -> goto window 0
* Ctrl + b   "    -> split window V
* Ctrl + b   %    -> split window horizontal in 2 pannel spliten
* Ctrl + b   w    -> show windowlist
* Ctrl + b   !    -> close all window
* Ctrl + b   n    -> next window
* Ctrl + b   p    -> previous window
* Ctrl + b   l    -> last window
* Ctrl + b   ,    -> rename window
* Ctrl + b   k    -> delete window
* ctrl + b   x    -> delete current pane
* Ctrl + b   o    -> switch panel
* ctrl + b up/down -> switch to panel up/down
* ctrl + b q <nr> -> show panel numbers and switch to it directly
* ctrl + b !      -> move current pane to new window
* ctrl + b s      -> send pane to other window
* Ctrl + b   [    -> switch to buffer (like emacs)
* Ctrl + Space    -> set marker
* Ctrl + w        -> cut region
* Alt  + w        -> copy region
* Esc             -> leave buffer
* Ctrl + b   ]    -> paste last copied buffer
* ctrl + b =      -> choose paste buffer
* ctrl + b : capture-pane -> copy all visible pane output
* ctrl + b : save-buffer -> write paste buffer to file
* ctrl + space    -> toggle different pane layouts
* ctrl + b : resize-pane -D 20 -> shrink down
* ctrl + b : resize-pane -U 20 -> shrink up
* ctrl + b <left/right/up/down> -> resize current pane to left/right/up/down
* ctrl + b : break-pane -> convert pane to window
* ctrl + b : source-file ~/.tmux.conf -> reload config


Session handling
================

* Create a new session named muh

.. code-block:: bash

  tmux new -s muh

* List all sessions

.. code-block:: bash

  tmux ls

* Attach to a session

.. code-block:: bash

  tmux attach -t <session-name>

* Detach from a session with Ctrl b + d

* Kill a session

.. code-block:: bash

  tmux kill-session -t <name-or-number>


Scripting
=========

.. code-block:: bash

  #!/bin/bash

  for IP in {1..96}; do
    tmux select-layout tiled
    tmux split-window -h
    tmux send-keys "ssh root@192.168.1.$IP" C-m
    tmux send-keys "top" C-m
  done


Synchronous input
=================

* ctrl + b : synchronize-panes


Getting help
============

ctrl b ? - show keys
ctrl b : list-commands


Balle Config
=============

.. code-block:: bash

  #!/bin/bash

  # Make it use C-a, similar to screen..
  unbind C-b
  unbind l
  set -g prefix C-a
  bind-key C-a last-window
  bind-key k kill-window
  bind-key -n C-M-d set-window-option synchronize-panes off
  bind-key -n C-M-c set-window-option synchronize-panes on

  # Reload key
  bind r source-file ~/.tmux.conf

  set -g default-terminal "screen-256color"
  set -g history-limit 100000
  set -g status-interval 1

  #--Status-Bar-------------------------------------------------------------------
  # Default colors
  set -g status-bg black
  set -g status-fg white

  # Left side of status bar
  set -g status-left-length 20
  set -g status-left ''
  #set -g status-left '#[fg=green][#[bg=black,fg=cyan]#S#[bg=black,fg=red,dim]:#H#[fg=green]]'

  # Inactive windows in status bar
  set-window-option -g window-status-format '#[fg=cyan,dim]#I#[fg=blue]:#[default]#W#[fg=grey,dim]#F'

  # Current or active window in status bar
  set-window-option -g window-status-current-format '#[bg=red,fg=cyan,bold]#I#[bg=red,fg=cyan]:#[fg=white]#W#[fg=dim]#F'

  # Alerted window in status bar. Windows which have an alert (bell, activity or content).
  #set-window-option -g window-status-alert-fg red
  #set-window-option -g window-status-alert-bg white

  set -g status-right-length 50
  set -g status-right '#[fg=yellow]#(cut -d " " -f 1-3 /proc/loadavg)#[default] #[fg=green]#(whoami)@#h#[default] #[fg=blue]%H:%M:%S %d/%m#[default]'

  # enable activity alerts
  setw -g monitor-activity on
  set -g visual-activity on

  # resize screen only for active clients
  setw -g aggressive-resize on

  bind-key C-s set-window-option synchronize-panes

  # bind arrow keys
  bind-key -n C-up select-pane -t :.+
  bind-key -n C-down new-window

  bind-key | split-window -h
  bind-key - split-window -v

  # pane movement
  bind-key j command-prompt -p "join pane from:"  "join-pane -s '%%'"
  bind-key s command-prompt -p "send pane to:"  "join-pane -t '%%'"

  # pane resize
  bind-key C-u resize-pane -U     # Resize window up              (Ctrl+b, u) (i.e., hold Ctrl and alternate hitting 'b' and 'u')
  bind-key C-d resize-pane -D     # Resize window down            (Ctrl+b, d) (similar)
  bind-key C-l resize-pane -L     # Resize window left            (Ctrl+b, l) (similar)
  bind-key C-r resize-pane -R     # Resize window right           (Ctrl+b, r) (similar)

  # browsing urls
  bind-key u capture-pane \; save-buffer /tmp/tmux-buffer \; new-window -n "urlview" '$SHELL -c "urlview < /tmp/tmux-buffer"'

  # Screen lock
  bind-key C-x   lock-server
  set-option -g   lock-after-time 0
  set-option -g   lock-server on
  #set-option -g   lock-command "vlock"

  # better copy & paste
  bind-key C-c run "tmux save-buffer - | xclip -i sel clipboard"
  bind-key C-v run "tmux set-buffer \"$(xclip -o sel clipboard)\"; tmux paste-buffer"
  bind-key C-y paste-buffer
  bind-key M-y choose-buffer

  # plugins
  #set -g @tpm_plugins "              \
  #  tmux-plugins/tpm                 \
  #  tmux-plugins/tmux-copycat        \
  #  tmux-plugins/tmux-yank          \
  #  tmux-plugins/tmux-open          \
  #"
  #run-shell ~/.tmux.d/tpm/tpm


* For browsing urls in firefox edit ``~/.urlview``

.. code-block:: bash

  COMMAND exec >> /tmp/urlview.out 2>&1; set -x; firefox


Tmux plugins
=============

* https://github.com/tmux-plugins
