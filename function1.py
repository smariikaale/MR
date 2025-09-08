# def my_function(*args):
#     print(args)
# my_function("Sma",23,"Ale","Anamnagar",{"name":"Smarika"})

# def my_function(**kwargs):
#     print(kwargs)
# my_function(name="Sma",age=23,caste="Ale",location="Anamnagar")

# def my_function_combined(*args,**kwargs):
#     print(f"Args={args}")
#     print(f"Kwargs={kwargs}")
# my_function_combined("Sma",23,"Ale",caste="Ale",location="Anamnagar")

#types of functions:
#1.built-in functions-has been already created by python:print(),type()
#2.user defined functions-created by programmers

#list comprehension-programical way of adding values to the list
# list1=[1,2,3,5,6]
# list2=[x for x in range(1,10)]#list comprehension
# print(list1)
# print(list2)

#other types of functions:
#lambda function:single-line function
  #lambda keyword is used 
#normal function:
# def add(a,b) :
#    return a+b
# print(add(2,3))

#lambda function for previous function:
# add=lambda a,b:a+b
# print(add(2,3))

#map functions-applies a function to each element of an iterable 
# numbers=[1,2,3,4,5]
# squares=list(map(lambda x:x**2,numbers))
# print(squares)

#filter-filters the elements acc to our condition
# numbers=[1,2,3,4,5]
# even_numbers=list(filter(lambda x: x % 2 == 0,numbers))
# print(even_numbers)

#reduce function-combines all elements of a list into a single value
#needs functools
# from functools import reduce
# numbers=[1,2,3,4,5,6]
# sum=reduce(lambda x,y:x+y,numbers)
# print(sum)

#zip function-combines multiple lists element-wise
names=["a","b","c"]
numbers=[1,2,3,4]
combined=list(zip(names,numbers))
print(combined)