
# _______ string to number ___________
a = "3"
b = 2
# print(type(b))
result = pow(b,3)
print(result)
# result_a = pow(a,3) # unsupported operand type(s)
# print(result_a)

import math 

a = int(float(input("enter a number : ")))
print(f"type of {a} = ",type(a))

age = abs(a)
print(age)


# _______ number to string ___________

a = 45.545
print(type(a))
b = str(a)
c = b.replace("5","9")
print(c)
print(b,type(b))