def count_vowels(s):

    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels("Hello World"))  # 3

#-----------------------------------------------------------------------------

def lower_vowels(s):

    return ''.join(char for char in s if char.lower() not in 'aeiou')

print(lower_vowels("Hello"))

# ----------------------------------------------------------------------------

def upper_vowels(s):

    return ''.join(char for char in s if char.upper() in 'AEIOU')

print(upper_vowels("HEllO"))

#----------------------------------------------------------------------------

def num_vowels(s):

    return ''.join(char for char in s if char.isalnum() and char.isalpha())

print(num_vowels("123HEllO"))
