#abstraction-hiding the complexity,only showing what's needed
# class Bike:
#     status=False
#     petrol=False
#     brake=False

#     def start(self):
#         self.status=True
#         self.petrol=True
#         self.brake=True
#         print("Bike gets started")

# b1=Bike()
# b1.start()

#abstractmethod
#ABC-Abstract Base Class
from abc import ABC, abstractmethod
class Teacher:
    @abstractmethod
    def teaches(self):
        print("Hello Teacher!!")
class EnglishTeacher(Teacher):
    def teaches(self):
        print("Hello English Teacher!!")
class MathTeacher(Teacher):
    def teaches1(self):
        print("Hello Math Teacher!!")
m1=MathTeacher()
m1.teaches1()