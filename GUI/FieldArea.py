#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FieldArea:

    def on_cell_toggled(self, widget, path):

        self.fieldListStore[path][0] = not self.fieldListStore[path][0]

    def Tabs(self):
        self.fieldList = [(False, 'icmp.type', 'Type 8 (Echo(ping) request)', '1', 34, '8', '08', 2),
                     (False, 'icmp.code', 'Code 0', '1', 35, '0x00', '00', 2),
                     (False, 'icmp.checksum', 'Checksum: 0x6861 (correct)', '0x00', 36, '0x6861', '6861', 0),
                     (False, 'icmp.ident', 'Identifier: 0x809e', '2', 38, '0x809e', '809e', 2),
                     (False, 'icmp.seq', 'Sequence number: 0x0f00', '2', 40, '0x0f00', '0f00', 2)]
        self.titles = ['Fieldname', 'Showname', 'Size', 'Position', 'Show', 'Value', 'Entropy']
        self.fieldListStore = Gtk.ListStore(bool, str, str, str, int, str, str, int)


        fieldAreaBox = Gtk.Box()
        fieldAreaBox.set_homogeneous(True)

        # List box for area
        fieldBox = Gtk.ListBox()

        fieldAreaBox.add(fieldBox)

        # Box for title
        titleBox = Gtk.Box()
        labelTitle = Gtk.Label()
        labelTitle.set_markup("<u>Field Area</u>")

        titleBox.set_child_packing(labelTitle, True, True, 100,0)
        titleBox.add(labelTitle)

        fieldBox.add(titleBox)

        # Setting up the grid in which the list will be contained
        grid = Gtk.Grid()
        #grid.set_column_homogeneous(True)
        #grid.set_row_homogeneous(True)
        grid.set_hexpand(True);
        fieldBox.add(grid)

        # Creating the ListStore model
        # field list was hardcoded
        # for field_ref in fieldList:
        #     self.fieldListStore.append(list(field_ref))

        # Creating the treeview
        treeview = Gtk.TreeView(self.fieldListStore)

        # adding checkbox
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_cell_toggled)

        column_toggle = Gtk.TreeViewColumn(" ", renderer_toggle, active=0)
        treeview.append_column(column_toggle)

        # adding other columns
        for i, column_title in enumerate(self.titles):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i+1)
            treeview.append_column(column)

        scrollable_treelist = Gtk.ScrolledWindow()
        scrollable_treelist.set_min_content_width(500)
        scrollable_treelist.set_min_content_height(300)

        #scrollable_treelist.set_vexpand(True)
        scrollable_treelist.add(treeview)

        grid.attach(scrollable_treelist, 0, 0, 2, 2)
        #print(fieldBox.size_request().width)

        # Select all checkbox
        selectAll = Gtk.CheckButton("Select all fields")

        editableFields = Gtk.Label("Field Name, Showname, Value, and Length are editable fields")

        grid.attach_next_to(selectAll, scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(editableFields, selectAll, Gtk.PositionType.RIGHT, 1, 1)

        return fieldAreaBox