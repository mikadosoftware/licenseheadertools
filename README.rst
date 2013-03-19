:docurl: http://license-header-tool.mikadosoftware.com
:desc: Ensure all files hold correct license header
:license: AGPLv3.  See LICENSE.txt

===================
License Header Tool
===================

One is supposed to put a header at the top of every OSS file similar to below ::

 #!/usr/bin/env python
 #! -*- coding: utf-8 -*-

 ###
 # Copyright (c) Rice University 2012
 # This software is subject to
 # the provisions of the GNU Lesser General
 # Public License Version 2.1 (LGPL).
 # See LICENCE.txt for details.
 ###

But you have shell, python, javsscript, php and java files in your repo,
and maybe dozens of them.  Fixing them all up is a pain.  This is trying to releave the pain.

No its not clever, and it could break, but its a loit faster than writing it 
yourself.

I also intend to devlop it as a plugin for flake8


  python fileheadermaker.py --conf=conf.ini --fldr=/home/pbrian/src/public/Connexions/rhaptos2.repo/rhaptos2/repo
  python fileheadermaker.py --conf=conf.ini --fldr=/home/pbrian/src/public/Connexions/rhaptos2.repo/rhaptos2/repo
