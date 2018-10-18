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
    notebook.append_page(newPage, Gtk.Label("New/Modify"))

    #Dependency Page
    dependencyPage = Gtk.Box()
    dependencyPage.set_border_width(10)
    dependencyPage.add(dependency())
    notebook.append_page(dependencyPage, Gtk.Label("Dependency"))

    #Template Page
    templatePage = Gtk.Box()
    templatePage.set_border_width(10)
    templatePage.add(template())
    notebook.append_page(templatePage, Gtk.Label("Template"))

    #Equivalency Page
    equivalencyPage = Gtk.Box()
    equivalencyPage.set_border_width(10)
    equivalencyPage.add(equivalency())
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

    #checkboxes
    hbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
    #hbox.setSpacing(5)

    fieldValueBtn = Gtk.CheckButton("Select both field name and value")
    hbox.pack_start(fieldValueBtn, True, True, 0)

    fOnlyButton = Gtk.CheckButton("Select field name only")
    hbox.pack_start(fOnlyButton, True, True, 0)

    messageTypeGrid.add(typeLabel)
    messageTypeGrid.attach_next_to(typeCombo, typeLabel, Gtk.PositionType.RIGHT, 1, 1)
    messageTypeGrid.attach_next_to(nameLabel, typeLabel, Gtk.PositionType.BOTTOM, 1, 1)
    messageTypeGrid.attach_next_to(nameEntry, nameLabel, Gtk.PositionType.RIGHT, 1, 1)
    messageTypeGrid.attach_next_to(fieldVPLabel, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)
    messageTypeGrid.attach_next_to(fieldVPEntry, fieldVPLabel, Gtk.PositionType.RIGHT, 1, 1)
    messageTypeGrid.attach_next_to(buttonBox, fieldVPEntry, Gtk.PositionType.BOTTOM, 1, 1)
    messageTypeGrid.attach_next_to(hbox, fieldVPLabel, Gtk.PositionType.BOTTOM, 1, 1)

    mainBox.pack_start(instructions, True, True, 0)
    mainBox.pack_start(messageTypeGrid, True, True,0)

    return mainBox

