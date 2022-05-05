# # Decision making is a process that runs a block of code if an expression is true
# # z = 1
# # if z != 1:
# #     print("z is greater than 1")
# # else:
# #     print("z is not greater than 1")
#
# # x = 10
# # if x == 1:
# #     print("hi")
# #     print("hello")
# # print("bye")
#
#
# # There are different ways of making decision
# # if  (Check only one condition)
# # if else (Check two condition)
# # if elif elif .. else (Check Multiple condition)
#
# x = 1
# if x == 1:
#     print("hi")
# else:
#     print("bye")
#
# x = 10
# if x == 1:
#     print("hi")
# elif x < 11:
#     print("True")
# else:
#     print("bye")
#
#
# l=2
# b=4
# if l==b:
#     print("square")
# else:
#     print("rectangle")
#
#
# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y:"))
# if x == y:
#     print("The given shape is square")
# else:
#     print("the given shape is rectangle")

# x = int(input("Enter input from range 1 to 10"))
# if x == 1:
#     print("A")
# elif x == 2:
#     print("B")
# elif x == 3:
#     print("C")
# elif x == 4:
#     print("D")
# elif x == 5:
#     print("E")
# else:
#     print(x)

# Grade = input("Enter Grade:  ")
# if Grade == "A":
#     print("Excellent")
# elif Grade == "B":
#     print("Good")
# elif Grade == "C":
#     print("C")
# elif Grade == "D":
#     print("Poor")
# else:
#     print("input error")
#

# x = 10
# y = 21
# if x > 1 and y > 10:
#     print("hello")
# # else:print("error!")

# x = 1
# y = 2
# if x >= 1 or y < 10:
#     print(x+y)
# # else:print("401 forbidden Error!")


Gender = "male"
Age = 58
# if Gender == "male" and Age > 60:
#     print("he is eligible for Corona Vaccine")
# else:
#     print("he is not eligible for vaccine")
if Gender == "male":
    if Age > 60:
        print("eligible")
    else:
        print("ineligible")
else:
    print("ineligible")
