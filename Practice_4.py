# x = [10, 5, 8, 7, 1, 2]
# y = []
# z = len(x)
# while z >= 1:
#     z -= 1
#     y.append(x[z])
# print(y)


# x = [1, 7, 3, 4, 5]
# odd=1
# for a in x:
#     if a%2!=0:
#         print(odd)
#     else:
#         pass
#     odd+=1

# x = [1, 10, 6, 3, 5, 7, 12, 24, 56]
# odd = []
# y = len(x)
# while y>=1:
#     y-=1
#     odd.append(x[y])
# print(odd)


a = [1, 2, 3, 4, 5, 7]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
    else:
        pass
print(b)

list = [1, 2, 3, 4, 5, 6, 10]
new_list = []
count = 0
for a in list:
    if count % 2 != 0:
        new_list.append(a)
    count += 1
print(new_list)
