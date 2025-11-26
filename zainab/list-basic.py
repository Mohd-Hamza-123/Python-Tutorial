color_options = ["Red","Blue","Yellow"]
multi = ["Hamza",4332323,True,None,121.121]

print(color_options)
print(multi)

# access list elements 

print(color_options[1])
print("last element : ",color_options[-1])
b = color_options[0]
print(b)

# update list elements 

phone_no = [9234234,42342342,3432423,54234,5234,"77777"]
print("old phone no : ",phone_no)

phone_no[0] = 9999999 
phone_no[1] = "0000000"
phone_no[-1] = 888888
print("new phone no : ",phone_no)
# phone_no = [True]
# print(phone_no)


# delete elements 
size_options = ["SM","MD","XL", "XXL"]

print("size options : ",size_options)
del size_options[-1]
print("size options : ",size_options)
del size_options[2]
print("size options : ",size_options)

