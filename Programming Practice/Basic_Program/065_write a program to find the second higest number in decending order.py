numbers = [12, 5, 7, 19, 1, 19]

# Remove duplicates, sort the list in descending order, and get the second element
second_highest = sorted(set(numbers), reverse=True)[1]

print("Second highest number:", second_highest)