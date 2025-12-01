product = ["Kurkure", "this is description",]

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

print(product)

# access key-value 

a = product["name"]
b = product["manufactured"]["place"]
print(a)
print(b)

# delete key-value 

del product["isVeg"]

print(product)

# update 

product["name"] = "Crax"
product["mfg-date"] = "12/02/2000"

print(product)