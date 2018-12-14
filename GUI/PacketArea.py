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

class PacketArea(Gtk.Window):

    def __init__(self, workspace):
        Gtk.Window.__init__(self, title="PacketArea")
        pdmlListBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        packetArea = pckt.Tabs(workspace)
        pdmlListBox.add(packetArea)
        bottomPart = self.bottomPDMLView()
        pdmlListBox.add(bottomPart)
        #win.show()

    def Tabs(self, workspace):
        currentWorkspace = workspace
        packetTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        grid = Gtk.Grid()
        packetTab.pack_start(grid, True, True, 5)

        # name of area
        nameLabel = Gtk.Label()
        nameLabel.set_markup("<u>Packet Area</u>")
        grid.add(nameLabel)

        #hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        store = Gtk.TreeStore(str)

        if (workspace.sessions[0].isEmpty()):
            code = []
        else:
            code = self.createPDMLview(workspace.sessions[0].getLatest())

        for i in range(len(code)):
            piter = store.append(None, [code[i][0]])
            
            for j in range(len(code[i])):
                store.append(piter, [code[i][j]])
                
                # for k in range(len(code[i][j])):
                #     store.append(ppiter, [code[i][j][k]])
                    
        print(store)

        view = Gtk.TreeView(store)
        #view.set_model(store)

        col0 = Gtk.TreeViewColumn("PDML")
        self.cell0 = Gtk.CellRendererText()
        view.append_column(col0)
        col0.pack_start(self.cell0, False)
        col0.set_attributes(self.cell0, text=0)




        # renderer = Gtk.CellRendererToggle()
        # column_in_size = Gtk.TreeViewColumn("", renderer, active=1)
        # view.append_column(column_in_size)

        # renderer_frame = Gtk.CellRendererText()
        # column_frame = Gtk.TreeViewColumn("", renderer_frame, text=1)
        # view.append_column(column_frame)

        # renderer_in_size = Gtk.CellRendererText()
        # column_in_size = Gtk.TreeViewColumn("Size", renderer_in_size, text=1)
        # view.append_column(column_in_size)

        # initializing box where packet will be
        scroll_window = Gtk.ScrolledWindow()
        grid.attach_next_to(scroll_window, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)
        scroll_window.add(view)
        view.show()

        scroll_window.set_min_content_width(1200)
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
        
        packetlen = len(pdml.packetList)

        tstr = ''

        for i in range(packetlen):
            packets = []
            tempPacket = pdml.packetList[i]
            tstr = tempPacket.plainXML
            #print(tstr)
            packets.append(tstr)
            protolen = len(tempPacket.protoList)

            if(protolen>0):
                for j in range(protolen):
                    protocols = []
                    tempProto = tempPacket.protoList[j]
                    tstr = tempProto.plainXML
                    #print(tstr)
                    protocols.append(tstr)
                    fieldlen = len(tempProto.fieldList)

                    # if(fieldlen>0):
                    #     for k in range(fieldlen):
                    #         fields = []
                    #         tempField = tempProto.fieldList[k]
                    #         tstr = tempField.plainXML
                    #         #print(tstr)
                    #         fields.append(tstr)
                    # protocols.append(fields)
            packets.append(protocols)

        return packets

        #for i in pdml.packetList:
            #packets.append(pdml.packetList[i].plainXML)
        #print(pdml.packetList[0].plainXML)



        # import xml.etree.ElementTree as ET
        # tree = ET.parse(pdml.name)
        # root = tree.getroot()
        # for packet in root.findall("packet"):
        #     print(packet)
        #     proto = packet.find("name")
        #     print(proto.text)
        #     protocols = []
        #     if(proto is not None):
        #         protocols.append(proto)
        #         fields = []
        #         for field in proto.findall("name"):
        #             print(field.text)
        #             fields.append(field)
        #         protocols.append(fields)
        #     packets.append(protocols)
        # return packets
            #print name.text
            #for char in actor.findall('{http://characters.example.com}character'):
             #   print ' |-->', char.text