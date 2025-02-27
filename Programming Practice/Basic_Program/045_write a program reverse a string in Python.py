
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
