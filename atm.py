# Task: Prepare a ATM system. User is allowed to register and login.
    # if login, user is allowed to view balance, add balance, withdraw balance
    # Use Functions File Handling and Loop
    # Hint => Use two files, one for authentication another for ATM task

import json

def register(username,pin):
    try:
        file=open("atm_credentials.txt","r")
        content=file.read()
        file.close()
    except FileNotFoundError:
        content=""
    
    credentials=content.split("-")
    for i in credentials:
        if i !="":
            dict_credentials=json.loads(i)
            if username in dict_credentials:
                print("Username already exists!!")
                return
    
    try:
        file=open("atm_credentials.txt","a")
        dict_credentials={username:pin}
        json_credentials=json.dumps(dict_credentials)
        file.write(json_credentials + "-")
        file.close()

        file=open("balance.txt","a")
        dict_balance={username:0}
        json_balance=json.dumps(dict_balance)
        file.write(json_balance + "-")
        file.close()

        print("Registration Successful!!")
    except Exception as e:
        print("Error during registration", e)

def login(username,pin):
    try:
        file=open("atm_credentials.txt","r")
        content=file.read()
        file.close()
    except FileNotFoundError:
        print("No users registered yet")
        return False
    
    credentials=content.split("-")
    for i in credentials:
        if i !="":
            dict_credentials=json.loads(i)
            if username in dict_credentials and dict_credentials[username]==pin:
                print("Login Successful!!")
                return True
    print("Invalid username or pin.")
    return False

def view_balance(username):
    try:
        file=open("balance.txt","r")
        content=file.read()
        file.close()
    except FileNotFoundError:
        print("Balance file not found")
        return 
    
    balance_data=content.split("-")
    for i in balance_data:
        if i !="":
            dict_balance=json.loads(i)
            if username in dict_balance:
                print("Your current balance is:",dict_balance[username])
                return

def add_balance(username):
    try:
        file=open("balance.txt","r")
        content=file.read()
        file.close()
    except FileNotFoundError:
        print("Balance file not found")
        return
    
    balance_data=content.split("-")
    new_content=""
    for i in balance_data:
        if i !="":
            dict_balance=json.loads(i)
            if username in dict_balance:
                try:
                    amount=int(input("Enter the amount you want to add:"))
                    if amount<=0:
                        print("Please enter a positive number")
                        new_content += json.dumps(dict_balance)+"-"
                    dict_balance[username] += amount
                    print("Balance updated! New balance is:", dict_balance[username])
                except ValueError:
                    print("Invalid Input!!")
            new_content += json.dumps(dict_balance)+"-"

    file=open("balance.txt","w")
    file.write(new_content)
    file.close()

def withdraw_balance(username):
    try:
        file=open("balance.txt",'r')
        content=file.read()
        file.close()
    except FileNotFoundError:
        print("Balance file not found")
        return
    
    balance_data=content.split("-")
    new_content=""
    for i in balance_data:
        if i !="":
            dict_balance=json.loads(i)
            if username in dict_balance:
                try:
                    amount=int(input("Enter the amount you want to withdraw:"))
                    if amount<=0:
                        print("Please enter a positive number")
                    elif amount>dict_balance[username]:
                        print("Insufficient balance")
                    else:
                        dict_balance[username] -= amount
                        print("Withdrawal successful!! New balance is:",dict_balance[username])
                except ValueError:
                    print("Invalid input!!")
            new_content += json.dumps(dict_balance) + "-"
    
    file = open("balance.txt", "w")
    file.write(new_content)
    file.close()

while True:
    choice=input("Choose r for register,l for login,e to exit:").lower()
    if choice=="r":
        username=input("Enter your username:")
        pin=input("Enter your pin:")
        register(username,pin)
    
    elif choice=="l":
        username=input("Enter your username:")
        pin=input("Enter your pin:")
        is_login=login(username,pin)
        if is_login:
            while True:
                print("ATM MENU")
                choice=input("Enter 1 for view balance,2 for add balance,3 for withdraw balance and 4 for logout:")
                if choice=="1":
                    view_balance(username)
                elif choice=="2":
                    add_balance(username)
                elif choice=="3":
                    withdraw_balance(username)
                elif choice=="4":
                    print("Logged out!")
                    break
                else:
                    print("Invalid Choice!!")
    elif choice=="e":
        print("Exiting ATM.....")
        break
    else:
        print("Invalid Choice!!")
print("Thankyou for using our system!!")







        


    

