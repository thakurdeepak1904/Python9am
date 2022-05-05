def word(word):
    score = 0
    for letters in word:
        if letters in 'aeiou':
            score+=1
        elif letters in 'bcfgh':
            score+=2
        elif letters in "jmnpq":
            score+=4
        elif letters in 'tvw':
            score+=5
        elif letters in 'xyz':
            score+=8
        else:
            score+=10
    return score
score=word("apple")
print(score)


def scrabble_word_count(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    # score={'eaionrtlsu':1,"dg":2,"bcmp":3,"fhvwy":4,'k':5,'qz':10,'jx':8}
    res = 0
    for letter in word:
        res += score[letter]
    return res
res=scrabble_word_count("adventures")
print(res)