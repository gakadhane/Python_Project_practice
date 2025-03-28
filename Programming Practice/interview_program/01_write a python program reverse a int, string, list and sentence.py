# What are other methods to reverse a list in Python?

# Using Slicing
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)
#----------------------------------------------------------------------------
# Using a Loop
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print(reversed_numbers)
#----------------------------------------------------------------------------
# Using the reversed() Function
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)
#----------------------------------------------------------------------------
# Using a Stack Approach: A stack follows the Last-In-First-Out (LIFO) principle, which can reverse the order.
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
while numbers:
    reversed_numbers.append(numbers.pop())
print(reversed_numbers)

#----------------------------------------------------------------------------------------------------------------------

# What are other methods to reverse a string in Python?

# Using slicing:
def reverse_string(rs):
    return rs[::-1]

Reverse_String = reverse_string("Hello")
print(Reverse_String)
#----------------------------------------------------------------------------
# Using a loop:
def reverse_string(s):
    reverse_s = ""
    for char in s:
        reverse_s = char + reverse_s

    return ''.join(char for char in reverse_s if char.lower() not in 'aeiou')

Reverse_String = reverse_string("Hello")
print(Reverse_String)

#----------------------------------------------------------------------------
# reverse a string using a recursive function:
def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:])+s[0]

example_string = "hello"
reversed_string = reverse_string(example_string)
print("Original string:", example_string)
print("Reversed string:", reversed_string)

#----------------------------------------------------------------------------
# Using the reversed() function:
def reverse_string(s):
    return (''.join(reversed(s)))

example_string = "hello"
print(reverse_string(example_string))
#----------------------------------------------------------------------------
# Using a Stack
text = "hello"
stack = list(text)  # Convert string to a list
reversed_text = ""
while stack:
    reversed_text += stack.pop()
print(reversed_text)  # Output: "olleh"
#----------------------------------------------------------------------------
# Reversing Each String in the List
string_list = ["apple", "banana", "cherry"]
reversed_each_string = [s[::-1] for s in string_list]
print(reversed_each_string)  # Output: ['elppa', 'ananab', 'yrrehc']
#----------------------------------------------------------------------------
# Reversing Both the List and Each String
string_list = ["apple", "banana", "cherry"]
reversed_both = [s[::-1] for s in string_list[::-1]]
print(reversed_both)  # Output: ['yrrehc', 'ananab', 'elppa']
#----------------------------------------------------------------------------
# Reversing  the List
string_list = ["apple", "banana", "cherry"]
reversed_both = [s for s in string_list[::-1]]
print(reversed_both)  # Output: ['cherry', 'banana', 'apple']
#----------------------------------------------------------------------------

# What are other methods to reverse a sentanse list in Python?

string_list = ["Hello world good morning"]
x = string_list[0][::-1]
print(x)            #gninrom doog dlrow olleH
#----------------------------------------------------------------------------

string_list = "Hello world good morning"
x = ' '.join(string_list.split()[::-1])  # Split the string into words, reverse the list, and join back
print(x)            #morning good world Hello
#----------------------------------------------------------------------------

# when list of number need to reverse and remove duplicate
# removes duplicates using a dictionary
# Original list of numbers
numbers = [1, 3, 45, 3, 4, 5, 6, 6, 7, 5, 8]

# Step 1: Remove duplicates while maintaining the original order
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)

# Step 2: Reverse the list
reversed_unique_numbers = unique_numbers[::-1]

print("Original list:", numbers)
print("Reversed list without duplicates:", reversed_unique_numbers)
#----------------------------------------------------------------------------

# Alternate Method Using set (Unordered Deduplication):
numbers = [1, 3, 45, 3, 4, 5, 6, 6, 7, 5, 8]
unique_numbers = list(set(numbers))[::-1]
print(unique_numbers)
reversed_unique_numbers = unique_numbers[::-1]
print("Reversed list without duplicates:", reversed_unique_numbers)
#----------------------------------------------------------------------------
def palin(s):

    return s == s[::-1]

print(palin("madam")) #O/p: True
#----------------------------------------------------------------------------