def dependency():
    dependencyBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    #labels
    typeLabel = Gtk.Label("Existing Message Type")
    fieldSizeLabel = Gtk.Label("Size of field")
    packetSizeLabel = Gtk.Label("Size of packet")
    checksumLabel = Gtk.Label("Checksum")
    #for some reason I can't use the same label on 3 differenf boxes
    dependsLabel = Gtk.Label(" depends on ")
    dependsLabel2 = Gtk.Label(" depends on ")
    dependsLabel3 = Gtk.Label(" depends on ")

    # drop down menu
    # TODO HAVE TO ESTABLISH THE INSIDE OF THE DROPDOWN
    typeCombo = Gtk.ComboBox()

    # text boxes
    #first box
    nameEntry = Gtk.Entry()
    nameEntry.set_placeholder_text("Field Name")
    nameEntry2 = Gtk.Entry()
    #second box
    nameEntry3 = Gtk.Entry()
    packetEntry = Gtk.Entry()
    #third box
    packetEntry2 = Gtk.Entry()
    fieldNamesEntry = Gtk.Entry()

    #button
    cycleBtn = Gtk.Button(label="Cycle Through Packets")

    #grid
    dependencyGrid = Gtk.Grid()
    dependencyGrid.set_column_spacing(10)
    dependencyGrid.set_row_spacing(5)

    #containers "depends on"
    firstbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    firstbox.pack_start(nameEntry, True, True, 0)
    firstbox.pack_start(dependsLabel, True, True, 0)
    firstbox.pack_start(nameEntry2, True, True, 0)

    secondbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    secondbox.pack_start(nameEntry3, True, True, 0)
    secondbox.pack_start(dependsLabel2, True, True, 0)
    secondbox.pack_start(packetEntry, True, True, 0)

    thirdbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    thirdbox.pack_start(packetEntry2, True, True, 0)
    thirdbox.pack_start(dependsLabel3, True, True, 0)
    thirdbox.pack_start(fieldNamesEntry, True, True, 0)

    #save and clear buttons at the bottom of the form
    buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    buttonBox.set_spacing(5)
    saveBtn = Gtk.Button(label="Save")
    clearBtn = Gtk.Button(label="Clear")
    buttonBox.pack_start(saveBtn, True, True, 0)
    buttonBox.pack_start(clearBtn, True, True, 0)

    dependencyGrid.add(typeLabel)
    dependencyGrid.attach_next_to(typeCombo, typeLabel, Gtk.PositionType.RIGHT, 1, 1)
    dependencyGrid.attach_next_to(cycleBtn, typeCombo, Gtk.PositionType.BOTTOM, 1, 1)
    dependencyGrid.attach_next_to(firstbox, cycleBtn, Gtk.PositionType.BOTTOM, 1, 1)
    dependencyGrid.attach_next_to(fieldSizeLabel, firstbox, Gtk.PositionType.LEFT, 1, 1)
    dependencyGrid.attach_next_to(secondbox, firstbox, Gtk.PositionType.BOTTOM, 1, 1)
    dependencyGrid.attach_next_to(packetSizeLabel, secondbox, Gtk.PositionType.LEFT, 1, 1)
    dependencyGrid.attach_next_to(checksumLabel, packetSizeLabel, Gtk.PositionType.BOTTOM, 1, 1)
    dependencyGrid.attach_next_to(thirdbox, checksumLabel, Gtk.PositionType.RIGHT, 1, 1)
    dependencyGrid.attach_next_to(buttonBox, thirdbox, Gtk.PositionType.BOTTOM, 1, 1)

    #add to dependency page (box)
    dependencyBox.pack_start(dependencyGrid, True, True, 0)

    return dependencyBox

def template():
    templateBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    #labels
    typeLabel = Gtk.Label("Existing Message Type")
    listValuePairsLabel = Gtk.Label("Message Type Template \nFields Value Pair(s)")

    # drop down menu
    # TODO HAVE TO ESTABLISH THE INSIDE OF THE DROPDOWN
    typeCombo = Gtk.ComboBox()

    #button
    cycleBtn = Gtk.Button(label="Cycle Through Packets")

    #entry
    listValuePairsEntry = Gtk.Entry()
    listValuePairsEntry.set_placeholder_text("List of Field Value Pair(s)")

    #save and clear buttons at the bottom of the form
    buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    buttonBox.set_spacing(5)
    saveBtn = Gtk.Button(label="Save")
    clearBtn = Gtk.Button(label="Clear")
    buttonBox.pack_start(saveBtn, True, True, 0)
    buttonBox.pack_start(clearBtn, True, True, 0)

    #grid
    templateGrid = Gtk.Grid()
    templateGrid.set_column_spacing(10)
    templateGrid.set_row_spacing(5)

    #construct grid
    templateGrid.add(typeLabel)
    templateGrid.attach_next_to(typeCombo, typeLabel, Gtk.PositionType.RIGHT, 1, 1)
    templateGrid.attach_next_to(cycleBtn, typeCombo, Gtk.PositionType.BOTTOM, 1, 1)
    templateGrid.attach_next_to(listValuePairsEntry, cycleBtn, Gtk.PositionType.BOTTOM, 1, 1)
    templateGrid.attach_next_to(listValuePairsLabel, listValuePairsEntry, Gtk.PositionType.LEFT, 1, 1)
    templateGrid.attach_next_to(buttonBox, listValuePairsEntry, Gtk.PositionType.BOTTOM, 1, 1)

    #add to main template page (box)
    templateBox.pack_start(templateGrid, True, True, 0)

    return templateBox

def equivalency():
    equivalencyBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)