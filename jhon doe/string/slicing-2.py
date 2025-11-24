str = "KDN4NANL3UJJJ"
# slicing syntax  str[start:end:step]
a = str[4:]
print(a)

b = str[:5]
print(b)

c = str[1:7]
print(c)

e = str[:]
print(e)

n = str[3:len(str)]
print(n)

phone_no = "0123456789"

x = phone_no[::2]
print(x)


account_No =  "HIO34G3YBN"
# print(len(account_No))
last_four_digit = account_No[6:]
print(last_four_digit)