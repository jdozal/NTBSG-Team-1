#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:49:50 2018

@author: Jessica Dozal
"""

class Dissector:
    name=''
    filePath=''
    
    def __init__(self, dname, dpath):
        self.name = dname
        self.filePath = dpath