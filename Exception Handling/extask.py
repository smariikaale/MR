#Implement all the programs till date with exception handling

#1.calculator:

# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Error! Division by zero is not allowed.")
# def calculator():
#     while True:
#         choice=input("Choose + for addition, - for substraction, * for multiplication ,/ for division and _ for exit:")
#         if choice == "_":
#             print("Exiting....!!")
#             break
#         try:
#             num1=int(input("Enter your first number:"))
#             num2=int(input("Enter your second number:"))
#         except ValueError:
#             print("Invalid input!")
#         if choice == "+":
#             print(f"Result is:{add(num1,num2)}")
#         elif choice == "-":
#             print(f"Result is:{subtract(num1,num2)}")
#         elif choice == "*":
#             print(f"Result is:{multiply(num1,num2)}")
#         elif choice == "/":
#             print(f"Result is:{divide(num1,num2)}")
#         else:
#             print("Invalid Choice!!")
# calculator()

#2.multiplication table:
# try:
#     number=int(input("Enter a number:"))
#     print(f"The multiplication table of {number} is:")
#     for m in range(1,11):
#         print(f"{number}*{m}={number*m}")
# except ValueError:
#     print("Invalid Input!!")

#3.given number is even or odd.
# try:
#     number=int(input("Enter a number:"))
#     if number%2==0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
# except ValueError:
#     print("Invalid Input!!")

#4.given number is palindrome or not.//(reads the same forward or backward)
# def is_palindrome(num):
#     str_num=str(num)
#     return str_num == str_num[::-1]
# try:
#     number=int(input("Enter a number: "))
#     if is_palindrome(number):
#       print(f"{number} is a palindrome.")
#     else:
#       print(f"{number} is not a palindrome.")
# except ValueError:
#    print("Invalid Input!!")

#5.login system using registration:
users={
    "Sma":"4567",
    "Smarika":"asdf"}
def register():
 try:
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists!!")
        return
    password = input("Enter a password: ")
    users[username] = password
    print(f"User {username} registered sucessfully!")
 except Exception as e:
    print("Error during registration:", e)

def login():
 try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login Sucessful!!")
    else:
        print("Invalid username or password!")
 except Exception as e:
        print("Error during login:", e)

def main():
    while True:
     try:
        choice=input("Choose 1 for register, 2 for login and 3 for exit:")
        if choice == "1":
           register()
        elif choice == "2":
           login()
        elif choice == "3":
           print("Exiting....!")
           break
        else:
            print("Invalid choice!")
     except Exception as e:
            print("Something went wrong:", e)
main()