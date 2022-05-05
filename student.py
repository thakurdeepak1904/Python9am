students = int(input('Enter the number of students:'))
count = 1

while count <= students:
    grade = ''
    print(f'---student No: {count}---')
    eng = int(input('Enter English Marks:'))
    nep = int(input('Enter Nepali Marks:'))
    sci = int(input('Enter Science Marks:'))
    mat = int(input('Enter Math Marks:'))
    soc = int(input('Enter social Marks:'))
    marks = eng + nep + sci + soc + mat
    percentage=marks/5
    if percentage > 80 and percentage<=100:
        division = 'Dictintion'
    elif percentage >60 and percentage<=80:
        division = 'Second'
    elif percentage>40 and percentage<=60:
        division = 'Third'
    else:
        division = "Failed"
    count += 1
grade += (f'---student No: {count}--- Marks: {marks} division: {division}')
print(grade)
    # grade.append(division)
    # grade = tuple(grade)
    # finalGrade.append(grade)

