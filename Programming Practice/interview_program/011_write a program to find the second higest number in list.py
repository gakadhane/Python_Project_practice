list_num = [33, 67, 22, 57, 78, 33, 7]

# Initialize variables for first and second highest numbers
first = second = float('-inf')  # Start with the lowest possible value

for num in list_num:
    if num > first:
        first, second = num, first  # Update both first and second
    elif first > num > second:
        second = num  # Update second highest if it lies between first and second

# Print the result
print("The second highest number is:", second)           # Outputs: 67

#------------------------------------------------------------------------------------------
numbers = [12, 5, 7, 19, 1, 19]

# Remove duplicates, sort the list in descending order, and get the second element
second_highest = sorted(set(numbers), reverse=True)[1]

print("Second highest number:", second_highest)

# ------------------------------------------------------------------------------------------
list_num = [33, 67, 22, 57, 78, 33, 7]
highest = float('-inf')
for num in list_num:
    if num > highest:
        highest = num
print(highest)  # Outputs: 78
