# stop = int(input("Enter a num where loop stop : "))

# for i in range(0,101):
#    print(i)
#    if stop == i:
#       break 
#    print(i)


skip = int(input("Enter a num where loop skip : "))
table = 5
for i in range(1,11):
    if i == skip:
        continue
    print(f"{table} * {i} = ", table * i)