# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restartthecomputer'
# Expected Result : 'resta$$$h$comp$$$'


# Function Definition: This defines a function named replace_specific_chars that takes a single argument s which is expected to be a string.
def replace_specific_chars(s):
    # List of Characters to Replace: Here, we create a list of characters chars_to_replace that we want to track and possibly replace in the input string.
    # In this case, the characters are 'r', 't', and 'e'.
    chars_to_replace = ['r', 't', 'e']

    # Dictionary to Track First Occurrence: We create a dictionary first_chars using a dictionary comprehension.
    # This dictionary will keep track of whether we have encountered the first occurrence of each character in chars_to_replace.
    # Initially, all values are set to False, indicating that none of the characters have been seen yet.
    first_chars = {char: False for char in chars_to_replace}

    # Result List: We initialize an empty list result to store the characters of the transformed string.
    result = []

    # Iterate Through Input String: We use a for loop to iterate through each character in the input string s.
    # The enumerate function provides both the index i and the character char.
    for i, char in enumerate(s):
        # Check and Replace Characters:
        # For each character in the input string:
        # If the character is in chars_to_replace:
        # 1. If it is the first occurrence (first_chars[char] == False), we append the character to the result list and mark its occurrence as True in the first_chars dictionary.
        # 2. If it is not the first occurrence (first_chars[char] == True), we append a dollar sign ('$') to the result list.
        # If the character is not in chars_to_replace, we simply append it to the result list.
        if char in chars_to_replace:
            if first_chars[char] == False:
                result.append(char)
                first_chars[char] = True
            else:
                result.append('$')
        else:
            result.append(char)
    # Join Result List to Form Final String: We join the elements of the result list into a single string and return it.
    return ''.join(result)


# Sample usage: We define a sample string sample_string and call the replace_specific_chars function with this string.
# The result is then printed.
sample_string = 'restartthecomputer'
result = replace_specific_chars(sample_string)
print(result)

# Here's how the transformation happens:
# 'r' is kept as is (first occurrence)
# 'e' is kept as is (first occurrence)
# 's', 'a' are kept as is
# Second 'r' is replaced with '$'
# 't' is kept as is (first occurrence)
# Second 't' is replaced with '$'
# 'h' is kept as is
# 'e' is replaced with '$'
# 'c', 'o', 'm', 'p', 'u' are kept as is
# Second 'e' is replaced with '$'
# 'r' is replaced with '$'
