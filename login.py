import security 
import findInFile
import signup
import game

def login():
    username = str(input("Enter name:")).lower()
    password = str(input("Enter password:"))
    line = findInFile.findInFile(username)

    if line:
        lineSplit = line.split(':')
        lineUser = lineSplit[0]
        linePassword = lineSplit[1]

        if security.checkEncryptedPassword(password,linePassword):
            print("Logged in!")
            game.main(lineUser)
        else:
            print("It Does not Match :(")
    else:
        print("User not found")
        registerNewUser = bool(input("Do you wanna join? y/n?")=='y')
        if registerNewUser:
            signup.signup(username,password)
            game.main(username)
        else:
            exit()
