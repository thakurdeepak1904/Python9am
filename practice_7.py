# fruits = ["apple", "mango"]
# word = "abc-xy"
# test=word.split("-")
# fruits.append(test[0])
# print(test)
# print(test[0])

# fruits = ["apple", "mango"]
# word = "abc-xy"
# fruits.append(word.split("-")[:])
# print(fruits)

# permutations in string
# from itertools import permutations
#
#
# def allPermutations(word,letters):
#     permList = permutations(word)
#     permList1=permutations(letters)
#     word_list=[]
#     for perm in list(permList):
#         # print(''.join(perm))
#         words=word_list.append(perm)
#         print(words)
# allPermutations('DEF','FED')

# from itertools import permutations
# def word_in_letters(word,letters):
#
#     words = [''.join(p) for p in permutations(word)]
#     if letters in words:
#         print("TRUE")
#     else:
#         print("FALSE")
#
# word_in_letters('DEEPAK','KAPEED')


from itertools import permutations


def word_in_letters(word, letters):
    for p in permutations(word):
        if str(''.join(p)) == str(letters):
            boolean = True
            break
        else:
            boolean: False
    return boolean


result = word_in_letters('DEEPAK', 'KAPEED')
print(result)
