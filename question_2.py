def word_from_letters(word, letters):
    Flag = False
    for i in word:
        if i in letters:
            if (word.count(i) <= letters.count(i)):
                Flag = True
            else:
                Flag = False
                break
        else:
            Flag = False
            break
    return Flag