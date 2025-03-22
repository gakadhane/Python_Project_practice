def count_uppercase(s):

    return sum(1 for char in s if char.isupper())

print(count_uppercase("nAHDkedbiJGoCHU"))

def remove_volwes(s):

    return ''.join(char for char in s if char.lower() not in 'aeiou')

print(remove_volwes("nAHDkedbiJGoCHU"))