# get()

product = {
    "name" : "Kurkure",
    # "name" : "Crax",
    "description" : "It is a snack",
    "price" : 299,
    "isVeg" : True,
    "variant" : ["Mirchi","Mango","Sweet"],
    "manufactured" : {
        "place" : "India",
        "pincode" : 234289
    }
}

a = product.get("mfg-date")
# b = product["mfg-date"] key error 
print(a)
print("4534534")

# popitem()

person = {"name": "John", "age": 30, "city": "New York"}

person.popitem()
print(person)

# pop(key-name)

person = {"name": "John", "age": 30, "city": "New York"}
person.pop("name")

print(person)


#  clear

product = {
    "name" : "Kurkure",
    # "name" : "Crax",
    "description" : "It is a snack",
    "price" : 299,
    "isVeg" : True,
    "variant" : ["Mirchi","Mango","Sweet"],
    "manufactured" : {
        "place" : "India",
        "pincode" : 234289
    }
}

product.clear()

print(product)