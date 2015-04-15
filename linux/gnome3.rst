#######
Gnome3
#######

Configure startup applications
==============================

* You can eithe use
  
.. code-block:: bash

  gnome-session-properties

* or

.. code-block:: bash

  gnome-tweak-tool
		

Install a new theme
===================

* Goto www.gnome-look.org
* Download a theme
* Unzip it to ~/.themes
* Install it with gnome-tweak-tool


Cool themes
===========

* http://gnome-look.org/content/show.php/Ambiance+Dark+Blue?content=169553
* http://gnome-look.org/content/show.php/E17gtk?content=163472
* http://gnome-look.org/content/show.php/Cenodark-red?content=165815
* http://gnome-look.org/content/show.php/Just-Dark?content=168025q


Automatically place windows
===========================

* Enable Auto move windows extension
* Add new placement rule


Non blank screensaver
=====================

* killall gnome-screensaver
* yum install xscreensaver
* xscreensaver-demo


Changing keyboard shortcuts
===========================

* Applications -> System Tools -> System Settings -> Keyboard


Default shortcuts
=================

* Alt+F1 - Switch between overview and desktop view
* Alt+F2 - Launch command
* Windows key - Goto activity view (enter first keys of what to execute / search)


Reload Gnome config
===================

* Alt+F2 r


Install extensions
==================

* Goto extensions.gnome.org
* Click on an extensions
* Use the on/off button to install/deinstall extension


Pidgin integration
==================

* Install https://extensions.gnome.org/extension/170/pidgin-peristent-notification/
* Or install https://extensions.gnome.org/extension/258/notifications-alert-on-user-menu/


System monitor in top panel
===========================

* Install https://extensions.gnome.org/extension/120/system-monitor/


Declaring the primary monitor
=============================

* Goto settings -> monitor
* Use drag and drop to move the monitors around, the first is the primary


Configure desktop to be on all monitors
=======================================

* gnome-tweak-tool -> desktops

Remove window decorations
==========================

* Assuming you use Adwaita as theme
* Edit /usr/share/themes/Adwaita/metacity-1/metacity-theme-1.xml
* Search for frame_geometry name="normal"
* Add has_title="false"
* Reload Gnome config


Alternative menu
================

* To access the alternative menu hold the Alt key
* This will for example allow you to hibernate instead of shutdown in the user menu


Switching back to old GNOME look and feel
=========================================

* Either set "Use Fallback Mode" in System Settings -> Details -> Graphics
* Or install Mate http://mate-desktop.org/
