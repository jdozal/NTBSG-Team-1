
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import Field

class Protocol:    
    
    def __init__(self, name, showname, size, pos, show, value, plainXML):
        self.name = name
        self.showname = name
        self.size = size
        self.pos = size
        self.show = size
        self.value = size
        self.plainXML = plainXML
        # Testing purposes 
        #print(plainXML)
        self.fieldList = []
        self.parseFields()
    
    def parseFields(self):
            tree = ET.ElementTree(ET.fromstring(self.plainXML))
            root = tree.getroot()
            # Getting all the fields 
            for child in root:
                # Attributes of field
                fieldName = child.get("name")
                fieldShowname = child.get("showname")
                fieldSize = child.get("size")
                fieldPos = child.get("pos")
                fieldValue = child.get("value")
                fieldShow = child.get("show")
                plainXML = ET.tostring(child, encoding='utf8').decode('utf8')
                currField = Field.Field(fieldName, fieldShowname, fieldSize, 
                                              fieldPos, fieldShow, fieldValue, plainXML)  
                self.fieldList.append(currField)


