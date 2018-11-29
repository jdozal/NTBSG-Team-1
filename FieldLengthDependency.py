
class FieldLengthDependency(Dependency):
    def __init__(self, sourceFieldName, targetFieldName):
        self.sourceFieldName = sourceFieldName
        self.targetFieldName = targetFieldName

    @property
    def sourceFieldName(self):
        return self.__sourceFieldName
    @sourceFieldName.setter
    def sourceFieldName(self, sourceFieldName):
        self.__sourceFieldName = sourceFieldName

    @property
    def targetFieldName(self):
        return self.__targetFieldName
    @targetFieldName.setter
    def targetFieldName(self, targetFieldName):
        self.__targetFieldName = targetFieldName