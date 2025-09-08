#super method-calls the next class in the mro order
# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         super().show()
#         print("B")
# class C(A):
#     def show(self):
#         super().show()
#         print("C")
# class D(B,C):
#     def show(self):
#         super().show()
#         print("D")
# obj=D()
# print(D.mro())
# obj.show()

#constructor-a special method that will be called automatically
  #when an object is created whether we define it or not
  #there is only one constructor in python ie.__init__
#attributes types-class and method attributes
#class attribute-defined in class,doesn't change acc to obj
#method-defined in method,changes acc to obj//obj attributes
# #setinfo-needs to be called explicitly

# class Student:
#     college="KCC" #class attribute
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno #method attributes

# s1=Student("Sma",23,8)
# print(s1.name)
# s2=Student("Puja",25,2)
# print(s2.age)
# s3=Student("Sami",25,6)
# print(s3.age)

# class Student:
#     college="KCC"
#     def setinfo(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
# s1=Student()
# print(s1.college)
# s1.setinfo("Sma",23,8)
# print(s1.name)

#Encapsulation-data hiding
# class Student:
#     __college="KCC"
#     college1=__college
#     def abc(self):
#         self.__college="ABC"
#         return self.college
#     def __setinfo(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
# s1=Student()
# # print(s1.college)
# # s1.setinfo("Sma",23,8)
# # print(s1.name)

# #hidden data can be accessed by the non encapsulated method
# print(s1.college1)

#create a reset password method that changes the encapsulated attribute "password":
# class User:
#     def __init__(self,username,password):
#         self.username=username
#         self.__password=password
#     def reset_password(self,new_password):
#         self.__password=new_password
#         print("Password updated successfully!!")
#     def check_password(self,password):
#         return self.__password==password
# u1=User("Sma","smarika3456")
# print(u1.check_password("smarika3456"))
# u1.reset_password("sma5678")
# print(u1.check_password("sma5678"))
        
# class User:
#     def __init__(self,username,password):
#         self.username=username
#         self.__password=password
#     def reset_password(self,new_password):
#         self.__password=new_password
#         print("Password updated successfully!!")
#     def get_password(self):
#         return self.__password
# u1=User("Sma","smarika3456")
# print(u1.get_password())
# u1.reset_password("sma5678")
# print(u1.get_password())
        
#Decorators-special kind of functions that takes another function as arguement
#  and returns the modified version of the func without changing the original func
#we use @ for decorator

# def my_decorator(func):
#     def abc():
#         print("Hello world!!")
#         func()
#         print("Hello world!!")
#     return abc
# @my_decorator
# def hello():
#     print("Hello!!!!")
# hello()

#incase of not using self//staticmethod
# class Student:
#     @staticmethod
#     def print_name():
#         print("Smarika Ale")

# s1=Student()
# s1.print_name()

#polymorphism-one thing,many forms
class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("meow")
class Bird:
    def sound(self):
        print("chirp")
d1=Dog()
c1=Cat()
b1=Bird()
d1.sound()
c1.sound()
b1.sound()