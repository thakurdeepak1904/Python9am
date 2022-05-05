def word_score(word):
    wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    wordscore = 0
    for i in word:
        for x in wordscrabble.keys():
            if i in x:
                wordscore += wordscrabble[x]

    return wordscore