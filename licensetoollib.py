#!/usr/bin/env python
#! -*- coding: utf-8 -*-

###
# Copyright (c) Rice University 2012-13
# This software is subject to
# the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
###


"""
We want to be able to visit file(s) on a filesystem and
match their suffixes with known suffixes, and ensure that
each file has an appropriate OSS license header in it.

How does it work
----------------

1. Given a fldr, walk the tree
2. for each file in tree, analyse it
3. if file matches conf.ini defined set of exts,
   replace the header of the file with the one
   named "use_these_headers.py"

(Yeah I did play with importing the recipie via imp. It is feasible
but PITA for doctests and generally overkill)



How to run tests
----------------

$ python licensetoollib.py
  (will run doctests)


.. todo::

  1. ignore-file
  2. tie into flake8 extension

"""

import shutil
import sys
import os

## I was playing with imp and importing a redcipie provided on command line but it is
## awful with doctests and frankly a lot of effort.
## So, just change the name of file in this dir
import use_these_headers as CurrentRecipie


class LicenseToolError(Exception):
    pass
  
def extract_hdr(txt, ext):
    """Given a file return the hdr and body components

    >>> txt = '''#!/bin/python
    ... # this is a header
    ...
    ... def foo():
    ...     print 1'''
    >>> extract_hdr(txt, ".py")
    ('#!/bin/python\\n# this is a header\\n\\n', 'def foo():\\n    print 1\\n')
    """
    orig_hdr = ''
    body = ''
    hdrflag = 0
    for line in txt.split("\n"):
        if (lineishdr(line, ext) and hdrflag == 0):
            orig_hdr += line + "\n"
        else:
            hdrflag = 1
            body += line + "\n"
    return (orig_hdr, body)    

def lineishdr(l, ext):

    """Determine is a line *at top of a file* is a header, or if its
    body

    We simply assume that the header of a file is a contiguous block
    of comment and blank lines.  Anything else triggers "no longer
    header" flag


    issue: sometimes we have lines of comment that are comment only
           because previous line is this block style is parseable, but
           I dont want to wonder off course too much.  For the moment
           only line by line comments are considered headers.


    >>> lineishdr("#!/usr/local/bin/python", ".py")
    True

    >>> lineishdr("#!/usr/local/bin/python", ".rst")
    False


    >>> lineishdr("  ", ".py")
    True

    >>> lineishdr(" #!/usr/local/bin/python", ".py")
    False

    >>> lineishdr("import os", ".js")
    False

    >>> lineishdr("// THis is JS", ".js")
    True
    
    >>> lineishdr("function foo()", ".py")
    False

    """
    try:
        tmpl, commentsymbols = CurrentRecipie.SUFFIX_MAP[ext]
    except Exception, e:
        raise LicenseToolError(str(e))
    
    for symbol in commentsymbols:
        if l.find(symbol) == 0:
            return True
            
    if l.strip() == '':
        return True
    #default    
    return False

    
def adjust_one_file(f, confd):
    """
    Badly named function that iterates over each line in a file fromt top
    and if that line meets the "hdr" criteria (ie starts with comment symbol)
    it is kept as original hdr, and gets replaced with new shiny hdr.
    Once hdr state ends everything is then kept pristine.


    testing?
    """
    tmpf = '/tmp/fooblah.txt'  ###awful replace!
    ext = os.path.splitext(f)[1]
    tmpl = CurrentRecipie.SUFFIX_MAP[ext][0]
    tmpfo = open(tmpf, 'w')

    hdr, body = extract_hdr(open(f).read(), ext)
    tmpfo.write(tmpl)
    tmpfo.write(body)
    tmpfo.close()

    shutil.move(tmpf, f)


def walk_tree(fldr, extlist):
    """Given fldr, walk the tree and return all files as abspaths """
    outfiles = []
    for root, dirs, files in os.walk(fldr):
        if ".git" in dirs: dirs.remove(".git")
        fileshere = [os.path.join(root, f) for f in
                     files if os.path.splitext(f)[-1:][0] in extlist]
        outfiles.extend(fileshere)
    return outfiles

def simplelog(msg):
    fo = open("license.log", "a")
    fo.write(str(msg)+"\n")
    fo.close()

def ext_in_list(ext, l):
    """Just simple for in seems to break in odd places - pullingout

    >>> ext_in_list(".py", [".py", ".js", ".java"])
    True
    >>> ext_in_list(".rpy", [".py", ".js", ".java"])
    False

    """
    for myext in l:
        if myext == ext:
            return True
        else:
            pass
    return False
    
def analyse_file(f, confd):
    """Given file, decide if it is suitable, if it alredy has header,
    is header uptdate and otehr

    bit rubbish analysis - returning flags to act upon

    
    
    """
    FLAGS = {'VALID_EXT': False,
             'BLANK_HEADER': False,
             'HEADER_OUTOFDATE': False,
         }
    currext = os.path.splitext(f)[-1:][0]
    if ext_in_list(currext, confd['app']['validexts']):
        FLAGS['VALID_EXT'] = True
        hdr, body = extract_hdr(open(f).read(), currext)
        if len(hdr) == 0: FLAGS['BLANK_HEADER'] == True
    else:
        return FLAGS
    return FLAGS

if __name__ == '__main__':
    import doctest
    doctest.testmod()



