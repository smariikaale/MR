#authentication system using file handling and functions:
import json

def login(username,password):
    file=open('credentials.txt','r')
    content=file.read()
    file.close()

    list_credentials=content.split("-")
    for i in list_credentials:
        if i !="":
            dicti=json.loads(i) #converts a JSON string back into a Python dictionary.
        if username in dicti and password==dicti[username]:
            print("Login Sucessful")
            break
    else:
            print("Login failed")

def register(username,password):
    dictcredentials={username:password}
    jsoncredentials=json.dumps(dictcredentials) #Converts the dictionary into a JSON string.
    file=open('credentials.txt','a')
    file.write(jsoncredentials+'_')
    file.close()
    
choice=input("Enter l for login, r for register:").lower()

match choice:
    case 'l':
        username=input("Enter your username:")    
        password=input("Enter your password:")
        login(username,password)
    case 'r':
        username=input("Enter your username:")    
        password=input("Enter your password:")
        register(username,password)
    case '_':
        print("Invalid Input!")