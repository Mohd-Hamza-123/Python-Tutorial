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
