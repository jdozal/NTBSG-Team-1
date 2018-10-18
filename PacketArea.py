#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

code = [["Frame 718: frame, eth, ip, tcp",
        ["Frame 718: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface 0", False],
        ["Ethernet II, Src: Elitegro_dd:12:cd (00:19:21:dd:12:cd), Dst: Broadcom_de:ad:05 (00:10:18:de:ad:05)", False],
        ["Internet Control Message Protocol", False],
        ["Transmission Control Protocol, Src Port: 55394 (55394), Dst Port: 80, Seq: 0, Len: 0", False]],
        ["Frame 767: frame, eth, ip, tcp", ["code", False]],
        ["Frame 768: frame, eth, ip, tcp", ["code", False]],
        ["Frame 769: frame, eth, ip, tcp, http", ["code", False]]
        ]

def Tabs():
    packetTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    grid = Gtk.Grid()
    packetTab.pack_start(grid, True, True, 5)

    # name of area
    nameLabel = Gtk.Label()
    nameLabel.set_markup("<u>Packet Area</u>")
    grid.add(nameLabel)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox.store = Gtk.TreeStore(str, bool)

    for i in range(len(code)):
        piter = hbox.store.append(None, [code[i][0], False])

        j=1
        while j < len(code[i]):
            hbox.store.append(piter, code[i][j])
            j += 1

    view = Gtk.TreeView()
    view.set_model(hbox.store)

    renderer = Gtk.CellRendererToggle()
    column_in_size = Gtk.TreeViewColumn("", renderer, active=1)
    view.append_column(column_in_size)

    renderer_frame = Gtk.CellRendererText()
    column_frame = Gtk.TreeViewColumn("Frame", renderer_frame, text=0)
    view.append_column(column_frame)

    renderer_in_size = Gtk.CellRendererText()
    column_in_size = Gtk.TreeViewColumn("Size", renderer_in_size, text=1)
    view.append_column(column_in_size)

    # initializing box where packet will be
    scroll_window = Gtk.ScrolledWindow()
    grid.attach_next_to(scroll_window, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)

    # left hand side where packet code is
    # codeBox = Gtk.Box()
    # grid.add(scroll_window)

    #
    # # Convert data to liststore (to display on treeviews)
    # code_list = Gtk.ListStore(str, int, bool)
    # for item in range(len(code)):
    #     code_list.append(code[item])
    #
    # # TreeView
    # code_tree = Gtk.TreeView(model=code_list)
    # cell1=Gtk.CellRendererToggle()
    # col1=Gtk.TreeViewColumn("", cell1, active=1)
    # code_tree.append_column(col1)
    #
    # for i, col_title in enumerate(["Frame", "Size"]):
    #     # how to draw the data
    #     renderer = Gtk.CellRendererText()
    #
    #     if i==0:
    #         renderer.props.weight_set = True
    #
    #     # create columns
    #     column = Gtk.TreeViewColumn(col_title, renderer, text=i)
    #
    #     # add columns
    #     code_tree.append_column(column)
    #
    # # add treeview
    # # code_tree.get_selection().connect("changed", self.on_changed)
    # # codeBox.add(code_tree)
    scroll_window.add(view)

    scroll_window.set_min_content_width(1000)
    scroll_window.set_min_content_height(200)

    # right hand side buttons
    btnBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    grid.attach_next_to(btnBox, scroll_window, Gtk.PositionType.RIGHT, 1, 1)

    removeBtn = Gtk.Button(label="Remove")
    clearBtn = Gtk.Button(label="Clear")
    btnBox.pack_end(clearBtn, True, True, 1)
    btnBox.pack_end(removeBtn, True, True, 1)
    

    return packetTab