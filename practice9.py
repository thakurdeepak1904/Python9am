def word_from_let(word, letters):
    count=0
    for i in word:
        if i in letters:
            if (word.count(i)==letters.count(i)):
             aaa=True
        else:
            aaa=False
    if count==len(word):
        aaa=True
    else:
        aaa=False
    return aaa
result=word_from_let("bbb","abc")
print(result)