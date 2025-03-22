def palin(s):

    return s == s[::-1]

print(palin("madam"))

# ------------------------------------

def is_palindrome(s):
    # Remove spaces, punctuation, and make the string lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())

    # Compare characters from the beginning and end of the string
    start = 0
    end = len(cleaned_str) - 1
    while start < end:
        if cleaned_str[start] != cleaned_str[end]:
            return False  # Not a palindrome
        start += 1  # Move start pointer forward
        end -= 1  # Move end pointer backward
    return True  # It's a palindrome

# Test the function
test_str = "A man, a plan, a canal, Panama"
if is_palindrome(test_str):
    print(f'"{test_str}" is a palindrome!')
else:
    print(f'"{test_str}" is NOT a palindrome.')



# --------------------------------

def is_palindrome_recursive(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Define a helper function for the recursive check
    def helper(start, end):
        # Base case: If start crosses end, it's a palindrome
        if start >= end:
            return True
        # Check if characters at current indices are equal
        if s[start] != s[end]:
            return False
        # Recursive step: Move towards the center
        return helper(start + 1, end - 1)

    return helper(0, len(s) - 1)

# Test the function
test_str = "A man, a plan, a canal, Panama"
if is_palindrome_recursive(test_str):
    print(f'"{test_str}" is a palindrome!')
else:
    print(f'"{test_str}" is NOT a palindrome.')

#------------------------------------------------------------------------

def is_palidrom(stirng):
    string = string.lower().replace(" ", "")
    return string == string[::-1]


string = input("enter the string:")

