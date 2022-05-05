class Human:
    def eat(self,name):
        print(self.name+" eats food")
class Male(Human):
    def __init__(self,name):
        self.name=name
    def shaveBeard(self):
        super().eat(self.name)
        print(self.name+" shaves beard every morning")
class Female(Human):
    def __init__(self,name):
        self.name=name
    def combHair(self):
        super().eat(self.name)
        print(self.name+" combs hair every morning")

m1=Male('Ram')
m1.shaveBeard()
f1=Female('Sita')
f1.combHair()

