a = 6
b = 5.4
c = 7
x = (a + b + c) / 3
print("averag height = ",x)

import math
r = 7
area = math.pi * pow(r,2)
print("area of circle = ",area)

x = 576
z = math.sqrt(x)
print(f"square root of {x} =",z)

r = 5 
c = math.pi * 2 * r
print("circumference of a circle =", c)


a = 87
b = pow(a,3)
print(f"power of {a} =" ,b)


a = 3
result = math.exp(a) # e ^ a , e = 2.718 
print(result)

b = -443.34
result = math.fabs(b)
print(result)


s = math.sin(1)  # return value of sin(1) into radian
print("s (degree) = ",math.degrees(s))

c = math.cos(1)
print(c)

t = math.tan(1)
print(t)

# radian to degree
radian = 34
degree_value = math.degrees(radian)
print("degree value = ",degree_value)

# degree to radian 
degree = 90 
radian_value = math.radians(degree)
print("radian value =",radian_value)


base = 10 
result = 1000
exponent = math.log(result,base)
print(exponent)

exponent2 = math.log10(10000)

print(exponent2)