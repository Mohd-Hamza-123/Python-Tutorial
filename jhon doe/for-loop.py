# loop on range

repeat = 10 

num = 1 
# num = num + 1 # 2
# num = num + 1 # 3

for i in range(1,repeat + 1): # 0,1,2,3,4,5
    num = num + 1

print(num)


# loop on list

l = ["hello","hi","nye","bye"]

for element in l:
    print(element)

# loop on string

print("_________________________________")

string = "Mohd Hamza"

for c in string:
    print(c)


# loop on tuple 
print("_________________________________")

tup = ("red",1,"blue","tup",45,True)

for element in tup:
    print(element)


# loop on set 

s = {1,2,3,43,4,5}

for element in s:
    print(element)

# loop on dictionary 

product = {
    "name" : "Mohd Hamza",
    "address" : "Hello",
    "pincode" : 34534534,
    "isPassed" : True 
}


for k,v in product.items():
    print(k,v)

for n in 534534:
    print(n)