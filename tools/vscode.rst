#######
VSCode
#######

Keyboard shortcuts
==================

============================ ==============
Shortcut                     Description
---------------------------- --------------
ctrl shift p                 open command palette
ctrl p                       goto file
ctrl g                       goto line
ctrl b                       display / hide sidebar
ctrl j                       new terminal
alt t                        focus terminal
ctrl 1                       focus current editor
ctrl shift p, type zen mode  remove everythin but edition window
ctrl shift p, type minimap   switch off mini map
ctrl b                       toggle sidebar
ctrl shift e                 goto explorer
ctrl shift f                 find over whole project
ctrl shift g                 goto source Control
ctrl shift d                 goto debug
ctrl ,                       goto settings
ctrl `                       goto terminal
ctrl k ctrl h                goto output window
ctrl 1                       goto editor
f12                          goto definition
ctrl f12                     goto implementation
ctrl shift \                 goto matching element
f8                           goto next error
ctrl alt -                   goto last cursor positon
ctrl shift space             Show documentation
ctrl space                   IntelliSense
ctrl .                       Quickfix
ctrl /                       Comment out line
f2                           Rename symbol in all files
ctrl shift p insert snippet  Show all snippets for current file
ctrl alt n                   new file
ctrl w                       close file
ctrl tab, ctrl shift tab     switch file tabs
ctrl p                       search file in project
ctrl k d                     show unsaved changes
ctrl right / left            jump word forward / backward
ctrl backspace / delete      delete word left / right
alt up / down                move line upwards / downwards
ctrl d                       select current word
alt shift                    rectangular edit
!                            execute emmet template
ctrl shift p, live server    show html in browser
alt shift down / up          create multiple cursors
alt click                    create multiple cursors
ctrl k ctrl s                show keyboard shortcuts
ctrl k z                     toggle editor fullscreen
ctrl k ctrl e                save open editors
ctrl k w                     close all open editors
ctrl alt k                   toggle bookmark
ctrl alt l                   jump to next bookmark
ctrl shift g g               git uncommited changes
ctrl shift g c               git commit
ctrl shift g s               git status
ctrl shift g p               git push
ctrl shift g f               git pull
============================ ==============

To get the above git shortcut paste the following in your keyboard shortcuts

.. code-block:: bash

  [
      {
              "key": "ctrl+shift+g c",
	      "command": "-gitlens.showQuickCommitFileDetails",
	      "when": "editorTextFocus && !gitlens:disabled && config.gitlens.keymap == 'chorded'"
	},
	{
	      "key": "ctrl+shift+g c",
	      "command": "git.commit"
	},
	{
	      "key": "ctrl+shift+g p",
	      "command": "git.push"
	},
        {
              "key": "ctrl+shift+g f",
	      "command": "gitlens.pullRepositories"
	}
  ]

Installed extensions
====================

* alefragnani.Bookmarks
* CoenraadS.bracket-pair-colorizer
* cweijan.vscode-mysql-client2
* eamodio.gitlens
* ecmel.vscode-html-css
* esbenp.prettier-vscode
* firefox-devtools.vscode-firefox-debug
* formulahendry.auto-rename-tag
* golang.go
* ms-azuretools.vscode-docker
* ms-python.python
* ms-python.vscode-pylance
* ms-toolsai.jupyter
* ms-toolsai.jupyter-keymap
* ms-toolsai.jupyter-renderers
* ms-vscode.js-debug-nightly
* ms-vscode.live-server
* mtxr.sqltools
* patbenatar.advanced-new-file
* pranaygp.vscode-css-peek
* redhat.java
* VisualStudioExptTeam.vscodeintellicode
* vscjava.vscode-java-debug
* vscjava.vscode-java-dependency
* vscjava.vscode-java-pack
* vscjava.vscode-java-test
* vscjava.vscode-maven
