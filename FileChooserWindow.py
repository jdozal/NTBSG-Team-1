#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:39:13 2018

@author: Jessica Dozal
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_file_clicked(self, widget):
    dialog = Gtk.FileChooserDialog("Please choose a file", self,
        Gtk.FileChooserAction.OPEN,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
         Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

    self.add_filters(dialog)

    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        print("Open clicked")
        print("File selected: " + dialog.get_filename())
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")

    dialog.destroy()

def on_folder_clicked(self, widget):
    dialog = Gtk.FileChooserDialog("Please choose a folder", self,
        Gtk.FileChooserAction.SELECT_FOLDER,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
         "Select", Gtk.ResponseType.OK))
    dialog.set_default_size(800, 400)

    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        print("Select clicked")
        print("Folder selected: " + dialog.get_filename())
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")

    dialog.destroy()