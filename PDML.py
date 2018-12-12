#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:06:56 2018

@author: Jessica Dozal
"""
import xml.etree.ElementTree as ET
import Packet

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
    
    def parse(self, path):
        print(path)
        tree = ET.parse(path + "/Session1/" + self.name)
        root = tree.getroot()
        # Getting all the packets 
        for child in root:
            # Creating current packet object
            currPacket = Packet.Packet('','',ET.tostring(child, encoding='utf8').decode('utf8'))
            # adding to packetlist
            self.packetList.append(currPacket)
    
         
