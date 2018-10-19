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

    add_filters(self,dialog)

    response = dialog.run()
    filePath = ''
    if response == Gtk.ResponseType.OK:
        print("Open clicked")
        print("File selected: " + dialog.get_filename())
        filePath = dialog.get_filename()
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")

    dialog.destroy()
    return filePath
    

def on_folder_clicked(self, widget):
    dialog = Gtk.FileChooserDialog("Please choose a folder", self,
        Gtk.FileChooserAction.SELECT_FOLDER,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
         "Select", Gtk.ResponseType.OK))
    dialog.set_default_size(800, 400)

    response = dialog.run()
    folderPath = ''
    if response == Gtk.ResponseType.OK:
        print("Select clicked")
        print("Folder selected: " + dialog.get_filename())
        folderPath = dialog.get_filename()
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")

    dialog.destroy()
    return folderPath

def add_filters(self, dialog):
    filter_text = Gtk.FileFilter()
    filter_text.set_name("Text files")
    filter_text.add_mime_type("text/plain")
    dialog.add_filter(filter_text)

    filter_py = Gtk.FileFilter()
    filter_py.set_name("Python files")
    filter_py.add_mime_type("text/x-python")
    dialog.add_filter(filter_py)

    filter_any = Gtk.FileFilter()
    filter_any.set_name("Any files")
    filter_any.add_pattern("*")
    dialog.add_filter(filter_any)