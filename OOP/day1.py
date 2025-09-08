#oop(object oriented programming)-based on class and objects
#class-a structure blueprint to create its object
#object-an instance created using the class
#car-toyota,honda

#class keyword is used to create a class
#object-a variable that calls a class
# class Student:
#     name="Sma" #attribures-variables defined inside class
#     age=23

#     def abc(self): #methods-functions defined inside class
#                             #contains parameter(self)
#         print("ABC")
#         print(self)
# S1=Student() #S1-obj
# # print(Student)
# print(S1)
# print(S1.abc())

#oop has 4 pillars:
#inheritance,polymorphism,abstraction&encapsulation

# name="Sma"
# print(type(name))
# n1=10
# print(type(n1))
# list1=[1,2,3,4]
# print(type(list1))

#inheritance-reuseability,one class inherits properties/behavior from another,
# eg.employee=>manager,developer

# class Student:
#     name="Sma" #attribures-variables defined inside class
#     age=23

#     def abc(self): #methods-functions defined inside class
#                             #contains parameter(self)
#         print("ABC")
#         print(self)
# class Monitor(Student):
#     pass
# S1=Monitor() #S1-obj
# print(S1.name)
# # print(S1.abc())
# S1.abc()

#types of inheritance:
#single-one child inherits from one parent
#multiple-one child inherits from mul parents
#example:
# class A:
#     def showa(self):
#         return "A"
# class B(A):
#     def showb(self):
#         return "B"
#     def showa(self):
#         return "A from class B"
# class C(B):
#     pass
# c1=C()
# print(c1.showa())
# print(c1.showb())
# b1=B()
# print(b1.showa())
# print(b1.showb())
# a1=A()
# print(a1.showa()) #can't access B as A is parent class

#multilevel-chain of inheritance(Grandpar->Parent->Child)
#example:
# class A:
#     pass
# class B:
#     pass
# class C:
#     def abc(self):
#         return "ABC from C"
# class D(A,B,C):
#     pass
# d1=D()
# print(d1.abc()) 
# print(D.mro()) #has 3 parent class so goes through MRO

#MRO Order-defines the order in which python looks for a method or attribute
        #in a hierarchy of classes when multiple inheritance is used
        #current class-check 1st parent class-next parent class(in order declared)-con. up until obj

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#         print("C")
# class D(B,C):
#     def show(self):
#         print("D")
# print(D.mro())

#calculating mro manually
#formula-class+merge(parent class1,parent class2,.....[list of parent classes])
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
    def show(self):
        print("D")
print(D.mro())
# D=D+merge(B,C,B C)//the 1st element is head and the rest are tails(B is head)
  #D+merge(B A,C A,B C)//since B is in head so taking B out=>D B+merge(A,C A,C)// A is in tail so taking C out first
  #D B C A+object//obj should be at last

# B=B+merge(A,A)//B+merge()=>B+A merge()
# C=C+merge(A,A)

    
#polymorphism-many forms,same method behaves differently depending on object,
# eg.diff ways to pay

#abstraction-shows only what's necessary,hides unnecessary details and only shows the relevant functionality,
#eg.car controls vs engine details

#encapsulation-data hiding,wraps data+methods into one unit and restricts direct acess
#eg.a bank account security