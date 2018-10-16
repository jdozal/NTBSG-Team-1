#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

code = [("Frame 718: frame, eth, ip, tcp", 74),
        ("   Frame 718: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface 0", 20),
        ("   Ethernet II, Src: Elitegro_dd:12:cd (00:19:21:dd:12:cd), Dst: Broadcom_de:ad:05 (00:10:18:de:ad:05)", 25),
        ("   Internet Control Message Protocol", 25),
        ("   Transmission Control Protocol, Src Port: 55394 (55394), Dst Port: 80, Seq: 0, Len: 0", 25),
        ("Frame 767: frame, eth, ip, tcp", 0),
        ("Frame 768: frame, eth, ip, tcp", 0),
        ("Frame 769: frame, eth, ip, tcp, http", 0)]

def Tabs():
    packetTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    grid = Gtk.Grid()
    packetTab.add(grid)

    # name of area
    nameLabel = Gtk.Label()
    nameLabel.set_markup("<u>Packet Area</u>")
    grid.add(nameLabel)

    # initializing box where packet will be
    panelGrid = Gtk.Grid()
    grid.attach_next_to(panelGrid, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)

    # left hand side where packet code is
    codeBox = Gtk.Box()
    panelGrid.add(codeBox)

    # Convert data to liststore (to display on treeviews)
    code_list = Gtk.ListStore(str, int)
    for item in code:
        code_list.append(list(item))

    # TreeView
    code_tree = Gtk.TreeView(code_list)

    for i, col_title in enumerate(["Frame", "Size"]):
        # how to draw the data
        renderer = Gtk.CellRendererText()

        # create columns
        column = Gtk.TreeViewColumn(col_title, renderer, text=i)

        # add columns
        code_tree.append_column(column)

    # add treeview
    codeBox.add(code_tree)

    # right hand side buttons
    btnBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    panelGrid.attach_next_to(btnBox, codeBox, Gtk.PositionType.RIGHT, 1, 1)

    removeBtn = Gtk.Button(label="Remove")
    clearBtn = Gtk.Button(label="Clear")
    btnBox.pack_end(clearBtn, True, True, 1)
    btnBox.pack_end(removeBtn, True, True, 1)

    return packetTab