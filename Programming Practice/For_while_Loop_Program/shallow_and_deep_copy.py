import copy

#shallow copy

my_item = [1,2,[3,4],5]
shallow_copy = copy.copy(my_item)

shallow_copy[2][0] = 8
print(my_item)
print(shallow_copy)



#deep copy

original = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original)

deep_copy[1][0] = 9
print(original)  # Output: [1, [9, 3], 4]
print(deep_copy)  # Output: [1, [9, 3], 4]


