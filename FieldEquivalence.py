

class FieldEquivalence:
    def __init__(self, sourceMessageType, sourceFieldName, targetMessageType, targetFieldName):
        self.sourceMesageType = sourceMessageType
        self.sourceFieldName = sourceFieldName
        self.targetMessageType = targetMessageType
        self.targetFieldName = targetFieldName

    @property
    def sourceMessageType(self):
        return self.__sourceMessageType
    @sourceMessageType.setter
    def sourceMessageType(self, sourceMessageType):
        self.__sourceMessageType = sourceMessageType

    @property
    def sourceFieldName(self):
        return self.__sourceFieldName
    @sourceFieldName.setter
    def sourceFieldName(self, sourceFieldName):
        self.__sourceFieldName = sourceFieldName

    @property
    def targetMessageType(self):
        return self.__targetMessageType
    @targetMessageType.setter
    def targetMessageType(self, targetMessageType):
        self.__targetMessageType = targetMessageType

    @property
    def targetFieldName(self):
        return self.__targetFieldName
    @targetFieldName.setter
    def targetFieldName(self, targetFieldName):
        self.__targetFieldName = targetFieldName