#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class OpenPCAP(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Open PCAP")
        #self.set_size_request(500, 200)
        self.set_border_width(20)

        self.timeout_id = None
        
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)


        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        mainLabel = Gtk.Label("Open a PCAP File")
        vbox.pack_start(mainLabel, True, True, 0)

        # Workspace path        
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label("PCAP Name")
        hbox.add(label)
        entry = Gtk.Entry()
        entry.set_placeholder_text("PCAP File")
        hbox.add(entry)
        button = Gtk.Button("Browse")
        hbox.add(button)
        vbox.add(hbox)
        
        # Workspace path        
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label("Dissector Name")
        hbox.add(label)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Optional Dissector")
        hbox.add(entry)
        button = Gtk.Button("Browse")
        hbox.add(button)
        vbox.add(hbox)     
        
        # Buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        createButton = Gtk.Button("Convert to PDML")
        hbox.add(createButton)
        cancelButton = Gtk.Button("Cancel")
        hbox.add(cancelButton)
        vbox.add(hbox)
        
        # Connecting buttons 
        cancelButton.connect("clicked", self.on_destroy)
        
    
    
    def on_destroy(self, widget):
        self.destroy()
        
win = OpenPCAP()
win.connect("destroy", Gtk.main_quit)
#win.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
win.show_all()
Gtk.main()