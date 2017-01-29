Personal Configuration
======================

This repo contains configuration files, notes and scripts for my personal configuration of Linux systems. Tested with Debian 8 (Jessie), but not on a completely fresh install.
I've uploaded this for my own usage, to make setting up new systems easier, but of course everyone's allowed to use it for any purpose.

Code in this repository is licenced under MIT license as stated in LICENSE.txt, with the exception of code from external sources. Such contains explicit license information.

Autosetup script
----------------

The autosetup.py script from this repo automates some changes needed for my setup. Namely, it does the following:
* Links the Vim configuration files from resources folder to the user's home directory.
* Links the bash alias configuration files from resources folder to the user's home directory.
* Creates directories for my Blender development builds and pulls the Blender source code.
