def highest__score(word_list, letters):
    file=open('Word.txt','r')
    read=file.read()
    splitted=read.split()
    print(splitted)
    matched = {}
    wordscrabble = {"aeilonsrut": 1, "dg": 2, "cbmp": 3, 'fhwvy': 4, 'k': 5, 'jx': 8, 'qz': 10}
    for i in word_list:
        flag = True
        value = 0
        for x in i:
            if x in letters:
                if (i.count(x) <= letters.count(x)):
                    flag = True
                    for ws in wordscrabble.keys():
                        if x in ws:
                            value += wordscrabble[ws]
                        else:
                            pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag == True:
            matched[i]=value
    return matched


result = highest__score('asdf','asdf')
print(result)
