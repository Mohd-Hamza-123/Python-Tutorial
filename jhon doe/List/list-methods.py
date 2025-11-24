# append()

colors = ['red','blue','green']
colors.append(True)
print("colors : ",colors)


# extend()

block1 = ["A","B","C"]
block2 = ["E","J","B"]

# block2.extend(block1)
block1.extend(block2)
# block1 = block1 + block2 + colors
print("block1 = ",block1)
print("block2 = ",block2)

# insert()

a = input("Enter a text need to insert : ")

seat = ["A1","A3","B1","B3"]

seat.insert(1,a)

print("seat : ",seat)

# remove()

colors = ["red","blue","green","pink","red"]
colors.remove("red")
print("colors : ",colors)


# pop()

names = ["adil","zeeshan","Hamza"]
a = names.pop()
print("removed element = ",a)
print("names : ",names)

# clear()

data_types = [1,True , "Hello", None]

data_types.clear()
print("data types : ",data_types)

# index(value) / index(value,starting_index)

colors = ["red","blue","green","blue", "pink","red"]
position = colors.index("blue")
position2 = colors.index("blue",2) 
print("position of blue  = ",position)
print("positin of blue after index 2 = ",position2)



# count()

c = ["A","B","C","A","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C",
]
no_of_A = c.count("A")
no_of_B = c.count("B")
no_of_C = c.count("C")

# print(c)
print("no of A,B,C ", no_of_A,no_of_B,no_of_C)

# sort()

roll_no = [3,6,6,8,2,9,0,5,1,4,6]
roll_no.sort()
print("roll no (ascending) : ",roll_no)

age = [34,64,34,90,34,5,2,5]
age.sort(reverse=True)
print("age (descending) = ",age)


# reverse()


colors = ["red","blue","green","blue", "pink"]
colors.reverse()

print("reverse colors : ",colors)