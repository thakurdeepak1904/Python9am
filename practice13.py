def find_word(word_list, letters):
    matched = []
    score_value={"aeilonsrut":1,"dg":2,"cbmp":3,'fhwvy':4,'k':5,'jx':8,'qz':10}

    score={}
    for i in word_list:
        flag = True
        for x in i:
            if x in letters:
                if (i.count(x) <= letters.count(x)):
                    flag = True
                    pass
                else:
                    flag=False
                    break
            else:
                flag = False
                break
        if flag == True:
            matched.append(i)
        # for a in matched:
        #     for b in a:
        #         if b in score_value.values():
        #             score[a]:score_value.values()
    return score


result = find_word(["aaaa", "eappl", "lape"], "apple")
print(result)

#
# def find_word(word_list, letters):
#     matched=[]
#     for i in word_list:
#         for x in i:
#             if x in letters:
#                pass
#             else:
#                 break
#         matched.append(i)
#     return matched
# result=find_word(["aaaa","eappl","lape"],"apple")
# print(result)
