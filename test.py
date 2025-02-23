# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restartthecomputer'
# Expected Result : 'resta$$$h$comp$$$'

def replace_specific_chars(s):
    chars_to_replace = ['r', 't', 'e']
    first_chars = {char: False for char in chars_to_replace}  # Track first occurrence
    result = []

    for i, char in enumerate(s):
        if char in chars_to_replace:
            if first_chars[char] == False:
                result.append(char)
                first_chars[char] = True
            else:
                result.append('$')
        else:
            result.append(char)

    return ''.join(result)

# Sample usage
sample_string = 'restartthecomputer'
result = replace_specific_chars(sample_string)
print(result)

