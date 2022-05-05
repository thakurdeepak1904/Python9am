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
        for a in story_list:
            return a
            # file = open(i[1], 'r')
            # read = file.read()
            # uppercase = read.upper()
            # splitted = uppercase.split()
            # score=0
            # check_letters=[]
            # for a in letters:
            #     check_letters.append(a)
            # for x in splitted:
            #     for y in x:
            #         if y in check_letters:
            #             score+=1
            #         else:pass
            # new_list = []
            # new_list.append(i[0])
            # new_list.append(score)
            # new_list = tuple(new_list)
            return


r1 = MathDemo()
result = r1.story_analysis([('RABBIT', 'story.txt'), ('ABBIT', 'story.txt')], 'XZ')
print(result)

