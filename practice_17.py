text_file = open('Word.txt', 'r')
read = text_file.read()
splitted = read.split()
matched = {}
wordscrabble = {"aeilonsrut": 1, "dg": 2, "cbmp": 3, 'fhwvy': 4, 'k': 5, 'jx': 8, 'qz': 10}
for i in splitted:
    letters = 'abc'
    value = 0
    flag=True
    for x in i:
        if x in letters:
            if (i.count(x) <= letters.count(x)):
                for ws in wordscrabble.keys():
                    flag=True
                    if x in ws:
                        value += wordscrabble[ws]
                    else:
                        pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        matched[i] = value
max_value=max(matched.values())
max_keys=max(matched.keys())
print(max_keys+": "+ str(max_value))
