#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:49:50 2018

@author: Jessica Dozal
"""
import os 
import sys
sys.path.append('../')
import PCAP

class Dissector:    
    def __init__(self, dname, dpath):
        self.name = dname
        self.filePath = dpath
    
    def convert(self, pcap):
        # PCAP to PDML 
        cmd = "tshark -r "+ pcap.getPath() + " > " + pcap.getName() + ".pdml -T pdml"
        
        os.system(cmd)
        
        pdmlName = pcap.getName() + ".pdml"
        
        return pdmlName
        
        
        
    