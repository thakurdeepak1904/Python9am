file = open("Word.txt", "r")
text = file.read()
from string import digits

s = text
remove_digits = str.maketrans('', '', digits)
res = s.translate(remove_digits)
Upper = res.upper()
splitted = Upper.split()
splitted_without_duplicate = list(dict.fromkeys(splitted))
newString = []
for i in splitted_without_duplicate:
    if "'" in i:
        z = i.split("'", 1)
        newString.append(z[0])
    elif "." in i:
        z = i.replace(".", "")
        newString.append(z)
    elif "-" in i:
        for z in i.split("-"):
            newString.append(z)
    else:
        newString.append(i)
sorted_String = newString.sort()
print(newString)
