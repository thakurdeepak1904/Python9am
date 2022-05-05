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

    def story_analysis(self, story_list, letters):
        new_list = []
        for i in story_list:
            file = open(i[1], 'r')
            read = file.read()
            uppercase = read.upper()
            splitted = uppercase.split()
            score=0
            matched=[]
            for x in splitted:
                for y in x:
                    if y in letters.upper():
                        score+=1
                    else:pass
            matched.append(i[0])
            matched.append(score)
            matched = tuple(matched)
            new_list.append(matched)
        return new_list


r1 = MathDemo()
result = r1.story_analysis([('RABBIT', 'story.txt'), ('ABBIT', 'story.txt')], 'xz')
print(result)
