#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

class Field:    
    
    def __init__(self, name, showname, size, pos, show, value, plainXML):
        self.name = name
        self.showname = name
        self.size = size
        self.pos = size
        self.show = size
        self.value = size
        self.plainXML = plainXML
        # Testing purposes
        print(self.name)        


