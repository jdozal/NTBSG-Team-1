import PDML, Protocol, Dependency

class PacketLengthDependency(Dependency):
    def __init__(self, packetName, fieldName):
        self.packetName = packetName
        self.fieldName = fieldName
        self.packetSize = '' #get with packet name
        self.fieldSize = '' #get with field name

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