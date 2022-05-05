# The Code inside function will not get executed until the function is called.

# def a():  # Function made
#     print("alpha")
#

# a()  # Function Called


# def addition(x, y):  # passing parameters or arguments in function
#     print(x + y)
#
#
# addition(5, 6)


def subtraction(x, y):
    z = x + y
    return z


y = subtraction(4, 2)
print(y)

