import json
file = open('credentials1.txt', 'a') #this file must exist
file.close()

def login(username, password):
    file = open('credentials1.txt', 'r')
    content = file.read()
    file.close()
    
    list_credentials = content.split("-")
    for i in list_credentials:
        if i != "":
            dicti = json.loads(i)
            if username in dicti and password == dicti[username]:
                print("Login Successful")
                break
    else:
        print("Login failed")

def register(username, password):
    file = open('credentials1.txt', 'r')
    content = file.read()
    file.close()
    
    list_credentials = content.split("-")
    #checking for duplicate username
    for i in list_credentials:
        if i != "":
            dicti = json.loads(i)
            if username in dicti:
                print("Username already exists! Please choose a different username.")
                return
            
    dictcredentials = {username: password}
    jsoncredentials = json.dumps(dictcredentials)
    file = open('credentials1.txt', 'a')
    file.write(jsoncredentials + '-')
    file.close()
    print("Registration Successful")
 
while True:
    choice = input("Enter l for login, r for register, or q to quit: ").lower()
    
    if choice == 'l':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username, password)
    
    elif choice == 'r':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register(username, password)
    
    elif choice == 'q':
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid Input!")
