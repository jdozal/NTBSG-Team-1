#!/usr/bin/env python2

import Tag 

class Workspace:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.sessions = []
        self.tagContainer = Tag.TagContainer() 
        self.pcap = ''
        #os.mkdir()

    def addSession(self, session):
        self.sessions.append(session)

    def setPCAP(self, pcap):
        self.pcap = pcap
        
    def getListSession(self):
        a = [[0] * len(self.sessions)] * len(self.sessions)
        i = 0
        for session in self.sessions:
            print(i)
            a[i][0] = session.name
            for pdml in session.pdmls:
                a[i].append([pdml.name, False])
            i = i + 1

	# @property
 #    def name(self):
 #        return self.__name
 #    @name.setter
 #    def name(self, name):
 #        self.__name = name

 #    @property
 #    def path(self):
 #        return self.__path
 #    @path.setter
 #    def path(self, path):
 #        self.__path = path

 #    def update(self, name, path):
 #        if(name != 0 and path != 0):
 #            self.name = name
 #            self.path = path
 #        if(name != 0):
 #            self.name = name
 #        else:
 #            self.path = path

   # def makeFolder(self, length):

  #   def createDirectory(self, path):
  #       try:
  #   		# Create target Directory
  #   		os.mkdir(path)
  #   		print("Directory " , path ,  " Created ") 
		# except FileExistsError:
  #   		print("Directory " , path ,  " already exists")