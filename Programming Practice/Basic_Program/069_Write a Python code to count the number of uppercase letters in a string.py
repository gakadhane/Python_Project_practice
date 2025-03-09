def count_uppercase(s):

    return sum(1 for char in s if char.isupper())

print(count_uppercase("nHDkdbJGCH"))