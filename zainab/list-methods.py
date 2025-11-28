size_options = ["SM","MD","XL", "XXL"]

# append(element)

# size_options[4] = "ETL" indexError
print("old size optins : ",size_options)
size_options.append("ETL")
size_options.append("EETL")
print("new size options : ",size_options)



# extend(newList)

color_options = ["Red","Blue","Yellow"]
new_colors_options = ["Crimson","Pink","Green"]

color_options.extend(new_colors_options)
print("new colors : ",color_options)


name1 = ["Nehal","Raji"]
name2 = ["Hamza","Herald"]

name3 = name1 + name2 + color_options
print("name1 : ",name3)


# insert(index,value)

phone_no = [999,111,222,444]
phone_no.insert(1,333)
print("new phoneno" , phone_no)

# clear()

colors_options = ["Crimson","Pink","Green"]
color_options.clear()
print("color options : ",color_options)

# index()

colors = ["Crimson","Pink","Green"]

index_of_pink = colors.index("Green")
print("index of pink",index_of_pink)

# count()

my_list = [1, 2, 3, 2, 2, 4,"2"]
c = my_list.count("2")
print(c)

# sort 

my_list = [5, 2, 9, 1, -3,3,53,5,5]
my_list.sort() # ascending
print(my_list)
my_list.sort(reverse=True)  # descending
print(my_list)

# reverse 

size_options = ["SM","MD","XL", "XXL"] 
size_options.reverse()
print(size_options)

# pop 

hh = [999, 333, 111, 222, 444]
hh.pop()
print(hh)