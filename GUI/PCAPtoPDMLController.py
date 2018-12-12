#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys 
sys.path.append('../')
import PCAP
import Dissector 
import PDML

class PCAPtoPDMLController:
    def __init__(self):
        self.pcap = PCAP.PCAP('','')
        self.dissector = Dissector.Dissector('','')
        self.pdml = PDML.PDML()
        
    def setPCAP(self, path):
        self.pcap.setAttributes(path)
        
    def callConversion(self, path):
        namePDML = self.dissector.convert(self.pcap, path)
        self.pdml.setName(namePDML)
        self.pdml.parse()
        
    


