from question_2 import word_from_letters
from question_3 import word_score


def find_words(word_list, letters):
    new_word_list = {}
    for i in word_list:
        flag = word_from_letters(i, letters)
        if flag == True:
            score = word_score(i)
            new_word_list[i] = score

    return new_word_list


result = find_words(['LAMB', 'REAL', 'WONDER'], 'BMOEALMR')
print(result)
