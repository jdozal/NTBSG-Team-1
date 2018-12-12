import PDML, Workspace

class Session:
	def __init__(self, name, description):
		self.name = name
        self.description = description
        self.pdmls = []
        os.mkdir()

    def addPDML(self, pdml):
    	self.pdmls.append(pdml)
