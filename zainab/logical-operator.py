age = 18
driving_license = "Yes"
have_insurance = "Yes"

isDrive = (age >= 18) and (driving_license == "Yes") and (have_insurance == "Yes")
# and => true and true = true
# and => true and false = false 
# and => false and false = false 

print("isDrive : ",isDrive)


# or 

age = 13
special_pass = "Yes"

isDrive = (age>= 18) or (special_pass == "Yes")
print("isDrive : ",isDrive)


# not 

is_dark_mode = False
hhh = not is_dark_mode
print(is_dark_mode)