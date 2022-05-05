import string


def word_score(word):
    wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    wordscore = 0
    for i in word:
        for x in wordscrabble.keys():
            if i in x:
                wordscore += wordscrabble[x]

    return wordscore


def highest_score(file, letters):
    file1 = open(file, 'r')
    text = ""
    while True:
        line = file1.readline()
        if not line:
            break
        text += line
    text = text.replace("-", " ")
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.upper()
    splitted_text = text.split()
    highest_score = 0
    for word in splitted_text:
        new_score = 0
        Flag = True
        for characters in word:
            if characters in letters:
                if word.count(characters) <= letters.count(characters):
                    Flag = True
                    new_score = word_score(word)
                else:
                    Flag = False
                    break
            else:
                Flag = False
                break
        if Flag == True:
            if new_score > highest_score:
                words = []
                words.append(word)
                words.append(new_score)
                words = tuple(words)
                highest_score = new_score
            else:
                highest_score = highest_score

    return words


result = highest_score("story.txt", "CFGHIJKN")
print(result)
