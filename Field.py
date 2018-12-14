#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

class Field:    
    
    def __init__(self, name, showname, size, pos, show, value, plainXML):
        self.name = name
        self.showname = showname
        self.size = size
        self.pos = pos
        self.show = show
        self.value = value
        self.plainXML = plainXML
        # Testing purposes
        #print(self.name)        


