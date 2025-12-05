# string to number 

phoneNo = input("enter a number : ")
# to check type of value - type(value)

correct_no = float(phoneNo)
print(type(correct_no), correct_no)

mobile_no = int(input("enter a number : "))
print(type(mobile_no),mobile_no)

# print(type(452345.34523))
# print(type([1,3,5]))

# __________number to string____________

print("------------------------------------")

a = str(32423)
print(a , type(a))

# ___________tuple to list______________

print("------------------------------------")
my_tuple = list((1, 2, 3))
print(type(my_tuple),my_tuple)

# _________any value to boolean 

a = bool("3453fasd")
print(a)
b = bool(-1)
print(b)


# Examples of Falsy values

# print(bool(None)) # Output: False
# print(bool(0)) # Output: False
# print(bool("")) # Output: False
# print(bool([])) # Output: False
# print(bool({})) # Output: False
# print(bool(set())) # Output: False
# print(bool(range(0))) # Output: False


# implicit 

a = 1 + 2.322 # 1 is convert into float
b = float(1) + 2.322
print(a)

