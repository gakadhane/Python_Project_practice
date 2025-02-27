#String Slicing:
text = "Hello, World!"
print(type(text))
print(text[0:5])  # Output: Hello
print(text[7:12])  # Output: World
print(text[:5])  # Output: Hello (same as text[0:5])
print(text[7:])  # Output: World! (same as text[7:len(text)])
print(text[::2])  # Output: Hlo ol! (every second character)
print(text[::-1])  # Output: !dlroW ,olleH (reversed string)

#List Slicing:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers))
print(numbers[2:5])  # Output: [2, 3, 4]
print(numbers[:3])  # Output: [0, 1, 2]
print(numbers[5:])  # Output: [5, 6, 7, 8, 9]
print(numbers[::2])  # Output: [0, 2, 4, 6, 8] (every second element)
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed list)

#Tuple Slicing:
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(type(letters))
print(letters[1:4])  # Output: ('b', 'c', 'd')
print(letters[:3])  # Output: ('a', 'b', 'c')
print(letters[4:])  # Output: ('e', 'f', 'g')
print(letters[::2])  # Output: ('a', 'c', 'e', 'g')
print(letters[::-1]) # Output: ('g', 'f', 'e', 'd', 'c', 'b', 'a') (reversed tuple)

#----------------------------------------------------------------------------


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Slicing first 2 rows
print("First 2 rows:", matrix[:2])

# Slicing first 2 columns of each row
print("First 2 columns of each row:", [row[:2] for row in matrix])

# Slicing diagonal elements (not exactly slicing, but extracting for demonstration)
print("Diagonal elements:", [matrix[i][i] for i in range(len(matrix))])

#----------------------------------------------------------------------------


sample_string = "Hello, World!"

# Slicing only vowels from the string
vowels = 'aeiouAEIOU'
sliced_vowels = ''.join([char for char in sample_string if char in vowels])
print("Vowels in the string:", sliced_vowels)

#----------------------------------------------------------------------------

sample_string = "Hello, World!"

# Slicing only vowels from the string
vowels = 'aeiouAEIOU'
sliced_vowels = ''.join([char for char in sample_string if char not in vowels])
print("Vowels in the string:", sliced_vowels)
