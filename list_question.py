a=[1,2,3,4,12,2,1,4]
for i in a:
    if i not in a:
        a.remove(i)
    else:
        pass
print(a)