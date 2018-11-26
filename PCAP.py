#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:05:39 2018

@author: Jessica Dozal
"""

import os 

class PCAP:
    name = ''
    filePath= ' '
    
    def convert():
        # PCAP to PDML 
        cmd = "tshark -r test.pcap > testPDML.pdml -T pdml"
        os.system(cmd)
    
    convert()