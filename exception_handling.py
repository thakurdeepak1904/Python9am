try:
    file=open('stori.txt')
    text=file.read()
    print(text)
except:
    print('Something went wrong when opening a file')



try:
    file=open('stori.txt')
    text=file.read()
    print(text)
except IOError as error:
    print(error)


# try:
#     text=open('story.txt')
#     read=file.read()
# except IOError
# else:

try:
    file=open('stor.txt')
    read=file.read()
    print(read)
except IOError as error:
    print(error)
finally:
    print('This will run anyhow')














