# def print_x(number):
#     i = 1
#     while i <= number:
#         print(i)
#         i += 1
#
#
# print_x(100)

# def function(x):
#     i = 0
#     j = 0
#     while i <= x:
#         j = i + j
#         i += 1
#     return j
#
#
# z = function(10)
# print(z)

# def function(z):
#     i = 1
#     odd = 0
#     even = 0
#     while i <= z:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#         i += 1
#     print("odd number:", odd)
#     print("even number:", even)
#
#
# function(100)
#
# def range(n):
#     i=1
#     while i<=n:
#         if i>1 and i<=3:
#             pass
#         else:
#             print(i)
#         i+=1
#
# range(10)

# def sum():
#     x = []
#     y = 1
#     while y <= 10:
#         x.append(y)
#         y += 1
#     print(x)
#
#
# sum()

def sum():
    x = []
    y = 1
    while y <= 1:
        if y == 3:
            x.insert(3, "hi")
            y += 1
        else:
            x.append(y)
            y += 1
        print(x)


sum()
