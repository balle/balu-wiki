#########
Security
#########

Encrypt your harddrive
======================

* Open "Manage Bitlocker" app
* Turn on Bitlocker for your hard disk 


Activate Ransomware protection
==============================

* In Windows Defender -> Virus & threat protection -> Manage ransomware protection turn on "Controlled folder access"
* Add folders containing your important data if there are any beside documents, pictures, videos and music
* You can also allow other than preconfigured apps to access the protected directories


Install Application guard
==========================

* To use Edge in an isolated environment (VM) goto Windows Defender -> App & browser control and install Application Guard


Run kernel processes in a sandbox
==================================

* In Windows Defender _> Device security -> Core isolation details activate "Memory integrity"


Run other programs in a sandbox
================================

* Activate the feature "Windows Sandbox"
* After a reboot open Windows Sandbox App
* Copy and paste the program you want to run and start it


Activate ASLR for all programs
==============================

* To activate Adress Space Layout Randomization (ASLR) for all programs go to Windows Defender -> App & browser control -> Exploit protection settings and turn on "Force randomization for images"


Dont upload file for virus protection
=====================================

* In Windows Defender -> Virus settings turn off "Cloud delivered protection"


Turn off smart screen
======================

* If you dont want to upload unknown exe files to the cloud
* In Windows Defender -> App & browser control -> Reputation-based protection turn off "Check apps and files" and "SmartScreen for Microsoft Edge"

