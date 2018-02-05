#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:57:11 2018

@author: f2a
"""

from setuptools import setup


setup(
      name='cryptopass',
      version=__import__('cryptopass').__version__,
      author='f2a',
      author_email='',
      #scripts=['cryptopass'],    
      description='Safe and simple passwords manager',
      url='https://github.com/francof2a/cryptopass',
      test_suite='tests',
      license='MIT',
      keywords='password safe store',
      classifiers=[
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python',
          'Environment :: Console',
          'Topic :: Security',
          ],
        entry_points={'console_scripts': ['cryptopass=console:main',],},
      )
