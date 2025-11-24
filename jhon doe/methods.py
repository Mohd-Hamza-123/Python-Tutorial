# important : get("key-name")


product = {
    "name" : "shampoo",
    "price" : 100.00,
    "description" : "It is a shampoo",
    "discount" : 30,
    "in_stock" : True,
}

a = product["name"]
print("simple way : ",a)
# expiry = product["expiry_date"]
# print(expiry)
a = product.get("name")
print("get method : ",a)
expiry = product.get("expiry-date")
print(expiry)
# print("Hello wrod")


# pop("key-name")

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# del person["address"] raise error
# x = person.pop("address") # raise error
# print(x)

person.pop("age")
print(person)



# popitem()

user = {
    "username" : "Mohd Hamza",
    "email" : "hamza@gmail.com",
    "password" : 3429432,
}

user.popitem()

print(user)

# update(dictionary)

shirt = {
    "company" : "Raymond",
    "price" : 4000
}
db_shirt = {"company" : "Nike", "price" : 2000,"is_available" : True}
shirt.update(db_shirt)
print(shirt)


# keys()  & values()


product = {
    "name" : "shampoo",
    "price" : 100.00,
    "description" : "It is a shampoo",
    "discount" : 30,
    "in_stock" : True,
}

product_keys = product.keys()
product_values = product.values()
print(product_keys)
print(product_values)

product.clear()
print(product)

