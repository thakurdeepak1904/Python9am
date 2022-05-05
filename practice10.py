# def is_anagram(str1, str2):
#     list_str1 = list(str1)
#     list_str1.sort()
#     list_str2 = list(str2)
#     list_str2.sort()
#
#     return (list_str1 == list_str2)
#
# # print(is_anagram('anagram','nagaram'))
# print(is_anagram('mat','tam'))


# def ReArrangeStrings(string1, string2):
#     list1 = list(string1.split())
#     list2 = list(string2.split())
#     list1.sort()
#     list2.sort()
#     if (list1 == list2):
#         return True
#     else:
#         return False
# S1 = "please select a category"
# S2 = "category please a select"
# if (ReArrangeStrings(S1, S2)):
#     print("Yes")
# else:
#     print("No")
#

def ReArrangeStrings(string1, string2):
    list1 = list(string1.)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    for i in list1:
        if list1 not in list2:
            return False
        else:
            return True
if (ReArrangeStrings("lapha", "alpha")):
    print("Yes")
else:
    print("No")
