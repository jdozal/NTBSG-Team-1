import MessageType

class MessageTypesContainer:
    def __init__(self):
        self.messageTypesList = []

    @property
    def messageTypesList(self):
        return self.__messageTypesList


    def createMessageType(self, name, color):
        tempObject = MessageType.__init__(name, color)
        self.__addToContainer(tempObject)

    def updateMessageType(self, index, name, color):
        self.messageTypesList[index].update(name, color)


    def addToContainer(self, messageType):
        self.messageTypesList.append(messageType)

    def deleteFromContainer(self, index):
        del(self.messageTypesList[index])

