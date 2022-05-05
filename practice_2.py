# Question 1
# i = 1
# while i <= 10:
#     if i == 10:
#         print(i)
#         print("=", i * (i + 1) / 2)
#     else:
#         print(i, end="+")
#     i += 1

# i = 0
# sum = 0
# while i <= 10:
#     sum = sum + i
#     i += 1
# print(sum)

# question2
# x = 1
# odd = 0
# even = 0
# while x <= 100:
#     if x % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     x += 1
# print("Number of even numbers :", even)
# print("Number of odd numbers :", odd)

# question3
# i = 1
# while i <= 10:
#     if i > 1 and i < 4:
#         i += 1
#     else:
#         print(i)
#     i += 1


# a = 1
# while a <= 10:
#     if a > 1 and a < 4:
#         pass
#     else:
#         print(a)
#     a += 1
#
# a = []  # empty list
# b = 1
# while b <= 5:
#     a.append(b)
#     b += 1
#     print(a)
#

a = []  # empty list
b = 1
while b <= 5:
    if b==3:
        a.insert(2,"hi")
        b+=1
    a.append(b)
    b += 1
    print(a)
