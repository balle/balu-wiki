#####
Tmux
#####

Tmux ist ein Terminal Multiplexer wie screen und wird unter OpenBSD entwickelt.

Um sich zu einem screen zu attaachen kann der Befehl 

.. code-block:: bash

   tmux attach -t sessionid or name

benutzt werden. Wird keine Session mitgegeben öffnet sich die letzt Sitzung.

Um Tmux bei starten der Shell mit zu starten, kann in die .zshrc oder die .bshrc folgende Zeile eigetragen werden.

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
* ctrl + b   x -> delete current pane
* Ctrl + b   o    -> switch panel
* Ctrl + b   [    -> switch to buffer (like emacs)
* Ctrl + Space    -> set marker
* Ctrl + w        -> cut region
* Alt  + w        -> copy region
* Esc             -> leave buffer
* Ctrl + b   ]    -> past copied buffer
* ctrl + space    -> toggle different pane layouts
* ctrl + b : resize-pane -D 20 -> shrink down
* ctrl + b : resize-pane -U 20 -> shrink up
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
    bind-key -n M-d set-window-option synchronize-panes off
    bind-key -n M-c set-window-option synchronize-panes on

    # Reload key
    bind r source-file ~/.tmux.conf

    set -g default-terminal "screen-256color"
    set -g history-limit 10000
    set -g status-interval 1

    #--Status-Bar-------------------------------------------------------------------
    # Default colors
    set -g status-bg black
    set -g status-fg white

    # Left side of status bar
    set -g status-left-length 20
    set -g status-left ''
    #set -g status-left '#[fg=green][#[bg=black,fg=cyan]#S#[bg=black,fg=blue,dim]:#H#[fg=green]]'

    # Inactive windows in status bar
    set-window-option -g window-status-format '#[fg=cyan,dim]#I#[fg=blue]:#[default]#W#[fg=grey,dim]#F'

    # Current or active window in status bar
    set-window-option -g window-status-current-format '#[bg=blue,fg=cyan,bold]#I#[bg=blue,fg=cyan]:#[fg=white]#W#[fg=dim]#F'

    # Alerted window in status bar. Windows which have an alert (bell, activity or content).
    #set-window-option -g window-status-alert-fg red
    #set-window-option -g window-status-alert-bg white

    # right side of statusbar
    set -g status-right-length 50
    set -g status-right '#[fg=yellow]#(cut -d " " -f 1-3 /proc/loadavg)#[default] #[fg=green]#(whoami)@#h#[default] #[fg=blue]%H:%M:%S %d/%m#[default]'


    # on more way to set the statusbar
    set -g status-interval 1
    set -g status-justify centre # center align window list
    set -g status-left-length 12
    set -g status-left '#S #(whoami)@#h'
    set -g status-right-length 14
    set -g status-right '%H:%M:%S %d/%m'

    # bind arrow keys
    bind-key -n C-left previous-window
    bind-key -n C-right next-window
    bind-key -n C-up select-pane -t :.+
    bind-key -n C-down new-window

    # Set the prefix to Alt-A
    set-option -g   prefix M-a
    bind-key M-a    send-prefix


    # some more nice options
    set-option -g   bell-action any
    set-option -g   default-terminal screen
    set-option -g   display-panes-colour red
    set-option -g   history-limit 100000
    set-option -g   message-bg red
    set-option -g   message-fg white
    set-option -g   mouse-select-pane off
    set-option -g   pane-active-border-bg default
    set-option -g   pane-active-border-fg red
    set-option -g   pane-border-bg default
    set-option -g   pane-border-fg cyan
    set-option -g   repeat-time 500
    set-option -g   visual-activity off
    set-option -g   visual-bell on
    set-option -g   set-titles on
    set-option -g   set-titles-string ' #I-#W '
    set-option -g   terminal-overrides 'zsh*:smcup@:rmcup@'
    set-option -g   base-index 1
    set-option -g   default-path ""

    # browsing urls
    bind-key u capture-pane \; save-buffer /tmp/tmux-buffer \; new-window -n "urlview" '$SHELL -c "urlview < /tmp/tmux-buffer"'
    
    # pane movement
    bind-key j command-prompt -p "join pane from:"  "join-pane -s '%%'"
    bind-key s command-prompt -p "send pane to:"  "join-pane -t '%%'"

    # pane resize
    bind-key C-u resize-pane -U     # Resize window up              (Ctrl+b, u) (i.e., hold Ctrl and alternate hitting 'b' and 'u')
    bind-key C-d resize-pane -D     # Resize window down            (Ctrl+b, d) (similar)
    bind-key C-l resize-pane -L     # Resize window left            (Ctrl+b, l) (similar)
    bind-key C-r resize-pane -R     # Resize window right           (Ctrl+b, r) (similar)

    # copy & paste
    bind -n M-w run "tmux show-buffer | xclip -i -selection clipboard"
    
