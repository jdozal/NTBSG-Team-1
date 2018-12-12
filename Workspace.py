
class Workspace():
	def __init__(self, name, path):
		self.name = name
		self.path = path
		self.sessions = []
		os.mkdir(path)

	@property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self, path):
        self.__path = path

    def update(self, name, path):
        if(name != 0 and path != 0):
            self.name = name
            self.path = path
        if(name != 0):
            self.name = name
        else:
            self.path = path

    def addSession(self, session):
    	self.sessions.append(session)

    def createDirectory(self, path):
    	try:
    		# Create target Directory
    		os.mkdir(path)
    		print("Directory " , path ,  " Created ") 
		except FileExistsError:
    		print("Directory " , path ,  " already exists")