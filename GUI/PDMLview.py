#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:19:42 2018

@author: Jessica Dozal

"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import MessageTypeArea, PacketArea, FieldArea

import sys
sys.path.append('../')
from Workspace import Workspace 
from FilterContainer import FilterContainer
import PCAP
import Dissector 
import PDML

class PDMLview:

    currentWorkspace = Workspace("","")

    def pdmlDesign(self, workspace):
        currentWorkspace = workspace
        # Starting box for pdmlView
        pdmlBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        pdmlBox.set_homogeneous(True)

        # Starting list box for pdmlVire
        pdmlListBox = Gtk.ListBox()

        # Adding listbox to box
        pdmlBox.add(pdmlListBox)

        # title "PDML View" area
        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        labelPDML = Gtk.Label("PDML View")
        titleBox.add(labelPDML)
        # child is packed into box (item, expand, fill, padding, packtype)
        titleBox.set_child_packing(labelPDML, True, True, 100, 0)
        # Homogeneous
        titleBox.set_homogeneous(True)
        # Adding into primary list box
        pdmlListBox.add(titleBox)

        # pdml menu
        menu = self.pdmlMenu()
        pdmlListBox.add(menu)

        # filter area
        filterTab = self.filterArea(currentWorkspace)
        pdmlListBox.add(filterTab)
        # grid.add(filterTab)

        # pdmlListBox.add(grid)

        # packet area
        pckt = PacketArea.PacketArea()
        packetArea = pckt.Tabs(currentWorkspace)
        # grid.add(packetArea)
        pdmlListBox.add(packetArea)

        bottomPart = self.bottomPDMLView()
        pdmlListBox.add(bottomPart)

        #thisListBox.add(packetTab)
        #thisListBox.add(bottomTab)

        return pdmlBox

    def pdmlMenu(self):
        header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        # WARNING THIS BREAKS LAYOUT
        #header.set_homogeneous(True)

        # text boxes
        newStateNameEntry = Gtk.Entry()
        newStateNameEntry.set_placeholder_text("New PDML State Name")

        renameCurrentEntry = Gtk.Entry()
        renameCurrentEntry.set_placeholder_text("Rename Current PDML State Name")


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


    def filterArea(self, currentWorkspace):

        # Starting box for filter
        filterBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        filterBox.set_homogeneous(True)

        # Starting list box for title
        filterListBox = Gtk.ListBox()

        # Adding listbox to box
        filterBox.add(filterListBox)

        # title "PDML View" area
        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        labelTitle = Gtk.Label()
        labelTitle.set_markup("<u>Filter Area</u>")
        labelTitle.set_justify(Gtk.Justification.LEFT)
        titleBox.add(labelTitle)
        # child is packed into box (item, expand, fill, padding, packtype)
        titleBox.set_child_packing(labelTitle, True, True, 0, 0)
        # Adding into primary list box
        filterListBox.add(titleBox)


        # Starting second row
        lineBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        #nameLabel.set_justify(Gtk.Justification.LEFT)
        filterLabel = Gtk.Label("Filter")

        # buttons
        applyNewBtn = Gtk.Button("Apply")
        clearBtn = Gtk.Button("Clear")
        saveBtn = Gtk.Button("Save")
        applyFilterBtn = Gtk.Button("Apply")

        # text box (entry)
        newFilter = Gtk.Entry()
        newFilter.set_placeholder_text("Filter Expression")

        # drop down
        # TODO HAVE TO ESTABLISH THE filters saved OF THE DROPDOWN
        filters = FilterContainer()
        filter_store = Gtk.ListStore(str)
        for filterT in filters.filterList:
                filter_store.append([filterT])
        savedFilters = Gtk.ComboBox().new_with_model(filter_store)

        #savedFilters.connect("changed", self.on_filter_combo_changed)
        renderer_text = Gtk.CellRendererText()
        savedFilters.pack_start(renderer_text, True)
        savedFilters.add_attribute(renderer_text, "text", 0)

    #    # adding second line into box
        lineBox.add(filterLabel)
        lineBox.pack_start(newFilter, True, True, 10)
        lineBox.pack_start(applyNewBtn, True, True, 0)
        lineBox.pack_start(clearBtn, True, True, 0)
        lineBox.pack_start(saveBtn, True, True, 0)
        lineBox.pack_start(savedFilters, True, True, 0)
        lineBox.pack_start(applyFilterBtn, True, True, 0)

        applyFilterBtn.connect("clicked", self.on_filter_apply_clicked, savedFilters, currentWorkspace)

        filterListBox.add(lineBox)

        return filterBox

    def on_filter_apply_clicked(self, widget, combo, workspace):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            filterT = model[tree_iter][0]
            #print("Selected: filter=%s" % filterT)
        dissector = Dissector.Dissector("", "")
        pdml = PDML.PDML()
        namePDML = dissector.convert(workspace.pcap, workspace.path)
        pdml.setName(namePDML)
        pdml.parse(workspace.path, filterT)
        workspace.sessions[0].addPDML(pdml)
        

    def bottomPDMLView(self):
        box = Gtk.Box()
        grid = Gtk.Grid()
        box.add(grid)

        # Field Area
        fieldArea = FieldArea.Tabs()
        grid.attach(fieldArea,0,1,1,1)

        # Message Type Area
        mta = MessageTypeArea.MessageTypeArea()
        messTypeArea = mta.Tabs()
        grid.attach(messTypeArea,2,1,1,1)

        buttonBox = Gtk.VBox()
        plusButton = Gtk.Button("+")
        minusButton = Gtk.Button("-")
        buttonBox.add(plusButton)
        buttonBox.add(minusButton)
        grid.attach(buttonBox, 1, 1, 1, 1)

        return box

