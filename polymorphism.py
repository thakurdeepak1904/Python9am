# Polymorphism is a method process objects differently depending on the class type or data type.

# Polymorphism in case if inbuilt function
people = ['ram', 'shyam', 'hari']
fruits = 'apple'
# here len() method treats an object as per its class type
print(len(people))
print(len(fruits))


# Polymorphism for user defined function
def maths(no1, no2=0):
    return no1 + no2


print(maths(4))
print(maths(6, 7))


# polymorphis, woth class methids
class Truck:
    def applybrakes(self):
        print('Truck has normal brake system')


class Car:
    def applybrakes(self):
        print('Car has abs system')


truck_obj = Truck()
car_obj = Car()

for vehicle in (truck_obj, car_obj):
    vehicle.applybrakes()


# Polymorphism with inheritances
# child class methid have the same name as parent class method

class Human:
    def walk(self):
        print('Human can walk')


class Male(Human):
    def walk(self):
        print('Male can walk')

    def talk(self):
        print('Female can walk')


class Female(Human):
    pass


m1 = Male()
m1.walk()
f1 = Female()
f1.walk()
