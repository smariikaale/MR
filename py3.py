#Conditional Statements-executed only if the condition is satisfied
#If Else, If elif...else,loops,match
#if Else:
# a=10
# b=20
# if a>b:
#     print("True")
# else:
#     print("False")

# age=int(input("Enter your age:"))
# if age>18:
#     print("You are eligible")
# else:
#     print("You are not eligible")

#Elif ladder-we use elif keyword,checks multiple conditiond
# percentage=int(input("Enter your percentage:"))
# if percentage>90:
#     print("A+")
# elif percentage>=80 and percentage<=90:
#     print("A")
# elif percentage>=70 and percentage<80:
#     print("B+")
# else:
#     print("Failed!")

#match-checks if the user input matches with the case
# choice=input("Enter + for addition, - for substraction, * for multiplication, / for division")
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# match choice:
#     case '+':
#         print("Addition:", num1+num2)
#     case '-':
#         print("Substraction:", num1-num2)
#     case '*':
#         print("Multiplication:", num1*num2)
#     case '/':
#         print("Division:", num1/num2)
#     case _:
#         print("Invalid Input!")

#f string helps to print the variable inside the string,stands for format
# names=["Sma","SSD","aaa","ghy"]
# name=input("Enter your name:")
# if name in names:
#     print(f"{name} is present in the list")
# else:
#     print(f"{name} is not present")
#     names.append(name)
#     print(names)

# vegetables=["Apple","Banana","Litchi"]
# veg=input("Enter vegetable:")
# if veg not in vegetables:
#     print(f"{veg} is not present in the list")
# else:
#     print(f"{veg} is present")

#dictionary
# credentials={
#     "Sma":"sma3456",
#     "Ale":"a234",
#     "P":"234"
# }
# username=input("Enter your username:")
# password=input("Enter your password:")
# if username in credentials and credentials.get(username)==password:
# #credentials[username]== password:
#     print("Login sucessful!")
# else:
#     print("Login Failed")

