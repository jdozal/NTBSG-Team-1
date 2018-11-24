#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:05:39 2018

@author: Jessica Dozal
"""

import pyshark

class PCAP:
    name = ''
    filePath= ' '
    
    def convert():
        cap = pyshark.FileCapture('/Users/jdozal/Documents/Fall2018/SOFTWARE/PCAP/maccdc2012_00000.pcap')
        print(cap[0])
        
    convert()