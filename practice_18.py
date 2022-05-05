class Human:
    def __init__(self, a, b, c, d):
        self.__name = a
        self.__city = b
        self.__age = c
        self.__Email = d

    def name(self):
        print(self.__name)

    def city(self):
        print(self.__city)

    def age(self):
        print(self.__age)

    def email(self):
        print(self.__Email)


h1 = Human('Ram', 'ktm', 22, "abc@gmail.com")
h1.name()
h1.city()
h1.age()
h1.email()
