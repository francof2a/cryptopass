#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:39:27 2018

@author: f2a
"""

import pyperclip as pclip

pclip.copy('Hello world!')

str_in = pclip.paste()
print(str_in)