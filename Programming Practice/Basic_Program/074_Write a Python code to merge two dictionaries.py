# For Older Versions of Python (< 3.9):
# If you're using an older version of Python,
# you can merge the dictionaries using the update() method or dictionary unpacking (**):

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged) #{'a': 1, 'b': 3, 'c': 4}



dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge using update()
merged = dict1.copy()  # Make a copy of dict1
merged.update(dict2)   # Update it with values from dict2

print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}



# Using Dictionary Unpacking (Python 3.9+):
# If you're using Python 3.9 or newer, you can use the | operator to merge dictionaries:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries
merged = dict1 | dict2

print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}



