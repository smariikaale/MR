#calculator system using loop:
while True:
     choice=input("Choose + for addition, - for substraction, * for multiplication , / for division and _ for exit:")
     if choice == "_":
          print("Exiting Calculator....!")
          break
     num1=int(input("Enter your first number:"))
     num2=int(input("Enter your second number:"))
     if choice == "+":
          print("Result is:",num1+num2)
     elif choice == "-":
          print("Result is:",num1-num2)
     elif choice == "*":
          print("Result is:",num1*num2)
     elif choice == "/":
          if num2!=0:
           print("Result is:",num1/num2)
          else:
           print("Error!!")
     else:
         print("Invalid choice!!")



          

