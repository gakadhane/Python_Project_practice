#capitalize():

string1 = "   hello    world   "
print(string1.capitalize())

#upper():
print(string1.upper())

#lower
print(string1.lower())

#strip
print(string1.strip())

#split
print(string1.split())

#join
list_of_string = ",".join(string1)
print(list_of_string)

#replace
new_string = string1.replace("world", "Python")
print(new_string)

#start with
print(string1.startswith("   hello"))

#end with

print(string1.endswith("world   "))

#find
print(string1.find("world"))