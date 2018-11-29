
class FieldValuePair:
    def __init__(self, fieldName, fieldValue):
        self.fieldName = fieldName
        self.fieldValue = fieldValue

    @property
    def fieldName(self):
        return self.__fieldName
    @fieldName.setter
    def fieldName(self, fieldName):
        self.__fieldName = fieldName

    @property
    def fieldValue(self):
        return self.__fieldValue
    @fieldValue.setter
    def color(self, fieldValue):
        self.__fieldValue = fieldValue


    def update(self, fieldName, fieldValue):
        if(fieldName != 0 and fieldValue != 0):
            self.fieldName(fieldName)
            self.fieldValue(fieldValue)
        if(fieldName != 0):
            self.fieldName(fieldName)
        else:
            self.fieldValue(fieldValue)