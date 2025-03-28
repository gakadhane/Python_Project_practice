a = {1, 2, 3, 4}
b = {5, 6, 3, 2}

# Find common elements using list comprehension
common = [item for item in a if item in b]

if common:
    print("Common", set(common))
else:
    print("No common elements.")
#----------------------------------------------------------------------------------------------
a = [1, 2, 3, 4]
b = [2, 3, 5, 6]
c = [1, 2, 3, 7]

# Convert lists to sets and find common elements
res = set(a).intersection(b, c)
print(f"Common elements: {res}")

#----------------------------------------------------------------------------------------------
a = [1, 2, 3, 4]
b = [2, 3, 5, 6]
c = [1, 2, 3, 7]

# Set comprehension to find common elements
res = {x for x in a if x in b and x in c}
print(f"Common elements: {res}")

# Filter common elements
res = set(filter(lambda x: x in b and x in c, a))
print(f"Common elements: {res}")
#----------------------------------------------------------------------------------------------
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common) #[3, 4]
#----------------------------------------------------------------------------------------------
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

union = set1.union(set2)
print(union)
#----------------------------------------------------------------------------------------------

intersection_set = set1.intersection(set2)
print(intersection_set) # Output: {3}
#----------------------------------------------------------------------------------------------
