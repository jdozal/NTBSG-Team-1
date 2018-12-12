import FieldValuePairsContainer
    #, Protocol


class MessageType:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.fieldValuePairs = []
        self.fields = []
        self.dependency = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

    def update(self, name, color):
        if(name != 0 and color != 0):
            self.name = name
            self.color = color
        if(name != 0):
            self.name = name
        else:
            self.color = color

# *****TESTING*****
# test = MessageType("field", "blue")
# print(test.name)
# print(test.color)
#
# test.name = "bitch"
# print(test.name)
#
# test.update(name="jk field", color="")
# print(test.name)
# print(test.color)xv