list_num = [33, 67, 22, 57, 78, 33, 7]

# Initialize variables for first and second highest numbers
first = second = float('-inf')  # Start with the lowest possible value

for num in list_num:
    if num > first:
        first, second = num, first  # Update both first and second
    elif first > num > second:
        second = num  # Update second highest if it lies between first and second

# Print the result
print("The second highest number is:", second)




# -----------------------------
list_num = [33, 67, 22, 57, 78, 33, 7]
highest = float('-inf')
for num in list_num:
    if num > highest:
        highest = num
print(highest)  # Outputs: 5
