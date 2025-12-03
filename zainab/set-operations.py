set1 = {1, 2, 3 ,4}
set2 = {3, 4, 5 ,6}

set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)
print(set3)
print(set4)
print(set5)
print(set6)

# superset and subset 

set1 = {1,2, 3}
set2 = {1, 2 }

print(set1.issubset(set2))
print(set2.issubset(set1))

print(set1.issuperset(set2))
print(set2.issuperset(set1))
