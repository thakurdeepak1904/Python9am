#constructior
# It is a function that is automatically executed during object execition/instantation.
##__init__ is a constructor function in python

# object variable are three tyoes:
# Public
# Private
# Protected
class Human:
    def __init__(self,x,y=0):
        self.name=x
        self.city=y
    def function(self):
        print(self.name, self.city)
h1=Human('Ram','ktm')
h2=Human('Hari','pkh')
h1.function()

class person(Human):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.graduationYear=2025

h3=person("Deepak",'KTM')
print(h3.graduationYear)


