import Dependency

class Checksum(Dependency):
    def __init__(self, packetName, fieldName):
        self.packetName = packetName
        self.fieldName = fieldName

    @property
    def packetName(self):
        return self.__packetName
    @packetName.setter
    def packetName(self, packetName):
        self.__packetName = packetName

    @property
    def fieldName(self):
        return self.__fieldName
    @fieldName.setter
    def fieldName(self, fieldName):
        self.__fieldName = fieldName