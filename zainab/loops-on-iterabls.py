li = ["Red","green","blue","Yellow"]

for color in li:
    print(color)

print("--------------------------------------------------------")

name = "Mohd Hamza"

for c in name:
    print(c)


print("--------------------------------------------------")

# price = 134_234_342 

# for n in price:
#     print(n)

size = {"XL","XXL","MD","SM","LG"}

for s in size:
    print(s)

print("--------------------------------------------------")

country_code = "+91","+92",'+42','+42'

for code in country_code:
    print(code)


### dictionary 

print("--------------------------------------------------")

phone_book = {
    "sadiq" : 9242934239,
    "rehman" : 234234239,
    "ali" : 324923942,
    "adil" : None ,
    "aman" : "+32 239239392"
}
# phone_book["sadiq"]
for name in phone_book:
    # if(name == "ali"):
    #     break
    print("key :",name, ",value : ", phone_book[name])