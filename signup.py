import security 

def signup(username,password):
    try:
        with open("PERFIS.txt", "a+") as f:
            hashed_password = security.encryptPassword(password)
            f.write(username+':'+hashed_password+"\n")
            print("User created!")
    except FileNotFoundError:
            print("The file doesn't exist")
