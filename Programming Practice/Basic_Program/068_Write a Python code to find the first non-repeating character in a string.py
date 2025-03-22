def first_repeating_char(s):
    char_set = set()
    # Iterate through the characters in the string
    for char in s:
        if char in char_set:
            return char  # Return the first repeating character
        char_set.add(char)
    return None  # Return None if there are no repeating characters

# Test the function
print(first_repeating_char("nxtwavea"))  # Output: a

#--------------------------------------------------------------------------
def all_repeating_chars(s):
    char_set = set()
    repeating_chars = set()  # Use a set to store all repeating characters

    # Iterate through the characters in the string
    for char in s:
        if char in char_set:
            repeating_chars.add(char)  # Add the repeating character to the set
        else:
            char_set.add(char)

    return list(repeating_chars)  # Return the repeating characters as a list


# Test the function
print(all_repeating_chars("nxttwaveae"))  # Output: ['t', 'a']