# def highest_score(text_file, letters):
#     file = open(text_file, 'r')
#     read = file.read()
#     splitted = read.split()
#     matched = {}
#     wordscrabble = {"aeilonsrut": 1, "dg": 2, "cbmp": 3, 'fhwvy': 4, 'k': 5, 'jx': 8, 'qz': 10}
#     for i in splitted:
#         value = 0
#         flag = True
#         for x in i:
#             if x in letters:
#                 if (i.count(x) <= letters.count(x)):
#                     for ws in wordscrabble.keys():
#                         flag = True
#                         if x in ws:
#                             value += wordscrabble[ws]
#                         else:
#                             pass
#                 else:
#                     flag = False
#                     break
#             else:
#                 flag = False
#                 break
#         if flag == True:
#             matched[i] = value
#     return matched
#     # print(matched)
#
# highest_score('Word.txt','abc')


def find_score(word_list, letters):
    file = open(word_list, 'r')
    read = file.read()
    splitted = read.split()
    matched = {}
    wordscrabble = {"aeilonsrut": 1, "dg": 2, "cbmp": 3, 'fhwvy': 4, 'k': 5, 'jx': 8, 'qz': 10}
    for i in splitted:
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


result =find_score('Word.txt', "apple")
print(result)
