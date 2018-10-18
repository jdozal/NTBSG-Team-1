#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

fieldList=[(False,'icmp.type','Type 8',1,34,8,'08',2),
           (False,'icmp.type','Type 8',1,34,8,'08',2)]
titles=['Fieldname','Showname', 'Size', 'Position', 'Show','Value','Entropy']
fieldListStore = Gtk.ListStore(bool,str, str, int , int, int, str, int)

def on_cell_toggled(widget, path):
        fieldListStore[path][0] = not fieldListStore[path][0]
        
def Tabs():
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
    for field_ref in fieldList:
        fieldListStore.append(list(field_ref))

    # Creating the treeview
    treeview = Gtk.TreeView(fieldListStore)
    
    # adding checkbox
    renderer_toggle = Gtk.CellRendererToggle()
    renderer_toggle.connect("toggled", on_cell_toggled)
    
    column_toggle = Gtk.TreeViewColumn(" ", renderer_toggle, active=0)
    treeview.append_column(column_toggle)
    
    # adding other columns 
    for i, column_title in enumerate(titles):
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(column_title, renderer, text=i+1)
        treeview.append_column(column)
    
    scrollable_treelist = Gtk.ScrolledWindow()
    scrollable_treelist.set_min_content_width(550)
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