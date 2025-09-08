
#a=10.5
#print(a)
#print(type(a))
#we use type to find the datatype

#operators-symbols that perform specific operations(+,-,/,*,>,%,and,or,not,....)
#and-if both conditions are true then it returns true else returns false
#or-T,T:T/ T,F:T/ F,F:F
#is-same like(== but it checks the value) whereas is checks the memory location
#in and not in-checks if the value is a part of the data type


#Task
# num1=int(input("Enter the first num: "))
# num2=int(input("Enter the second num:"))
#print(num1+num2)
#print(num1-num2)
#print(num1*num2)
#print(num1/num2)
#print(num1%num2)
#print(num1**num2)
#print(num1//num2)

#if 10>5 and 5<4:
    #print("true")
#else:
    #print("false")

#a="Sma"
#if "m" in a:
    #print("m is present")
#else:
    #print("m is not present")

# name=input("Enter your name:")
# if "m" in name:
#     print("m is present")
# else:
#     print("m is not present")

#list-datatype that stores multiple values of diff datatypes
# multiple lists can be stored inside a list(nested list)
# []-used to define a list
a=[1,2,3,4,5.6,"Sma","Ale",[2,3,4,5,6]]
print(type(a))
print(a)
#list methods:
a.append("Magar")
print(a)
print(a.count(2))
print(a.index(4))
# print(a.clear())
print(a.copy())
#list slicing:
print(a[0])
print(a[5])
#slicing-creates a new subset list from the original list
 # end value is always exclusive(not sliced)
# b =a[0:5]
# print(b)
# print(type(b))
# e=a[4:6]
# print(e)
#end slicing:
# c=a[:7]
# print(c)
# #start slicing:
# d=a[4:]
# print(d)

#positive index with step:
# f=a[::2]
# print(f)
#//skips 2 index
#negative index:
# print(a[-1])
# print(a[-2])
#slicing in negative indexing:
# print(a[-1:-4:-1])
# print(a[-4:-1:1])
# name="sma"
# print(name[0])
# print(name[-1])


#strip()-trims the string
# name = "  Sma  "
# print(name)
# print(name.strip())
# #split()-returns the list of strings 
# # we use separator in split that is unique than other characters to separate strings
# string="aaaaa,bbbb,xxx,cccc,dddd"
# print(string.split(","))

#tuple-immutable datatype that wraps the elements in ()//parenthesis
#used to create constants
# tuple=(1,2,3,4,5)
# print(type(tuple))
# print(tuple[2])
# #converting tuple into list
# list_tupe=list(tuple)
# list_tupe.append("5")
# print(type(list_tupe))
# print(list_tupe)
#list into tuple
# list1=[4,5,6,7,8]
# tup=tuple(list1)
# print(type(tup))

#boolean datatype-either true or false
# print(10>2)

#set datatype-also a mutable datatype enclosed in {}
#index in this datatype is not fixed
# a={1,2,3,"Sma",4,"Ale"}
# print(a)
#set methods:
# a={1,2,3,4,5,6}
# b={3,4,5,8}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))

#dictionary-mutable datatype,stores data values in key-value pairs, we use {} to define it
#used to check values if we already know the keys
#we use dict() to cast value in dictionary
dictionary={"Sma":"Smarika3456","Fav singer":"Taylor Swift","5":"3"}
print(dictionary)
print(type(dictionary))
print(dictionary.keys())
print(dictionary.values())

# name="Sma" #here name is key and caste is value
# caste="Ale"
# dict_credential={name:caste}
# print(dict_credential)
# print(type(dict_credential))
# print(dict_credential.get(name))
# print(dict_credential[name])
# print(dict_credential.keys())

