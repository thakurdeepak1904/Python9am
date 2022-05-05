# Create a function to find a largest number from a list

def function(*list):
    x = list[0]
    for a in list:
        if a > x:
            x = a
        else:
            pass
    return x


x = function(1, 2, 4, 5, 1, 2, 1, 10)
print(x)


def list(*num):
    Sum = 0
    for i in num:
        Sum += i
    return Sum


Sum = list(1, 20, 19, 45, 2, 3, 4)
print(Sum)
