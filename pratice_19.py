class Human:
    def __init__(self, a, b):
        self.__name = a
        self.__city = b

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setCity(self, city):
        self.__city = city

    def getCity(self):
        return self.__city


h1 = Human('Ram', 'Ktm')  # h1 object is instantiated and its private properties are initialized through the constructor
h1.setName('Hari')
print(h1.getName())
print(h1.getCity())
