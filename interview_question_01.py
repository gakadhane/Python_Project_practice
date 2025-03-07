
[3,4,6,7,8,9,10] o/p:5

nums = [3, 4, 6, 7, 8, 9, 10]

# Find the missing number
for i in range(nums[0], nums[-1] + 1):
    if i not in nums:
        print(i)
        break

"""
Explanation:
The input list nums is sorted, so you can check each number in the range from the smallest (nums[0]) to the largest (nums[-1]).

The loop checks if each number in the range exists in the list. The first missing number, 5, is printed and the loop stops.
"""


remove duplicate number and then find higest number
[12, 24, 10, 15, 45, 5, 34, 10, 15, 34, 18, 34]


# Input list
list_num = [12, 24, 10, 15, 45, 5, 34, 10, 15, 34, 18, 34]

# Remove duplicates by converting the list to a set
unique_numbers = set(list_num)

# Find the highest number
highest_number = max(unique_numbers)

# Print the results
print("Unique numbers:", unique_numbers)
print("Highest number:", highest_number)


"""
Explanation:
Remove Duplicates: Convert list_num to a set using set(), which automatically removes duplicate values.

Find Highest Number: Use the max() function to determine the highest number in the set.

Output Results: Print both the unique numbers and the highest number for clarity.
"""


def merge_lists(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    # Sort the merged list
    sorted_list = sorted(merged_list)
    # Print the result
    print(sorted_list)

# Input lists
your_list = [3, 4, 6, 10, 12, 15, 16]
friend_list = [1, 5, 8, 11, 14]

# Call the function
merge_lists(your_list, friend_list)