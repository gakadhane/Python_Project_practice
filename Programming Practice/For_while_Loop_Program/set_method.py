# Union of sets

set1 = {1,2,3,4,5}
set2 = {5,6,7,8}
union_set = set1.union(set2)
print(union_set)

# Intersection of sets
intersection = set1.intersection(set2)
print(intersection)

# Difference of sets

difference_set = set1.difference(set2)
print(difference_set)

# Symmetric difference of sets
sys = set1.symmetric_difference(set2)
print(sys)

print(len(set2))


set3 = {1,2,3,4}
set4 = {1,2,3,4,5,6,7}
#issubset() and issuperset()
print(set3.issubset(set4))
print(set4.issubset(set3))

print(set3.issuperset(set4))
print(set4.issuperset(set3))