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
    labelTitle.set_markup("<u>Message Type Area</u>")
    
    titleBox.set_child_packing(labelTitle, True, True, 100,0)
    titleBox.add(labelTitle)
    
    tabsList.add(titleBox)

    notebook = Gtk.Notebook()

    #New/Modify Page
    newPage = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    newPage.set_border_width(10)
    newPage.add(newModify())
    #newPage.pack_start(newModify(), True, True, 0)
    #newPage.add(Gtk.Label("content Main"))
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

def newModify():

    mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    instructions = Gtk.Label("To create a new message type, please enter a message type name \n"
                             "and select message type field value pair(s). To update/delete message type. \n"
                             "Please select from the existing message type first and the previously \n"
                             "selected name and field value pair(s) will be pre-populated")
    #mainBox.add(instructions)


    # labels
    typeLabel = Gtk.Label("Existing Message Type")
    nameLabel = Gtk.Label("Message Type Name")
    fieldVPLabel = Gtk.Label("Message Type Field\n"
                             "Value Pair(s)")

    # drop down menu
    # TODO HAVE TO ESTABLISH THE INSIDE OF THE DROPDOWN
    typeCombo = Gtk.ComboBox()

    # text boxes
    nameEntry = Gtk.Entry()
    fieldVPEntry = Gtk.Entry()

    # bottom buttons
    buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    #buttonBox.set_homogeneous(True)
    buttonBox.set_spacing(5)
    saveBtn = Gtk.Button(label="Save")
    deleteBtn = Gtk.Button(label="Delete")
    clearBtn = Gtk.Button(label="Clear")
    buttonBox.pack_start(saveBtn, True, True, 0)
    buttonBox.pack_start(deleteBtn, True, True, 0)
    buttonBox.pack_start(clearBtn, True, True, 0)

    #grid
    messageTypeGrid = Gtk.Grid()
    messageTypeGrid.set_column_spacing(10)
    messageTypeGrid.set_row_spacing(5)

    messageTypeGrid.add(typeLabel)
    messageTypeGrid.attach_next_to(typeCombo, typeLabel, Gtk.PositionType.RIGHT, 1, 1)
    messageTypeGrid.attach_next_to(nameLabel, typeLabel, Gtk.PositionType.BOTTOM, 1, 1)
    messageTypeGrid.attach_next_to(nameEntry, nameLabel, Gtk.PositionType.RIGHT, 1, 1)
    messageTypeGrid.attach_next_to(fieldVPLabel, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)
    messageTypeGrid.attach_next_to(fieldVPEntry, fieldVPLabel, Gtk.PositionType.RIGHT, 1, 1)
    messageTypeGrid.attach_next_to(buttonBox, fieldVPEntry, Gtk.PositionType.BOTTOM, 2, 1)

    mainBox.pack_start(instructions, True, True, 0)
    mainBox.pack_start(messageTypeGrid,True,True,0)

    return mainBox
