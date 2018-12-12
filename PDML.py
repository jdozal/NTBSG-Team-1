#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:06:56 2018

@author: Jessica Dozal
"""
import xml.etree.ElementTree as ET
import Packet
import FilterContainer

class PDML:
    def __init__(self):

        self.name = ''
        self.timeStamp = ''
        self.analystName = ''
        self.date = ''
        self.stage = ''
        self.packetList = []

        
    def setName(self, name):
        self.name = name
        print(self.name)
    
    def parse(self, path, filterT):
        print(path)
        tree = ET.parse(path + "/Session1/" + self.name)
        newFile = self.filterOut(path, filterT, tree)
        tree = ET.parse(newFile)
        root = tree.getroot()
        # Getting all the packets 
        for child in root:
            # Creating current packet object
            currPacket = Packet.Packet('','',ET.tostring(child, encoding='utf8').decode('utf8'))
            # adding to packetlist
            self.packetList.append(currPacket)

    # TODO FIGURE OUT THE FILTERING OF PROTOCOLS
    def filterOut(self, path, filterT, tree):
        root = tree.getroot()
        for packet in root.iter("packet"):
            # Creating current packet object
            for proto in packet.findall("proto"):
                if proto.get('name') != filterT:
                    packet.remove(proto)
            #root.remove(packet)
        newPath = (path + "/Session1/" + filterT + "applied.pdml")
        tree.write(newPath)
        return newPath
