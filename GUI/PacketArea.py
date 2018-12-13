#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:15:16 2018

@author: Jessica Dozal
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import sys
sys.path.append('../')
from Workspace import Workspace

class PacketArea:

    def Tabs(self, workspace):
        currentWorkspace = workspace
        packetTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        grid = Gtk.Grid()
        packetTab.pack_start(grid, True, True, 5)

        # name of area
        nameLabel = Gtk.Label()
        nameLabel.set_markup("<u>Packet Area</u>")
        grid.add(nameLabel)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox.store = Gtk.TreeStore(str, bool)

        print(workspace.sessions[0].isEmpty())
           #code = self.createPDMLview(workspace.sessions[0].getLatest())

        # for i in range(len(code)):
        #         #     piter = hbox.store.append(None, [code[i][0], False])
        #         #
        #         #     j=1
        #         #     while j < len(code[i]):
        #         #         hbox.store.append(piter, code[i][j])
        #         #         j += 1

        view = Gtk.TreeView()
       # view.set_model(hbox.store)

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

    def createPDMLview(self, pdml):
        fields = []
        protocols = []
        packets = []
        import xml.etree.ElementTree as ET
        tree = ET.parse(pdml.name)
        root = tree.getroot()
        for packet in root.findall("packet"):
            proto = packet.find("proto")
            protocols = []
            if(proto != null):
                protocols.append(proto)
                fields = []
                for field in proto.findall("field"):
                    fields.append(field)
                protocols.append(fields)
            packets.append(protocols)
            #print name.text
            #for char in actor.findall('{http://characters.example.com}character'):
             #   print ' |-->', char.text