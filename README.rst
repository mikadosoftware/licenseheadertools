:docurl: http://license-header-tool.mikadosoftware.com
:desc: Ensure all files hold correct license header
:license: AGPLv3.  See LICENSE.txt

===================
License Header Tool
===================

One is supposed to put a header at the top of every OSS file similar
to below ::

 #!/usr/bin/env python
 #! -*- coding: utf-8 -*-

 ###
 # Copyright (c) Rice University 2012
 # This software is subject to
 # the provisions of the GNU Lesser General
 # Public License Version 2.1 (LGPL).
 # See LICENCE.txt for details.
 ###

But you have shell, python, javsscript, php and java files in your
repo, and maybe dozens of them.  Fixing them all up is a pain.  This
is trying to relieve the pain.

No its not clever, and it could break, but its a lot faster than
writing it yourself.

I also intend to devlop it as a plugin for flake8

.. warning::  This is by default aggressive 
   it captures blank and comment lines at top of file
   and blows them away in preference for the configured
   snippet ala above.

I think a more step-through approach might be a better idea

    


::

  $ python fileheadermaker.py --conf=conf.ini --fldr=/path/to/code/

