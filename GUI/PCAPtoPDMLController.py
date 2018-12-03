#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys 
sys.path.append('../')
import PCAP
import Dissector 

class PCAPtoPDMLController:
    def __init__(self):
        self.pcap = PCAP.PCAP('','')
        self.dissector = Dissector.Dissector('','')
        
    def setPCAP(self, path):
        self.pcap.setAttributes(path)
        
    def callConversion(self):
        self.dissector.convert(self.pcap)


