
def count_str(s):

    return sum(1 for char in s if char.lower() in 'aeiou' and char.upper() in 'AEIOU')

text_str = count_str('hfgweuyfgweuoaaAsoavehyiboxu ')
print(text_str)

# ----------------------------------------------------------------------------
def reverse_string(s):
    reverse_s = ""
    for char in s:
        reverse_s = char + reverse_s

    return ''.join(char for char in reverse_s if char.lower() not in 'aeiou')

Reverse_String = reverse_string("Hello")
print(Reverse_String)

# ----------------------------------------------------------------------------
