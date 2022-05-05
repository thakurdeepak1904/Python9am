def take_value(p, t, r):
    return take_value(p, t, r)


p = int(input("Enter Principle: "))
t = int(input('Enter Time: '))
r = int(input('Enter Interest Rate: '))


def calculate():
    SI = p * t * r / 100
    return SI


def display():
    return calculate()


result = display()
print(result)
