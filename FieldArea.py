#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def Tabs():
    # Box for tabs section
    tabs = Gtk.Box()
    
    # List box for tabs section
    tabsList = Gtk.ListBox()
    tabs.add(tabsList)
    
    # Box for title 
    titleBox = Gtk.Box() 
    labelTitle = Gtk.Label()
    labelTitle.set_markup("<u>Field Area</u>")
    
    titleBox.set_child_packing(labelTitle, True, True, 100,0)
    titleBox.add(labelTitle)
    
    tabsList.add(titleBox)

    notebook = Gtk.Notebook()

    #New/Modify Page
    newPage = Gtk.Box()
    newPage.set_border_width(10)
    newPage.add(Gtk.Label("content Main"))
    notebook.append_page(newPage, Gtk.Label("New/Modify"))

    #Dependency Page
    dependencyPage = Gtk.Box()
    dependencyPage.set_border_width(10)
    dependencyPage.add(Gtk.Label("content 2"))
    notebook.append_page(dependencyPage, Gtk.Label("Dependency"))

    #Template Page
    templatePage = Gtk.Box()
    templatePage.set_border_width(10)
    templatePage.add(Gtk.Label("content Main"))
    notebook.append_page(templatePage, Gtk.Label("Template"))

    #Equivalency Page
    equivalencyPage = Gtk.Box()
    equivalencyPage.set_border_width(10)
    equivalencyPage.add(Gtk.Label("content Main"))
    notebook.append_page(equivalencyPage, Gtk.Label("Equivalency"))

    #Generation Page
    generationPage = Gtk.Box()
    generationPage.set_border_width(10)
    generationPage.add(Gtk.Label("content Main"))
    notebook.append_page(generationPage, Gtk.Label("Generation"))
    
    tabsList.add(notebook)
    return tabs