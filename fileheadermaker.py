#!/usr/bin/env python
#! -*- coding: utf-8 -*-

###
# Copyright (c) Rice University 2012
# This software is subject to
# the provisions of the GNU Lesser General
# Public License Version 2.1 (LGPL).
# See LICENCE.txt for details.
###


"""
We want to be able to visit


"""
import shutil
import sys
import os
from optparse import OptionParser
from rhaptos2.common import conf
import licensetoollib as llib


def parse_args():
    parser = OptionParser()
    parser.add_option("--fldr", dest="fldr",
                      help="folder to descend and add headers")
    parser.add_option("--conf", dest="confpath",
                      default="conf.ini",
                      help="Config file")

    (options, args) = parser.parse_args()
    return (options, args)


if __name__ == '__main__':
    
    opts, args = parse_args()
    confd = conf.get_config(opts.confpath)
    validexts = eval(confd['app']['validexts'])
    confd['app']['validexts'] = validexts
    files_to_process = llib.walk_tree(opts.fldr,
                                      confd['app']['validexts'])
    for f in files_to_process:
        
        if not os.path.isfile(f):
            raise OSError("%s must be a file" % f)

        llib.simplelog("Analyse %s" % f)
        FLAGS = llib.analyse_file(f, confd)
        llib.simplelog(FLAGS)

        if FLAGS['VALID_EXT'] is True:  # I cpould make different decisions here based on config
            llib.adjust_one_file(f, confd)
            llib.simplelog("Done %s" % f)
        
