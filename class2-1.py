class Human:
    def __init__(self, x, y):
        self.name = x
        self.__city = y

    def walk(self):
        print(self.name, self.__city)


h1 = Human('Ram', 'ktm')
print(h1.name)
h1.walk()
# print(h1.__city)
