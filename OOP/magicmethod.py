#magic methods:starts and ends with double underscore
#   python calls them automatically
#   __init__=>called automatically when an obj is created,
#   __str__=>defines how obj appears when printed
# __len__,__add__,__sub__,__mul__,etc

class Student:
    name="Smarika Ale"

    def __str__(self):
        return "The str method is called"
    def __len__(self,value):
        count=0
        for i in value:
            count +=1
        return count
    def __call__(self, *args, **kwds):
        return "The obj is called"
s1=Student()
print(s1())
# print(len(s1.name))
