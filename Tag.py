#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:09:01 2018

@author: Jessica Dozal
"""

class Tag:
    
    def __init__(self, name, field, annotation):
        self.name = name
        self.field = field
        self.annotation = annotation
        
        
    def changeName(self, name):
        self.name = name
    
    def changeField(self, field):
        self.field = field
    
    def changeAnnotation(self, annotation):
        self.annotation = annotation
        
    def getName(self):
        return self.name
        

        
class TagContainer:
    
    def __init__(self):
        self.tagList = [] 
        self.tag1 = Tag("test tag 1", "Field", "annotation")
        self.tag2 = Tag("test tag 2", "Field 2", "annotation")
        self.addTag(self.tag1)
        self.addTag(self.tag2)
        
    def addTag(self, tag):
        self.tagList.append(tag)
        #for tag in self.tagList:
         #   print(tag.name)
    
    def getList(self):
        return self.tagList
    
    def getTag(self, name):
        for tag in self.tagList:
            if tag.name == name:
                return tag
        return -1