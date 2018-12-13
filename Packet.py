#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import Protocol

class Packet:    
    
    def __init__(self, name, size, plainXML):
        self.name = name
        self.size = size
        self.plainXML = plainXML
        # Testing purposes 
        #print(plainXML)
        self.protoList = []
        self.parseProto()
    
    def parseProto(self):
        tree = ET.ElementTree(ET.fromstring(self.plainXML))
        root = tree.getroot()
        # Getting all the protocols 
        for child in root:
            # Attributes of protocol
            protoName = child.get("name")
            protoShowname = child.get("showname")
            protoSize = child.get("size")
            protoPos = child.get("pos")
            protoValue = child.get("value")
            protoShow = child.get("show")
            plainXML = ET.tostring(child, encoding='utf8').decode('utf8')
            currProto = Protocol.Protocol(protoName, protoShowname, protoSize, 
                                          protoPos, protoShow, protoValue, plainXML)  
            self.protoList.append(currProto)

    #def print(self):
     #   return <proto name="icmp" pos="34" showname="Internet Control Message Protocol" size="36">