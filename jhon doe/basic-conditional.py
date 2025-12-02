age = int(float(input("Enter your age : ")))

if age >= 18 and age <= 100:
    print("You can drive car")
    print(f"Your age is {age}")
else:
    print("You can't drive car")
    print("Reason : You are not old enough")


print("------------------------------------------")

marks = -4000
is_correct = marks >= 0 and marks <= 100 # False
print(is_correct)

if marks >= 90 and is_correct:
    print("Grade A")
elif marks >= 70 and is_correct:
    print("Grade B")
elif marks >= 50 and is_correct:
    print("grade C")
elif marks > 33 and is_correct:
    print("Grade D")
elif marks == 33:
    print("Grade E")
else:
    print("Grade F")




    


