#loop-a technique to execute the same block of code repeatedly
#2 types of loop-For loop and While loop

#syntax for For loop:
#  for variable(iterator) in iterables:
#code to be executed
#we use For loop when we already know the start and end point
#iterator-a variable used in loop to access each element of iterable
#iterable-a group datatype where loop runs
#iteration-a single time that a loop runs
#example:
# list1=[1,2,3,4,5]
# for i in list1:
#     print(i)
# list2=[1,"Sma",2,[2,3],{"age":23}]
# for i in list2:
#     print(i)
#     print(list2)

#range(), syntax-range(start_value,end_value,step)
#it is exclusive so it doesn't take end value
# for i in range(5,10,2):
#     print(i)
#only prints keys in dict
# dict={
#     "name":"Sma",
#     "age":23,
#     "location":"anamnagar"
# }
# for i in dict:
#     print(i)


#syntax for While loop:
#while condition:
#code to be executed
#we use While loop when we don't know the start and end point
#has a defect, may fall into infinite loop trap 
# a=5// NOT TO DOOOO
# b=10
# while a<b:
#     print("b is greater than a")
#example:

while True:
    choice=int(input("Enter 1 for addition, 2 for substraction and 3 for exit:"))
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    match choice:
        case 1:
         print(num1+num2)
        case 2:
         print(num1-num2)
        case 3:
         print("Exciting...")
         break
        case _:
         print("Invalid input")
print("Thankyou!!!!")

#break-breaks and exits from the current loop
#continue-breaks the current iteration but continues the loop
# numbers=[5,6,7,8,9]
# for i in numbers:
#     if i == 8:
#         break
#     print(i)
# print("Outside the loop")


















