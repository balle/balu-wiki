###
Zsh
###

History
========

* !13 -> ruft den 13 Befehl der History aus
* !-1 -> genau wie !!-> ruft den gesamten letzten Befehl auf
* !-2 -> ruft den vorletzten Befehl auf usw.
* !:2 -> ruft nur das 2 Argument des letzten Befehls auf
* !:2:h -> ruft den vorderen Teil des letzten Arguments auf
* !-2:2:t -> ruft den hinteren Teil des vorletzten Befehls auf
* !:2:r.pdf -> ändert das Suffix des letzten Befehls (z.B txt) in pdf
* !!:s/z/y/ -> ändere im letzten Befehl das ERSTE z in y
* !!:gs/z/y/ -> ändere im letzten Befehl ALLE z in y
* history -D -> zeigt letzten Befehle an mit Nummer und Startzeit
* history -40 -20 -> zeigt alle letzten Eintrage zwischen dem 20 - 40
* !ca -> letzter Befehl der mit ca anfing z.B cal 12 2011
* !?pwd -> sucht nach dem letzten Befehl in dem pwd vorkam und führt ihn aus
* ``history -EDd`` shows history with timestamps and how long a command had run

* vom letzten Befehl bestimmte Zeichen löschen oder ersetzen

.. code-block:: bash

  cal 1222 2011

* ^12 	      -> ruft cal 12 2011 auf
* ^cal^echo     -> ersetzt das erste cal mit echo und gibt 12 2011 in stdout aus

* Pfade wiederverwenden

.. code-block:: bash

  ls /usr/local/src
  !!/blub		 -> ls /usr/local/src/blub		-> Wiederverwendung des gesamten letzten Befehls und hängt
                                                                   hinten "blub" an
  cp !$/something .      -> cp /usr/local/blub/something .      -> wiederverwenden des letzten Arguments des letzten Befehls


Output redirect
================

* cat bla > file.txt > error.txt->  redirect  output to file.txt and errors to error.txt
* cat bla >| filename ->  redirect  output to File nur wenn diese NICHT existiert
* mehrere Pfade /Dateien  hintereinander ausgeben

.. code-block:: bash

  ls /etc /bin /usr -> gibt hintereinander /etc dann /bin dann /usr aus
  cp file file0 file1 file3 /home  -> kopiert alle Dateien nach /home

* nach dem Anfang oder Ende eines Befehls oder Datei  suchen

.. code-block:: bash

  ls /usr/bin /bin | grep 'sh$'     -> findet alle Dateien die mit sh Enden in /usr/bin und /bin
  ls /home | grep  test* 		  -> findet alle Dateien mit dem Anfang test im /home

* alles in einem Verzeichnis ausgeben bis auf gestimmte Sachen

.. code-block:: bash

  ls /usr/bin /bin | grep -v 'sh$'      -> gibt alles in den Verzeichnissen /usr/bin und /bin aus bis auf das was mit sh endet

* Sachen sortiert ausgeben mit sort

.. code-block:: bash

  ls /usr/bin /bin | grep 'sh$' | sort	-> gibt die Dateien von a - z sortiert aus

* Ausgabe in mehrere Spalten mit column

.. code-block:: bash

  ls /usr/bin /bin | grep 'sh$'| column	-> gibt die Dateien in so vielen Spalten wie auf den Bildschirm passen aus

* im Befehl cat kann die Spalten Anzahl mitten -c angeben werden

.. code-block:: bash

  cat -c 1-3 bla 	   -> Ausgabe von bla in 3 Spalten

* lange Befehleketten können mittels \newline unterteilt werden

.. code-block:: bash

  ls /usr/bin /bin | \
  grep 'sh$' | \
  sort | \
  column \


Prozesse eines Terminals
=========================

* Ctrg+z -> Prozess im Vordergrund im Hintergrund schlafen legen (suspend)
* Ctrg+c -> Tötet den Prozess im Vordergrund
* Ctrg+\ -> Tötet den Prozess + Core Dump
* Ctrg+R -> Rückwärts suchen
* jobs   -> zeigt alle Prozesse des Terminals mit Nummern an
* bg %Prozessnummer  -> Restartet schlafende Prozesse im Hintergrund
* fg %Prozessnummer -> holt Prozesse aus dem Hintergrund in den Vordergrund
* Ctrg+z  + bg %Prozessnummer ->  Prozesse in den Hintergrund schieben die im Vordergrund laufen


ZSh Bindings
=============

* bindkey -L -> listet alle zsh Bindings auf
* bindkey '\C-w' kill-region  -> setzt zsh keybinding für kill-region auf Ctrg+w (für dauerhafte Bindings einfach in die .zshrc eintragen)
* read -> liest einen Buchstaben ein und gibt seine escapde Form aus für ein bindkey
* bindkey -s '\C-ff' "firefox" -> Bindet den String firefox an die Tastenkürtzel Ctrg+ff

