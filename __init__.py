#! /usr/bin/env python
# coding=utf-8

import os.path
import subprocess


class Task(object):
    title = "Compilation of TCC"
    version = 1
    arguments = [
        {"name": "prefix", "type": "text", "title": "Install directory prefix (used for configure script)"},
        {"name": "patch", "type": "file", "title": "Patch file"},
        {"name": "strip", "type": "bool", "title": "Strip symbol tables from resulting binaries?"},
        {"name": "flags", "type": "checkbox", "values": ["Wall", "g", "O2"], "title": "Specify compiler flags"},
        {"name": "lib", "type": "radio", "values": ["libtcc", "libgcc"], "title": "Select library to use"}
    ]

    @staticmethod
    def setup(srcdir):
        print "__setup__"
        retcode = subprocess.call(['git', 'clone', 'https://github.com/lugovskoy/dts-sample-compile.git', srcdir])
        return
        if retcode != 0:
            raise Exception("Cannot setup git repo in {0}".format(srcdir))


    def __init__(self):
        print "__init__"
        self.__wd = os.path.dirname(os.path.realpath(__file__))
        self.__tcc_dir = os.path.join(self.__wd, 'tcc')
        retcode = subprocess.call(['git', 'clone', 'git://repo.or.cz/tinycc.git', self.__tcc_dir])
        return 
        if retcode != 0:
            raise Exception("Cannot initialize git repo in {0}".format(self.__tcc_dir))


    def __call__(self, args, resdir, q):
        print "__call__"
        tcc_srcdir = self.__tcc_dir
        tcc_resdir = os.path.join(resdir, 'opt')
        print tcc_srcdir
        os.chdir(tcc_srcdir)
        retcode = subprocess.call(['./configure', '--prefix={0}'.format(tcc_resdir)])
        if retcode != 0:
            raise Exception("Cannot configure in {0}".format(tcc_srcdir))
        retcode = subprocess.call(['make'])
        if retcode != 0:
            raise Exception("Cannot make in {0}".format(tcc_srcdir))
        retcode = subprocess.call(['make', 'install'])
        if retcode != 0:
            raise Exception("Cannot install to {0}".format(tcc_resdir))
        q.put({'tcc': os.path.join(tcc_resdir, 'bin')})

