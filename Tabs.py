#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Tabs(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Tabs")
        self.set_border_width(10)
        self.set_default_size(1100, 200)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        #New/Modify Page
        self.newPage = Gtk.Box()
        self.newPage.set_border_width(10)
        self.newPage.add(Gtk.Label("content Main"))
        self.notebook.append_page(self.newPage, Gtk.Label("New/Modify"))

        #Dependency Page
        self.dependencyPage = Gtk.Box()
        self.dependencyPage.set_border_width(10)
        self.dependencyPage.add(Gtk.Label("content 2"))
        self.notebook.append_page(self.dependencyPage, Gtk.Label("Dependency"))

        #Template Page
        self.templatePage = Gtk.Box()
        self.templatePage.set_border_width(10)
        self.templatePage.add(Gtk.Label("content Main"))
        self.notebook.append_page(self.templatePage, Gtk.Label("Template"))

        #Equivalency Page
        self.equivalencyPage = Gtk.Box()
        self.equivalencyPage.set_border_width(10)
        self.equivalencyPage.add(Gtk.Label("content Main"))
        self.notebook.append_page(self.equivalencyPage, Gtk.Label("Equivalency"))

        #Generation Page
        self.generationPage = Gtk.Box()
        self.generationPage.set_border_width(10)
        self.generationPage.add(Gtk.Label("content Main"))
        self.notebook.append_page(self.generationPage, Gtk.Label("Generation"))

window = Tabs()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()