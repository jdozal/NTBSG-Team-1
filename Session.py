#import PDML, Workspace
import os

class Session:
	def __init__(self, name, description, path):
		self.name = name
		self.description = description
		self.pdmls = []
		os.mkdir(path + "/" + self.name)

	def addPDML(self, pdml):
		self.pdmls.append(pdml)

	def getLatest(self):
		return self.pdmls[len(self.pdmls)-1]