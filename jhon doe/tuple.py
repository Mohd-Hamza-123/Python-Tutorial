l = ["hello", 1 , 2 ,True]
a = l[0]
l.append(4)
print(a)
l[0] = "Hi"
del l[2]
print(l)

# access 

t = ("Hello","Hi",1,True)
print(t)
b = t[0]
print(b)

# del t[2] error 
# t[2] = 4     error 

# tuple slicing 

person = ("John", 30, "New York", "Engineer")

print(person[0::2])


# methods 

# count()

numbers = (1, 2, 3, 2, 1, "2")
a = numbers.count(1)
print(a)


# index()



person = ("John", 30, "New York", "Engineer")

i = person.index("Engineer")
print(i)


# packing and unpacking of tuples 

x , y = ("Hello",None)
print(x,y)

# adding tuple 

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2
print(tuple3)