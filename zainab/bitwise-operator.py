### Bitwise AND

result = 3 & 6 
print(result) 

# 110   --> 6
# 011   --> 3
# 010   --> 2

print(bin(2))

### Bitwise OR

result2 = 3 | 6 
print("result2",result2)
# 110   --> 6
# 011   --> 3
# 111   --> 7

# print(bin(7))

# Bitwise XOR (^)

result3 = 3 ^ 6 
print("result3  : ",result3)

# same bit --> 0 , else 1 
# 110   --> 6
# 011   --> 3
# 101   --> 5
# print(bin(5))\

# Bitwise NOT ~ 

result4 = ~8

# formula --> ~x = -(x + 1)

print(result4)