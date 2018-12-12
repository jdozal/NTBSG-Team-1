#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:09:01 2018

@author: Jessica Dozal
"""
import Filter

class FilterContainer:
    def __init__(self):
        self.filterList = ["ICMP", "TCP", "DNS"]
        
    def addFilter(self):
        filterName = "name"
        expressionName = "expression"
        currFilter = Filter.Filter(filterName, expressionName)
        self.filterList.append(currFilter)
        print(self.filterList)

# FC = FilterContainer()
# FC.addFilter()
# FC.addFilter()