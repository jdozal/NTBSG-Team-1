#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:09:01 2018

@author: Jessica Dozal
"""
class Filter:    
    
    def __init__(self):
        self.filterList = []
        
    def addFilter(self, newFilter):
        self.filterList.append(newFilter)
        
