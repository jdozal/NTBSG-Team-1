#!/usr/bin/env python2
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
        cap = pyshark.FileCapture('/tmp/mycapture.cap')
        cap
        
    convert()