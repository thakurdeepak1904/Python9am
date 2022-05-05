class MathsDemo:
    def word_from_let(self, word, letters):
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

    def find_words(self, word_list, letters):
        new_word_list = {}
        for i in word_list:
            Flag = self.word_from_let(i, letters)
            if Flag == True:
                score = self.word_score(i)
                new_word_list[i] = score
        return new_word_list


result = MathsDemo()
res = result.word_from_let("EALMRBMO", "BMOEALMR")
print(res)
