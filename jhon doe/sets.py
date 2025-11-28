roll_no = {1,2,3,4,1}
print(roll_no)

# methods 

# add()

roll_no.add(5)
roll_no.add("5")
roll_no.add(5)
print(roll_no)


# clear 

my_set = {1, 2, 3, 4 , True}

# my_set.clear()
# my_set.remove(5)
# my_set.discard(5)
my_set.pop()
print(my_set)


my_set = {"Hello","hi","bye" , "UUUU"}
my_set.pop()
print(my_set)


# set operations 


set1 = {1, 2, 3 , 4}
set2 = {3, 4, 5,4,6}

# union 
new_set = set1.union(set2)
print(new_set)

# intersection 

common_set = set1.intersection(set2)
print(common_set)

# difference 

set1 = {1, 2, 3}
set2 = {3, 4, 5}

n = set1.difference(set2)
n2 = set2.difference(set1)
n3 = set2.symmetric_difference(set1)
print(n)
print(n2)
print(n3)

# subset 

a = {1,2,3}
b = {1,2}

h = b.issubset(a)
print(h)

superset = b.issuperset(a)
print(superset)

