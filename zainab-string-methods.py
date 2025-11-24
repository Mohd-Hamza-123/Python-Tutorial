# strip method 

email = "           hamza @gmail.com            "
correct_email = email.strip()
print(correct_email)
print(email) # no change 

# lower()

username = "MOHD HamZa"
correct_username = username.lower()
print("correct username = ",correct_username)
# print(username)

# upper()

pancard_no = "bleph33he"
correct_pancard_no = pancard_no.upper()
print("pancard no = ",correct_pancard_no)

# replace("old text","new text")

email = "hamza@yahoo.com"
correct_email = email.replace("yahoo","gmail")
print("email : ",correct_email)

# startswith("prefix")

number = "+91 382938492382"
is_number_indian = number.startswith("+91")
print("is_no_indian = ",is_number_indian)

# endswith("suffix")

file_name = input("Enter file Name : ")
is_python_file = file_name.endswith(".py")
print("is Python file = ",is_python_file)

# count("letter")

word = input("Enter a word : ")
find_letter = input("Enter word/letter you want to know its count : ")

word_count = word.count(find_letter)
print(f"count of {find_letter} = ",word_count)

# capitalize()

para = "it is a sun"
c_para = para.capitalize()
print(c_para)

# title()

para = "it is a cat"
t_para = para.title()
print(t_para)


# upper() & lower() & isalpha() & isdigit

text = input("Enter a text : ")
is_upper = text.isupper()
is_lower = text.islower()
is_alpha = text.isalpha()
is_digit = text.isdigit()
print(f"{text} , upper = ",is_upper, "lower = ",is_lower)
print(f"is text ({text}) alphabet = ",is_alpha)
print(f"{text} is digit = ",is_digit)



# find()

a = "Hello Word"
index_of_e = a.find("e")
index_of_o = a.find("o")
index_of_w = a.find("w")
index_of_Word = a.find("Word")
print(index_of_e)
print(index_of_o)
print(index_of_w)
print(index_of_Word)


