tuple=(1,2,3,4,5,6,"Sma","Ale",8)
print(tuple)
print(type(tuple))
#indexing in tuples:
print(tuple[6])
print(tuple[-3])
#slicing in tuples:
print(tuple[1:6])
print(tuple[:3])
print(tuple[::2])
print(tuple[::-1])

#tuple to list:
tuple1=(5,6,7,8,9)
list_t=list(tuple1)
print(list_t)
#list to tuple:
list1=[1,2,3,4,5]
tuple_l=tuple(list1)
print(tuple_l)

#set methods:
a={1,2,3,4,5,6,9}
b={4,5,6,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
a.add(0)
print(a)
b.copy()
print(b)
c={5,8,6,3,2}
c.remove(6)
print(c)
c.update({0},{1,3})
print(c)
c.discard(5)
print(c)
c.pop()
print(c)
d={1,2,4,6,7,8}
e={5,6,4,2}
print(d.symmetric_difference(e))
print(d.issubset(e))
print(e.issuperset(d))
print(d.isdisjoint(e))