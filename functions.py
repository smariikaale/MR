#we create a function and add the code that should be executed again and again 
# and can call the function whenever we need it
#we use "def" keyword to define a function
#example of a simple function:
#syntax:
#def function_name():
    #block of code
#the function is not executed directly, we should call a function

# def my_function():
#     print("Smarika Ale")
#     print("Smarika Ale")
#     print("Smarika Ale")
# #to call a function- function_name()
# my_function()
# print()
# print()
# my_function()
#we use function to make our code reuseable
# def add():
#  num1=int(input("Enter num1 to add:"))
#  num2=int(input("Enter num2 to add:"))
#  print(num1+num2)
# def subtract():
#  num1=int(input("Enter num1 to sub:"))
#  num2=int(input("Enter num2 to sub:"))
#  print(num1-num2)
# def multiplication():
#  num1=int(input("Enter num1 to mul:"))
#  num2=int(input("Enter num2 to mul:"))
#  print(num1*num2)
# def division():
#  num1=int(input("Enter num1 to div:"))
#  num2=int(input("Enter num2 to div:"))
#  print(num1/num2)
# choice=int(input("Enter 1 for addition, 2 for substraction, 4 for multiplication, 5 for division and 3 for exit:"))

# match choice:
#     case 1:
#         add()
#     case 2:
#         subtract()
#     case 3:
#       print("Exiting...")
    
#     case 4:
#       multiplication()
#     case 5:
#       division()
#     case _:
#         print("Invalid input!")

#arguments and parameters:
#arguments are the values we pass to the function when calling the function
#parameters are the variables that are used during the function definition to receive the arguments

# def add(a,b):
#  print(a+b)
# def substract(a,b):
#  print(a-b)

# choice=int(input("1 for addition, 2 for substraction and 3 for exit:"))
# num1=int(input("Enter num1 :"))
# num2=int(input("Enter num2 :"))
# match choice:
#     case 1:
#      add(num1,num2)
#      #positional argument-the parameters take the arguments according to the position(args)
    
#     case 2:
#       substract(a=num1,b=num2)
#       #keyword argument- :key:value pir(kwargs)// position doesn't matter
#     case 3:
#        print("Exiting...")
#     case _:
#         print("Invalid input!")

#local and global variables:
#global variables-defined globally
#local variables-declared inside a function ,block or method 
# def add(a,b):
#  name="sma"
#  print(a+b)
#  print(num1)
#  print(num2)
#  print(name)#local variable

# def substract(c,d):
#  print(c-d)


# choice=int(input("1 for addition, 2 for substraction and 3 for exit:"))
# num1=int(input("Enter num1 :"))
# num2=int(input("Enter num2 :"))
# match choice:
#     case 1:
#      add(num1,num2)
     
    
#     case 2:
#       substract(a=num1,b=num2)
      
#     case 3:
#        print("Exiting...")
#     case _:
#         print("Invalid input!")
# print(num1)#global variable

