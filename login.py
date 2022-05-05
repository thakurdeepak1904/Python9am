import os
import getpass

if not os.path.exists('Data.txt'):
    fs = open('Data.txt', 'w')
    fs.close()


def register():
    username = input("Enter Username: ")
    if username == open('Data.txt', 'r').read():
        print("Username already exists")
        exit()
    password = input(getpass.getpass("Enter Passwword: "))
    c_password = getpass.getpass("Enter Confirm Passwword: ")
    if password != c_password:
        print('Password not match')
        exit()
    file = open("Data.txt", "a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("User successfully created")
    exit()


def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    user_data = []
    for line in open("Data.txt", "r").readlines():
        user_data.append(line.split())
    total_user = len(user_data)
    increment = 0
    login_success = False
    while increment < total_user:
        if username == user_data[0] and password == user_data[1]:
            login_success = True
            increment += 1
    if login_success:
        print(f'Welcome {username}')
    else:
        print('Username and Password not match')


question = input('Do you have an account y/n: ')
if question == 'y':
    login()
else:
    register()
