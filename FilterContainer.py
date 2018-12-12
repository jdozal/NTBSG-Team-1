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

# TODO FIGURE OUT THE FILTERING OF PROTOCOLS
    def filterOut(self, filterT, file):
    	for country in root.findall('country'):
    		rank = int(country.find('rank').text)
    		if rank > 50:
    			root.remove(country)
    	tree.write('output.xml')

# FC = FilterContainer()
# FC.addFilter()
# FC.addFilter()