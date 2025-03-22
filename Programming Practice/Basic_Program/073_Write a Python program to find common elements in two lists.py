list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common) #[3, 4]


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

union = set1.union(set2)
print(union)

intersection_set = set1.intersection(set2)
print(intersection_set) # Output: {3}
