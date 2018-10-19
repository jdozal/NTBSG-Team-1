#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import FileChooserWindow

class WorkspaceLauncher(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")
        #self.set_size_request(500, 200)
        self.set_border_width(50)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        mainLabel = Gtk.Label("Select a directory as workspace: NTBSG uses the workspace \ndirectory to store sessions")
        vbox.pack_start(mainLabel, True, True, 0)

        # Workspace path        
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label("Workspace")
        hbox.add(label)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Workspace Directory Path")
        hbox.add(entry)
        browseFolder1 = Gtk.Button("Browse")
        hbox.add(browseFolder1)
        vbox.add(hbox)
        
        # Destination name
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label("Destination \nFolder Name")
        hbox.add(label)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Destination Folder Name")
        hbox.add(entry)
        vbox.add(hbox)

        # Destination path
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label("Destination \nFolder Path")
        hbox.add(label)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Destination Folder Path")
        hbox.add(entry)
        browseFolder2 = Gtk.Button("Browse")
        hbox.add(browseFolder2)
        vbox.add(hbox)
        
        
        # Buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        launchButton = Gtk.Button("Launch")
        hbox.add(launchButton)
        cancelButton = Gtk.Button("Cancel")
        hbox.add(cancelButton)
        vbox.add(hbox)
        
        # Connecting buttons 
        launchButton.connect("clicked", self.on_launch_clicked) 
        cancelButton.connect("clicked", self.on_destroy)
        browseFolder1.connect("clicked", self.on_folder_clicked)
        browseFolder2.connect("clicked", self.on_folder_clicked)
        
    def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)

    def on_visible_toggled(self, button):
        value = button.get_active()
        self.entry.set_visibility(value)

    def on_pulse_toggled(self, button):
        if button.get_active():
            self.entry.set_progress_pulse_step(0.2)
            # Call self.do_pulse every 100 ms
            self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
        else:
            # Don't call self.do_pulse anymore
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
            self.entry.set_progress_pulse_step(0)

    def do_pulse(self, user_data):
        self.entry.progress_pulse()
        return True

    def on_icon_toggled(self, button):
        if button.get_active():
            icon_name = "system-search-symbolic"
        else:
            icon_name = None
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY,
            icon_name)
        
    def on_launch_clicked(self, widget):
        from MainWindow import MainWindow
        win = MainWindow()
        win.show_all()
    
    def on_destroy(self, widget):
        self.destroy()
    
    def on_folder_clicked(self,widget):
        FileChooserWindow.on_folder_clicked(self,widget)
        
win = WorkspaceLauncher()
win.connect("destroy", Gtk.main_quit)
win.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
win.show_all()
Gtk.main()