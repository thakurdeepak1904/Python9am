# x = [4, 3, 7, 3, 5]
# a = []
# for i in x:
#     if i not in a:
#         a.append(i)
#     else:
#         pass
# print(a)

# a = [10, 3, 4, 1, 30, 20]
# b = len(a)
# c = 0
# d = []
# while c < b:
#     if c == 0:
#         d = a[c]
#     else:
#         if a[c] > d:
#             d = a[c]
#         else:
#             pass
#     c += 1
# print(d)



# my_list = [2,1,3,252,1,1,35,6,3,2]
# my_final_list = dict.fromkeys(my_list)
# print(list(my_final_list))
import msilib.schema

my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []
while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)
print(new_list)
print(min)

# a = [10, 3, 4, 1, 30, 20]
# b = len(a)
# c = 0
# d = a[c]
# while c < b:
#     if a[c] > d:
#         d = a[c]
#     else:
#         pass
#     c += 1
# print(d)

my_list = [-15, -26, 15, 1, 23, -64, 23, 76,-15]
a=[]
for i in my_list:
    if i in a:
        pass
    else:
        a.append(i)
print(a)
