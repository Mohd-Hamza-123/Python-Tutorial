# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))

def MaximumNo(num1,num2):
    if(num1 > num2):
        return num1
    else:
        return num2
    

# max_num = MaximumNo(num1,num2)
# print("Max num = ",max_num)



def addListElements(l):
    # print("parameter : ",l)
    sum = 0
    for element in l:
        sum = sum + element
    return sum


list1 = [-2,-4]
total = addListElements(list1)
print(total)

