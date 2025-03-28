# For Older Versions of Python (< 3.9):
# If you're using an older version of Python,
# you can merge the dictionaries using the update() method or dictionary unpacking (**):

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#----------------------------------------------------------------------------------------------

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge using update()
merged = dict1.copy()  # Make a copy of dict1
merged.update(dict2)   # Update it with values from dict2

print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

#----------------------------------------------------------------------------------------------

# Using Dictionary Unpacking (Python 3.9+):
# If you're using Python 3.9 or newer, you can use the | operator to merge dictionaries:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

#----------------------------------------------------------------------------------------------

#insert key value in dictionary
# Original dictionary
my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date"}

# Convert the dictionary into a list of items (key-value pairs)
items = list(my_dict.items())

# Insert the new key-value pair between the 2nd and 3rd index
items.insert(2, (5, "mango"))  # Insert key=5, value="mango" at 3rd position (index 2)

# Convert the list of items back to a dictionary
updated_dict = dict(items)

print("Updated Dictionary:", updated_dict)          #Updated Dictionary: {1: 'apple', 2: 'banana', 5: 'mango', 3: 'cherry', 4: 'date'}

#------------------------------------------------------------
# fetch key or value
my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date"}

key_list = list(my_dict.keys())
print(key_list[-1], "-", my_dict[key_list[-1]])         #4 - date

#-------------------------------------------------------------------

#update/replace key value
# Original dictionary
my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date", 5: "my_dict"}

# Using a loop to create a new dictionary with the desired changes
updated_dict = {}
for key, value in my_dict.items():
    if key == 3:
        updated_dict[6] = "badam"  # Replace key 3 with 6 and value with "badam"
    else:
        updated_dict[key] = value  # Keep the rest of the key-value pairs unchanged

# Display the updated dictionary
print("Updated dictionary:", updated_dict)          #Updated dictionary: {1: 'apple', 2: 'banana', 6: 'badam', 4: 'date', 5: 'my_dict'}

#-------------------------------------------------------------------

# Original dictionary
my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date", 5: "my_dict"}

# Updating the key-value pair in one step by creating a new dictionary
my_dict = {key: value for key, value in my_dict.items() if key != 3}  # Remove the key 3
my_dict[6] = "badam"  # Add new key-value pair

# Display the updated dictionary
print("Updated dictionary:", my_dict)                   #Updated dictionary: {1: 'apple', 2: 'banana', 4: 'date', 5: 'my_dict', 6: 'badam'}


#-------------------------------------------------------------------

# Original dictionary
my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date", 5: "my_dict"}

# Changing the key-value pair for the key 3 to 6: "badam"
my_dict.pop(3)  # Remove the key-value pair with key 3
my_dict[6] = "badam"  # Add the new key-value pair

# Display the updated dictionary
print("Updated dictionary:", my_dict)               #Updated dictionary: {1: 'apple', 2: 'banana', 4: 'date', 5: 'my_dict', 6: 'badam'}
#-------------------------------------------------------
# fetch value only
# Original dictionary
my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date", 5: "my_dict"}

# Fetching only the values
values = list(my_dict.values())

# Display the result
print("Values:", values)

#-----------------------------
# Original dictionary
my_dict = {1: "apple", 2: "banana", 3: "cherry", 4: "date", 5: "my_dict"}

# Fetching only the values using list comprehension
values = [value for value in my_dict.values()]

# Display the result
print("Values:", values)