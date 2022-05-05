# def check(s1, s2):
#     if (sorted(s1) != sorted(s2)):
#         print("False")
#     else:
#         print("True")
# s1 = "adddd"
# s2 = "dddda"
# check(s1, s2)

# def check(s1, s2):
#     list_1 = list(s1)
#     list_2 = list(s2)
#     list_1.sort()
#     list_2.sort()
#     if list_1 == list_2:
#         boolean=True
#     else:
#         boolean=False
#     return boolean
#
# boolean=check("asdf", "asdf")
# print(boolean)

def check(s1, s2):
    list_1 = list(s1)
    list_2 = list(s2)
    list_1.sort()
    list_2.sort()
    return (list_1 == list_2)
print(check("asaf", "asaf"))


