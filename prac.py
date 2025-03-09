from math import factorial

print("Hello")

# --------------------------------------------
def even_odd(x):
    return x % 2 == 0

print(even_odd(4))
print(even_odd(7))

# --------------------------------------------

str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print(result)

# --------------------------------------------

def maximun(a, b, c, d, e):
    return max(a, b, c, d, e)

print(maximun(23,45, 56,81,93))
# -------------------------------

def count_str(s):

    return sum(1 for char in s if char.lower() in 'aeiou' and char.upper() in 'AEIOU')

text_str = count_str('hfgweuyfgweuoaaAsoavehyiboxu ')
print(text_str)

# ----------------------------

def fact(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(fact(7))
# ----------------------------------



string = '123445'
int_str = int(string)
print(int_str)


string = 'hello'
int_str = str(string)
print(int_str)

# -------------------------------

def area(length, width):

    return length * width

rectagular = area(5, 10)
print(rectagular)

# -----------------

def palin(s):

    return s == s[::-1]

print(palin("madam"))

# ---------------------

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("The fox jumps over the lazy dog"))  # jumps


print(bool('none'))