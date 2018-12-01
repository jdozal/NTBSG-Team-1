
class MessageTemplate:
    def __init__(self, name, destinationName, destinationPath, outputFormat):
        self.name = name
        self.destinationName = destinationName
        self.destinationPath = destinationPath
        self.outputFormat = outputFormat

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def destinationName(self):
        return self.__destinationName
    @destinationName.setter
    def destinationName(self, destinationName):
        self.__destinationName = destinationName

    @property
    def destinationPath(self):
        return self.__destinationPath
    @destinationPath.setter
    def targetMessageType(self, destinationPath):
        self.__destinationPath = destinationPath

    @property
    def outputFormat(self):
        return self.__outputFormat
    @outputFormat.setter
    def outputFormat(self, outputFormat):
        self.__outputFormat = outputFormat