def longest_word(sentence):

    words = sentence.split()
    print(words)
    return max(words, key=len)

print(longest_word("The fox jumpssss over the lazy dog"))  # jumps

# ----------------------------------------------------------------------------

def maximun(a, b, c, d, e):
    return max(a, b, c, d, e)

print(maximun(23,45, 56,81,93))

# ----------------------------------------------------------------------------

def maximun(a, b, c, d, e):
    return min(a, b, c, d, e)

print(maximun(23,45, 56,81,93))