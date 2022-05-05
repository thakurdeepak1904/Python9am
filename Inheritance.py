
# Inheritance is the property of OOP in which a child class object can access methods/properties of paernt class.
# Method override is a case when parent class method is rewritten in child
class Human():
    def __init__(self):
        print('constructor')
    def walk(self):
        print('hello')

class child(Human):
    def __init__(self):
        print('constructor123')
        # super(child, self).__init__()
        super().__init__()
    def shave(self):
        print('hi')
    def walk(self):
        print('hello123')
        super().walk()
child_1=child()
child_1.walk()
child_1.shave()
