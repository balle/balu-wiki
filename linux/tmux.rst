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

* Strg + b   d    -> dettach
* Strg + b   c    -> new window
* Strg + b   0    -> goto window 0
* Strg + b   "    -> split window V
* Strg + b   %    -> split window horizontal in 2 pannel spliten 
* Strg + b   w    -> show windowlist
* Strg + b   !    -> close all window
* Strg + b   n    -> next window
* Strg + b   p    -> privios window
* Strg + b   l    -> last window
* Strg + b   ,    -> rename window
* Strg + d        -> delete window
* strg + b   x -> delete current pane
* Strg + b   o    -> switch panel
* Strg + b   [    -> switch to buffer (like emacs)
* Strg + Space    -> set marker
* Strg + w        -> cut region
* Alt  + w        -> copy region
* Esc             -> leave buffer
* Strg + b   ]    -> past copied buffer
* strg + b : resize-pane -D 20 -> shrink down
* strg + b : resize-pane -U 20 -> shrink up
* strg + b : break-pane -> convert pane to window
* strg + b : source-file ~/.tmux.conf -> reload config


Balle Config 
=============

.. code-block:: bash

    #!/bin/bash

    # Make it use C-a, similar to screen..
    unbind C-b
    unbind l
    set -g prefix C-a
    bind-key C-a last-window

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
    set-window-option -g window-status-alert-fg red
    set-window-option -g window-status-alert-bg white

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

    # pane movement
    bind-key j command-prompt -p "join pane from:"  "join-pane -s '%%'"
    bind-key s command-prompt -p "send pane to:"  "join-pane -t '%%'"

    # pane resize
    bind-key C-u resize-pane -U     # Resize window up              (Ctrl+b, u) (i.e., hold Ctrl and alternate hitting 'b' and 'u')
    bind-key C-d resize-pane -D     # Resize window down            (Ctrl+b, d) (similar)
    bind-key C-l resize-pane -L     # Resize window left            (Ctrl+b, l) (similar)
    bind-key C-r resize-pane -R     # Resize window right           (Ctrl+b, r) (similar)

