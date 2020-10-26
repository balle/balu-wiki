##########
Launchctl
##########

Show all running services
=========================

.. code-block:: bash

  launchctl list

  
Disable a service
==================

E.g. Bonjour for MDNS

.. code-block:: bash

  sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponder.plist
  
You may need to boot into recovery mode and disable SIP
