# file = open("Word.txt", "r")
# text = file.read()
# Upper = text.upper()
# replaced=Upper.strip('-')
# splitted = replaced.split()
# splitted_without_duplicate = list(dict.fromkeys(splitted))
# splitted_without_duplicate.sort(reverse=False)
# print(splitted_without_duplicate)
#
# sentence = "The college's best part is its sports activity"
# sentence = sentence.split()
# without = []
# for i in sentence:
#     if "'" in i:
#         z=i.replace("'s", "")
#         without.append(z)
#     else:
#         without.append(i)
# print(sentence)
# print(without)
#
file = open("Word.txt", "r")
text = file.read()
from string import digits
s= text
remove_digits = str.maketrans('', '', digits)
res = s.translate(remove_digits)
splitted=res.split()
splitted_without_duplicate = list(dict.fromkeys(splitted))
# print(splitted_without_duplicate)
newString=[]
for i in splitted_without_duplicate:
    if "'" in i:
        z=i.replace("'s", "")
        newString.append(z)
    elif "'" in i:
        z=i.replace("'re", "")
        newString.append(z)
    elif "." in i:
        z = i.replace(".", "")
        newString.append(z)
    elif "-" in i:
        for z in i.split("-"):
            newString.append(z)
    else:
        newString.append(i)
print(newString)
# from string import digits
# s = 'abc123def456ghi78912345zer134o0'
# remove_digits = str.maketrans('', '', digits)
# res = s.translate(remove_digits)
# print(res)