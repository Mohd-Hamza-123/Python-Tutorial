
room_no = [1,2,3,4,5,6,7,8]
x = [False,True] 
multiple_data = ["T-shirt",4000,True , None,["Hello", "World"]]



size = ["Red","Blue","Green","Pink","Yellow"]

# accessing list element
print("size = ",size)
print(size[0])
print(size[-1])
most_used_color = size[::2]
# print(most_used_color)

# delete list element

del size[2]
print(size)
del size[2]
print(size)


my_list = [10, 20, 30, 40, 50]

del my_list[1:4]
print(my_list)


# update elements

names = ["Adil","Hamza","Shadab","Umar"]
names[2] = "Zahid"
names[0] = 200

print("names = ",names)

age = [10, 20, 30, 40, 50]
age[2:4] = [3,4]
print(age)