* stty -a  -> zeigt alle Terminal bindings und mehr an
* Terminal bindings ändern mit
* stty intr '^t'  -> Interrupt jetzt nicht mehr Ctrg+c sondern Ctrg+t


Keybindings für BASH ZSH und Emacs
===================================

* Alt + b		-> Wort zurück springen
* Alt + f 	        -> Wort vor springen
* Alt + Backspace	-> Wort vor Cursor löschen
* Alt + d		-> Wort nach Cursor löschen
* Alt + h 	        -> manpage des Befehls aufrufen
* Alt + Q		-> Befehl für eine Zeile in den Hintergrund schieben
* Strg + l 	        -> clean screen
* Strg + x Strg +x      -> Zeile von Cursor bis Anfang der Zeile markieren (EMACS markiert Block)
* Alt + .       	->  Argumente der vorhergehenden Befehle abrufen (nur BASH und ZSH)
* Strg + Space          -> Marke setzen
* Strg + k 	        -> Ende der Zeile löschen von Cursor
* Strg + w 	        -> Anfang der Zeile löschen bis Cursor
* Strg + u 	        -> ganze Zeile löschen
* Strg + s	        -> suche vorwärts
* Strg + r 	        -> suche rückwärts
* Strg + s	        -> Output Pause und     Strg + Q  -> Fortsetzen der Ausgabe

Directory Stack
===============

* dirs -v    -> zeigt alle Directory des Stacks an
* ~    	   -> Home dir
* ~person    -> home dir von person
* ~- 	   -> letztes Verzeichnis
* ~3 	   -> 2 Verzeichnis im Stack


Befehle finden
===============

* type acroread -> zeigt das Verzeichnis vom Adobe Reader an
* which firefox -> "" von Firefox
* whence -M '*fg' -> gibt alle Befehle die auf fg-enden mit vollen Pfad  aus
* ls *.{c,h,o} -> gibt alle Dateien aus die auf c, h oder o enden
* echo {1..10} -> gibt alle Zahlen von 1 bis 10 aus


Pattern Matching
================

* Dateien finden & Pattern Matching (ls ist doch Befehle wie chmod, print oder echo etc. ersetzbar)
* ls * 	 -> alle Dateien und Verzeichnisse in diesem Verzeichnis (0 bis n Zeichen) ausgeschlossen sind . Dateien!
* ls **/	 -> alle Dateien und Verzeichnisse in diesem Verzeichnis und allen Unterverzeichnissen ausgenommen . Dateien
* ls */**/ -> -> alle Dateien und Verzeichnisse in allen Unterverzeichnissen ausgenommen . Dateien
* ls .*	 -> listet alle .Dateien diese Verzeichnisses

* ?  	  -> ein Zeichen
* [abc]	  -> ein a,b, oder c
* [a-z] 	  -> ein Zeichen zwischen a bis z
* [1A-Z]    -> 1 oder ein Zeichen zwischen A bis Z
* [^a-z]    -> kein Zeichen zwischen a bis z das selbe wie
* (doc|txt) -> entweder txt oder doc
* <1-9>     -> Zahlen zwischen 1 - 9
* pat1~pat2 -> das Pattern vor der ~ soll gesucht werden und danach alle Ergebnisse mit dem Pattern nach der ~ entfernt werden
* #	  -> 0, 1 oder mehrfaches auftreten von Zeichen oder [] ()
* (i#)read(I#) -> sucht nach allen groß und klein geschriebenen read

* Globale Qualifier müssen immer am ende des Pattern in () Klammern stehen
* . -> nur reguläre Dateien keine Verzeichnisse oder Links
* @ -> nur Links
* / -> nur Verzeichnisse
* * -> ausführbare Dateien (keine Verzeichnisse)
* f:u+rwx,o-rwx:  -> Dateirechte (hier User hat read write execute others haben kein read write execute
* Lk+100 	       -> Filegröße (hier Kilobyte größer 100) m für Megabyte, - für kleiner
* mh-1	       -> File Timestamp (hier kleiner eine Stunde) m für Minuten, + für mehr als
* on 	       -> sortierte Ausgabe

* Coluom Modifiers as Qualifiers (müssen in den global Qualifiers ganz am Ende stehen)
* :t 	-> zeigt nur den Hintern Teil der Ausgabe an (z.b. nur Dateinamen nicht den Pfad)
* :t:s/z/ZED/ -> zeigt nur den hinteren Teil der Ausgabe an und ersetzt in jeder Zeile das erste  z mit ZED
* :t:gs/z/ZED/ -> zeigt nur den hinteren Teil der Ausgabe an und ersetzt in jeder Zeile alle z mit ZED


Misc
=====

* zsh oder bash für Windows use Cygwin
* http://www.rayninfo.co.uk/tips/zshtips.html
* http://grml.org/zsh/zsh-lovers.html
