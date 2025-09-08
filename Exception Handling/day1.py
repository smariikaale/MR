#exception handling-way of handling errors

# a=10
# b=0
# print(a/b)

#try-we write code thay may contain error in try block
#except-we write code that will be executed when an error occurs in try block
#finally-executes whether error occurs or not
# a=10
# b=0
# try:
#    print(a/b)
# except:
#    print("The value of b cannot be 0.")
# finally:
#    print("This code runs anyway.")

#specific error handling:
list=[1,2,3,4,5]
a=10
b=2
try:
  print(a/b)
  print(list[4])
  print(int("Sma"))
except ZeroDivisionError:
  print("The number cannot be divided by zero.")
# except ZeroDivisionError as e:
#   print(e) #creating an object
except IndexError:  
  print("5th index is not found.")
except:
  print("Error!!")#should be at last

