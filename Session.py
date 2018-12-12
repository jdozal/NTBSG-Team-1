#import PDML, Workspace

class Session:
	def __init__(self, name, description, path):
		self.name = name
		self.description = description
		self.pdmls = []
		os.mkdir(path + "/" + self.name)

	def addPDML(self, pdml):
		self.pdmls.append(pdml)