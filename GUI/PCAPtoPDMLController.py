#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys 
sys.path.append('../')
import PCAP
import Dissector 
import PDML
import Workspace

class PCAPtoPDMLController:
    def __init__(self):
        self.pcap = PCAP.PCAP('','')
        self.dissector = Dissector.Dissector('','')
        self.pdml = PDML.PDML()
        
    def setPCAP(self, path):
        self.pcap.setAttributes(path)
        
    def callConversion(self, workspace):
        #namePDML = self.dissector.convert(self.pcap, workspace.path)
        workspace.setPCAP(self.pcap)
        #self.pdml.setName(namePDML)
        #self.pdml.parse(workspace.path)
        from MainWindow import MainWindow
        self.window = MainWindow(workspace)
        #window.connect("destroy", Gtk.main_quit)
        self.window.maximize()
        self.window.show_all()
