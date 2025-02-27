#Reversing a List Using Slicing

def reverse_list(lst):
    return lst[::-1]

# Sample usage
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)



#Reversing a List Using a Loop
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# Sample usage
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)


#Reversing a String Using a Loop

def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

# Sample usage
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)

