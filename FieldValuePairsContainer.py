import FieldValuePair

class FieldValuePairsContainer:
    def __init__(self):
        self.fieldValuePairsList = []

    @property
    def fieldValuePairsList(self):
        return self.__fieldValuePairsList


    def createFieldValuePair(self, fieldName, fieldValue):
        tempObject = FieldValuePair.__init__(fieldName, fieldValue)
        self.__addToContainer(tempObject)

    def updateFieldValuePair(self, index, fieldName, fieldValue):
        self.fieldValuePairsList[index].update(fieldName, fieldValue)


    def addToContainer(self, fieldValuePair):
        self.fieldValuePairsList.append(fieldValuePair)

    def deleteFromContainer(self, index):
        del(self.fieldValuePairsList[index])