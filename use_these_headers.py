#!/usr/bin/env python
#! -*- coding: utf-8 -*-

###
# Copyright (c) Rice University 2012-13
# This software is subject to
# the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
###


pytmpl = """#!/usr/bin/env python
#! -*- coding: utf-8 -*-

###
# Copyright (c) Rice University 2012-13
# This software is subject to
# the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
###


"""

jstmpl = """
// <!--
// Copyright (c) Rice University 2012-3
// This software is subject to
// the provisions of the GNU Affero General
// Public License Version 3 (AGPLv3).
// See LICENCE.txt for details.
// -->


"""

rsttmpl = """
.. Copyright (c) Rice University 2012-3
.. This software is subject to
.. the provisions of the GNU Affero General
.. Public License Version 3 (AGPLv3).
.. See LICENCE.txt for details.


"""



javatmpl = """
//
// Copyright (c) Mark Matten (mark_matten@hotmail.com) 2011-13
// Part of the dbfit-teradata software.
// This software is subject to the provisions of
// the GNU General Public License Version 2.0 (GPL).
// See LICENCE.txt for details.
//


"""

coffeetmpl = """
# <!-- 
# Copyright (c) Rice University 2012-13
# This software is subject to the provisions of
# the GNU Affero General Public License
# Version 3 (AGPLv3). See LICENCE.txt for details.
# -->

"""


################ CONSTANTS

SUFFIX_MAP = {
    '.py': (pytmpl, ["#",]),
    '.js': (jstmpl, ['//',]),
    '.rst': (rsttmpl, ['..',]),
    '.java': (javatmpl, ['//',]),
    '.coffee': (coffeetmpl, ['#',],)
}





