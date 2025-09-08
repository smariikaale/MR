#1.Make a calculator program using Python functions and loop
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     if b==0:
#         return "Error!!"
#     return a/b
# def calculator():
#     while True:
#         choice=input("Choose + for addition, - for substraction, * for multiplication ,/ for division and _ for exit:")
#         if choice == "_":
#             print("Exiting....!!")
#             break
#         num1=int(input("Enter your first number:"))
#         num2=int(input("Enter your second number:"))
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

#2.Print a multiplication table of the number that is input by the user.
# number=int(input("Enter a number: "))
# print(f"The multiplication table of {number} is:")
# for m in range(1,11):
#     print(f"{number}*{m}={number*m}")

#3.Check if the given number is even or odd.
# number=int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

#4.Check if a given number is palindrome or not.(reads the same forward or backward)
# def is_palindrome(num):
#     str_num=str(num)
#     if str_num == str_num[::-1]:
#        return True
#     else:
#        return False
# number=int(input("Enter a number: "))
# if is_palindrome(number):
#    print(f"{number} is a palindrome.")
# else:
#    print(f"{number} is not a palindrome.")

#5.Make a simple login system without registration using functions.
# def check_login(username,password):
#     c_username = "Sma"
#     c_password = "1234"
#     if username == c_username and password == c_password:
#         return True
#     else:
#         return False
# def login_system():
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if check_login(username, password):
#         print("Login successful!!")
#     else:
#         print("Invalid username or password.")
# login_system()

#6.Make a login system using registration using function.
users={
    "Sma":"4567",
    "Smarika":"asdf"}
def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists!!")
        return
    password = input("Enter a password: ")
    users[username] = password
    print(f"User {username} registered sucessfully!")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login Sucessful!!")
    else:
        print("Invalid username or password!")
def main():
    while True:
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
main()

#7.Print all the even numbers in a list of numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Even numbers are:")
# for num in numbers:
#     if num % 2 == 0:  
#         print(num)

#8.Write 10 hobbies in the file with a seperator.
hobbies = ["Reading", "Writing", "Painting", "Singing", "Sketching","Cooking", "Swimming", "Photography", "Traveling", "Dancing"]
file=open("hobbies.txt","w")
file.write(",".join(hobbies))
file.close()


            
        
        