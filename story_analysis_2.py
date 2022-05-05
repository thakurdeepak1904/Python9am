class MathDemo:
    def word_from_letters(self, word, letters):
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

    def word_score(self, word):
        wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
        wordscore = 0
        for i in word:
            for x in wordscrabble.keys():
                if i in x:
                    wordscore += wordscrabble[x]

        return wordscore

    def read_function(self, story):
        file = open(story, 'r')
        read = file.read()
        uppercase = read.upper()
        splitted = uppercase.split()
        return splitted

    def highest_score(self, story, letters):
        high_score = 0
        for i in self.read_function(story):
            flag = self.word_from_letters(i, letters)
            if flag == True:
                score = self.word_score(i)
                if score > high_score:
                    word = []
                    word.append(i)
                    word.append(score)
                    word = tuple(word)
                    high_score = score
                else:
                    high_score = high_score
        return word


r1 = MathDemo()
result = r1.highest_score('Story.txt', 'CFGHIJKN')
print(result)
