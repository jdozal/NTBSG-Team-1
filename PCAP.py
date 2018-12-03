#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:05:39 2018

@author: Jessica Dozal
"""

class PCAP:    
    def __init__(self, name, filePath):
        self.filePath= filePath
        splitPath = filePath.split('/')
        print(splitPath)
        self.name = splitPath[-1]
        #if(self.name.contains('.pcap')):
        self.name = self.name.replace('.pcap','')
        
        # Create PDML object 
    
    def setAttributes(self, filePath):
        self.filePath= filePath
        splitPath = filePath.split('/')
        print(splitPath)
        self.name = splitPath[-1]
        #if(self.name.contains('.pcap')):
        self.name = self.name.replace('.pcap','')     
        
    def getPath(self):
        return self.filePath 
    
    def getName(self):
        return self.name
        
