colors = ("Green","Blue","Pink","Yellow")
print(colors)

# access 
print(colors[0])

# delete 

# del colors[0] error 

# update 

# colors[0] = "Red"

# tuple with single element 

a = (1,)


color = ("Green","Blue","Pink","Yellow")

a = color[1:3]
print(a)

# methods 


numbers = (1, 2, 3, 2, 1, 2)

no_of_2 = numbers.count("2")
index_of_2 = numbers.index(2)
print(no_of_2)
print(index_of_2)



# packing and unpacking of tuples 

x , y , z = (1,2,"Hello")

print(x,y,z)

# adding tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2 + colors
print(tuple3)