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
ctrl q                       goto last edit position
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
alt shift up / down          copy line upwards / downwards
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
* batisteo.vscode-django
* cirlorm.mobileview
* codista.vscode-autosave
* cschlosser.doxdocgen
* cweijan.vscode-mysql-client2
* dineug.vuerd-vscode
* E-Jacques.pytestersuits
* eamodio.gitlens
* ecmel.vscode-html-css
* esbenp.prettier-vscode
* firefox-devtools.vscode-firefox-debug
* formulahendry.auto-rename-tag
* golang.go
* Gruntfuggly.todo-tree
* HoangKimLai.ipython
* jeff-hykin.better-cpp-syntax
* jorol.perl-completions
* josetr.cmake-language-support-vscode
* krizzdewizz.goto-last-edit-location
* ms-azuretools.vscode-docker
* ms-dotnettools.vscode-dotnet-runtime
* ms-python.python
* ms-python.vscode-pylance
* ms-vscode-remote.remote-containers
* ms-vscode.cmake-tools
* ms-vscode.cpptools
* ms-vscode.cpptools-extension-pack
* ms-vscode.cpptools-themes
* ms-vscode.js-debug-nightly
* ms-vscode.live-server
* ms-vscode.makefile-tools
* mtxr.sqltools
* mtxr.sqltools-driver-mysql
* mtxr.sqltools-driver-pg
* mtxr.sqltools-driver-sqlite
* PierreQuemard.macro
* pranaygp.vscode-css-peek
* redhat.ansible
* redhat.fabric8-analytics
* redhat.java
* redhat.vscode-community-server-connector
* redhat.vscode-rsp-ui
* redhat.vscode-server-connector
* redhat.vscode-yaml
* richterger.perl
* ritwickdey.LiveServer
* theumletteam.umlet
* tushortz.python-extended-snippets
* twxs.cmake
* VisualStudioExptTeam.intellicode-api-usage-examples
* VisualStudioExptTeam.vscodeintellicode
* vscjava.vscode-java-debug
* vscjava.vscode-java-dependency
* vscjava.vscode-java-pack
* vscjava.vscode-java-test
* vscjava.vscode-maven
* wsds.theme-hacker
* xabikos.JavaScriptSnippets
