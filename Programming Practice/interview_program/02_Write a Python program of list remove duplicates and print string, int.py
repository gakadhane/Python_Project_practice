# remove duplicate
list1 = [1, 2, 2, 3, 4, 4]

unique_list1 = list(set(list1))
print(unique_list1) #[1, 2, 3, 4]

#---------------------------------------

# Original list of numbers
numbers = [1, 3, 45, 3, 4, 5, 6, 6, 7, 5, 8]

# Step 1: Remove duplicates while maintaining the original order
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)
#---------------------------------------

# Alternate Method Using set (Unordered Deduplication):
numbers = [1, 3, 45, 3, 4, 5, 6, 6, 7, 5, 8]
unique_numbers = list(set(numbers))
print(unique_numbers)


#---------------------------------------



#list of string and int  convert into string
# Original list
my_list = ['p', 'y', 't', 'h', 'o', 'n', 3]

# Convert each element to a string and join them
#The map(str, my_list) ensures all elements (including numbers) are converted to strings, and ''.join combines them into a single string.
result = ''.join(map(str, my_list))

# Display the result
print("Converted string:", result)          #Converted string: python3

#----------------------------------------
# list to string converter
my_list = ['p', 'y', 't', 'h', 'o', 'n']

# Convert each element to a string and join them
result = ''.join(my_list)

# Display the result
print("Converted string:", result)              #Converted string: python
#---------------------------------
#set to string converter
my_list = {'p', 'y', 't', 'h', 'o', 'n'}

# Convert each element to a string and join them
result = ''.join(my_list)

# Display the result and  output not in order because of set.
print("Converted string:", result)          #Converted string: thynop

#-----------------------------------
#set to string converter
my_list = {"A": "apple", "B": "banana", 3: "cherry", "D": "date", "E": "my_dict"}

# Convert each element to a string and join them
result = ''.join(map(str,my_list.keys()))

# Display the result and  output not in order because of set.
print("Converted string:", result)          #Converted string: AB3DE
"""
Explanation:
Keys Only: The my_list.keys() retrieves all keys from the dictionary.
Convert to String: The map(str,my_list.keys()) ensures non-string keys (like 3) are converted into strings.
Join Together: The ''.join combines the keys into a single string.
"""