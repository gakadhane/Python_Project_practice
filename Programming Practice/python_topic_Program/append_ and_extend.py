#append() Method

my_list = [2,3,4,5,6,7,8,9]
my_list.append(2)
print(my_list)

my_list.append([4,5,6])
print(my_list)

# extend() Method

my_list2 = [1,3,5,7,9]
my_list2.extend([2,4,6,8])
print(my_list2)

my_list2.extend("abc")
print(my_list2)



# Create an empty list
new_list = [i for i in range(1, 11)]
print("List created using list comprehension:", new_list)


# Create an empty list
new_list = []

# Add elements using the `+` operator
new_list = new_list + [1]
new_list = new_list + [2]
new_list = new_list + [3]

print("List created using the + operator:", new_list)
