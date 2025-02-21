# List of tuples
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]

# Convert list into dictionary
dictionary = dict(list_of_tuples)

print(dictionary)




# List of keys and values
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Convert lists into dictionary
dictionary = dict(zip(keys, values))

print(dictionary)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)




