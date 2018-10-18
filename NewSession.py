#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NewSession(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Session")
        #self.set_size_request(500, 200)
        self.set_border_width(20)

        self.timeout_id = None
        
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)


        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        mainLabel = Gtk.Label("Create a new session")
        vbox.pack_start(mainLabel, True, True, 0)

        # Workspace path        
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label("Session Name")
        hbox.add(label)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Project Name")
        hbox.add(entry)
        vbox.add(hbox)
        
        # Destination name
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label("Description")
        hbox.add(label)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Project Description")
        hbox.add(entry)
        vbox.add(hbox)        
        
        # Buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        createButton = Gtk.Button("Create")
        hbox.add(createButton)
        cancelButton = Gtk.Button("Cancel")
        hbox.add(cancelButton)
        vbox.add(hbox)
        
        # Connecting buttons 
        cancelButton.connect("clicked", self.on_destroy)
        
    
    
    def on_destroy(self, widget):
        self.destroy()
        
win = NewSession()
win.connect("destroy", Gtk.main_quit)
#win.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
win.show_all()
Gtk.main()