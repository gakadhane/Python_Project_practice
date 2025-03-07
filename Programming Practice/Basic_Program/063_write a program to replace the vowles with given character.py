my_string = input("enter the string:\n ")
my_char = input("enter the char to replace:\n ")

vowels = ('a','e','i','o','u','A','E','I','O','U')

new_string = ''

for i in my_string:
    if i in vowels:
        new_string += my_char
    else:
        new_string += i

print(new_string)