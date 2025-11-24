product = {
    "name" : "shampoo",
    "price" : 100.00,
    "description" : "It is a shampoo",
    "discount" : 30,
    "in_stock" : True,
}

# print(product)
# print("product price = ",product["price"])
# print("stock = ",product["in_stock"])


user = {
    "username" : "Mohd Hamza",
    "email" : "hamza@gmail.com",
    "password" : 3429432,
}

# print(user["email"])
print(user)
user["secret_password"] = "adslkf43985349"
user["age"] = 344
user["username"] = "Sadiq"
print(user)
del user["age"]
print(user)

# colors = {
#     "0" : "Red",
#     "1" : "Blue",
#     "2" : "Green"
# }
# print(colors["0"])