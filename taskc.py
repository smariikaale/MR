# #list:
# usernames=["Sma","Puja","Samikshya","Ishant"]
# user_input=input("Enter your username:")
# if user_input in usernames:
#     print("Username is present")
# else:
#     print("Username is not present")

# #dictionary of usernames and passwords
# names={
#     "Sma":"Sma5678",
#     "Puja":"p0987",
#     "Samikshya":"s234",
#     "Ishant":"ish5678"
# }
# username=input("Enter your username:")
# password=input("Enter your password:")
# if username in names and names.get(username)==password:
#     print("Login Sucessful!")
# else:
#     print("Login Failed!")

# #simple calculator system using condition cases:
# choice=input("Addition(+), Substraction(-),Multiplication(*),Division(/)")
# num1=float(input("Enter the first number:"))
# num2=float(input("Enter the second number:"))
# if choice=="+":
#     print("Result is: ", num1+num2)
# elif choice=="-":
#         print("Result is:",num1-num2)
# elif choice=="*":
#       print("Result is:",num1*num2)
# elif choice=="/":
#       print("Result is:",num1/num2)
# else:
#       print("Invalid choice!!")


#complete register and login system using dictationary
#register:
users={
    "Sma":"Sma5678",
    "Puja":"p0987",
    "Samikshya":"s234",
    "Ishant":"ish5678"
}
username=input("Enter your username:")
if username in users:
    print("Username already exists")
else:
    password=input("Enter a password:")
    users.update({username:password})
    print("Registration is sucessful!!")
#login:
login_username=input("Enter your username:")
login_password=input("Enter your password:")
if login_username in users and users.get(login_username)==login_password:
    print("Login Sucessful!")
else:
    print("Login Failed!")
