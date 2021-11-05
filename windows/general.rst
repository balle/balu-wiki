#######
General
#######

Package Manager
===============

* https://chocolatey.org/


Keyboard shortcuts
==================

===================== ==============
Shortcut              Description
--------------------- --------------
Windows + A           Infocenter
Windows + D           Show desktop
Windows + E           Explorer
Windows + I           Settings
Windows + K           Connect
Windows + L           Lock screen
Windows + R           Execute
Windows + V           Clipboard
Windows + left/right  Split desktop
Strg + Shift + Enter  Execute seleted programm as administrator
===================== ==============


Disable Internet search in taskbar search
=========================================

* By default if you search in the taskbar search field or via start menu all you enter is sent to the Bing search engine
* To disable this open the regedit program as administrator and navigate to HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search
* Create the following two new DWORD entries and give it the value 0
* BingSearchEnabled
* CortanaConsent
* Log out and in again


Ansible on Windows
==================

* Install Cygwin with Git and Ansible
* Install OpenSSH Server via Settings -> Apps -> Apps and Features -> Optional Features -> Add a feature
* Edit C:\ProgramData\ssh\sshd_config to change ListenAddress to 127.0.0.1
* Start service via services app
