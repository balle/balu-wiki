##############
Android Tools
##############

Enable USB Debugging 
=====================

* On the android device go to settings -> about
* Tab on the build number seven times
* Go back to settings than to developer options
* Enable USB Debugging

Install an apk
==============

.. code-block:: bash

    adb install some_app.apk

List all installed apps
=======================

.. code-block:: bash

    adb shell pm list packages

Download an installed app
=========================

.. code-block:: bash

    adb shell pm path <package_name>
    adb pull <apk_path> <destination_path>
