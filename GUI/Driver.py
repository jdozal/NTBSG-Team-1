#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:46:20 2018

@author: Jessica Dozal
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
sys.path.append('../')
import Workspace 
import PCAPtoPDMLController
import Session 
import shutil 

workspace = Workspace.Workspace('','')
session = Session.Session("Session1", "original PDML", workspace.path)
workspace.addSession(session)
controller = PCAPtoPDMLController.PCAPtoPDMLController()
pathPCAP = "test.pcap"
controller.setPCAP(pathPCAP)
#controller.callConversion(workspace)
from MainWindow import MainWindow
window = MainWindow(workspace)
#window.connect("destroy", Gtk.main_quit)
window.maximize()
window.show_all()

shutil.rmtree(workspace.path + "/Session1") 
 
Gtk.main()
