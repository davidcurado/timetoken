#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2015
@author: José David Fernández Curado
'''
import sys

from setuptools import setup, find_packages


try:
    sys.path.append('src')
    from timetoken import __version__ as version
except: raise

setup(
    name = 'timetoken',
    version = version,

    author = u'José David Fernández Curado',
    author_email = 'david@dialeti.co',

    packages = find_packages('src'),
    package_dir = {'' : 'src'},
    test_suite = 'timetoken.tests'
)
