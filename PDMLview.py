#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:19:42 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def pdmlDesign():
    pdmlViewCol = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    thisListBox = Gtk.ListBox()
    pdmlViewCol.add(thisListBox)

    # title "PDML View" area
    titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
    labelPDML = Gtk.Label("PDML View")
    titleBox.add(labelPDML)
    titleBox.set_child_packing(labelPDML, 1, 1, 350, 0)

    # pdml view header
    headerTab = pdmlHeader()

    # filter area
    filterTab = filterArea()

    # packet area
    #packetTab = self.packetArea()

    # bottom pdml view
    #bottomTab = self.bottomArea()

    thisListBox.add(titleBox)
    thisListBox.add(headerTab)
    thisListBox.add(filterTab)
    #thisListBox.add(packetTab)
    #thisListBox.add(bottomTab)

    return pdmlViewCol

def pdmlHeader():
    header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    # TODO fix spacing

    # text boxes
    newStateNameEntry = Gtk.Entry()
    renameCurrentEntry = Gtk.Entry()

    # buttons
    saveNewBtn = Gtk.Button(label="Save as New\nPDML State")
    saveCurrentBtn = Gtk.Button(label="Save Current\nPDML State")
    closeCurrentBtn = Gtk.Button(label="Close Current\nPDML State")
    deleteCurrentBtn = Gtk.Button(label="Delete Current\nPDML State")
    renameCurrentBtn = Gtk.Button(label="Rename Current\nPDML State")

    header.add(newStateNameEntry)
    header.add(saveNewBtn)
    header.add(saveCurrentBtn)
    header.add(closeCurrentBtn)
    header.add(deleteCurrentBtn)
    header.add(renameCurrentEntry)
    header.add(renameCurrentBtn)

    return header

def filterArea():
    filterTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    grid = Gtk.Grid()
    filterTab.add(grid)
    lineBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


    # labels
    nameLabel = Gtk.Label()
    nameLabel.set_markup("<u>Filter Area</u>")
    nameLabel.set_justify(Gtk.Justification.LEFT)
    filterLabel = Gtk.Label("Filter")

    # buttons
    applyNewBtn = Gtk.Button("Apply")
    clearBtn = Gtk.Button("Clear")
    saveBtn = Gtk.Button("Save")
    applyFilterBtn = Gtk.Button("Apply")

    # text box (entry)
    newFilter = Gtk.Entry()

    # drop down
    # TODO HAVE TO ESTABLISH THE filters saved OF THE DROPDOWN
    savedFilters = Gtk.ComboBox()

    # adding second line into box
    lineBox.add(filterLabel)
    lineBox.pack_start(newFilter, True, True, 5)
    lineBox.pack_start(applyNewBtn, True, True, 5)
    lineBox.pack_start(clearBtn, True, True, 5)
    lineBox.pack_start(saveBtn, True, True, 5)
    lineBox.pack_start(savedFilters, True, True, 5)
    lineBox.pack_start(applyFilterBtn, True, True, 5)

    # adding to grid
    grid.add(nameLabel)
    grid.attach_next_to(lineBox, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)

    return filterTab
