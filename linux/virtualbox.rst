============
 Virtualbox
============

Running on Grsec kernel
=======================

If someone out there should face the same problems as I did here are the Grsecurity features I had to disable to get VirtualBox running correctly:

* grsecurity -> address space protection -> hide kernel symbols
* grsecurity -> filesystem protections -> proc restrictions
* pax -> non-executable pages -> enforce non-executable kernel pages
* pax -> miscellaneous hardening features -> prevent invalid userland pointer dereferences

Headless Server
===============

* http://0x7e.org/blog/2011/10/15/virtualbox-on-a-headless-server/


PXE Boot
=========

* Needs extenstions
* On older versions only via bridged network support


Automation
==========

* http://vagrantup.com/
