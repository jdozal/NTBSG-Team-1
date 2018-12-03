#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:06:56 2018

@author: Jessica Dozal
"""
import xml.etree.ElementTree as ET

class PDML:    
    def __init__(self):
        self.name = ''
        self.timeStamp = ''
        self.analystName = ''
        self.date = ''
        self.stage = ''
        
    def setName(self, name):
        self.name = name
        print(self.name)
    
    def parse(self):
        tree = ET.parse(self.name)
        root = tree.getroot()
        print(root)
        
    
         
