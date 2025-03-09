
# [3,4,6,7,8,9,10] o/p:5

nums = [3, 4, 6, 7, 8, 9, 10]

# Find the missing number
for i in range(nums[0], nums[-1] + 1):
    if i not in nums:
        print(i)
        break
# ---------------------------------------------------------------
"""
Explanation:
The input list nums is sorted, so you can check each number in the range from the smallest (nums[0]) to the largest (nums[-1]).

The loop checks if each number in the range exists in the list. The first missing number, 5, is printed and the loop stops.
"""

#
# remove duplicate number and then find higest number
# [12, 24, 10, 15, 45, 5, 34, 10, 15, 34, 18, 34]


# Input list
list_num = [12, 24, 10, 15, 45, 5, 34, 10, 15, 34, 18, 34]

# Remove duplicates by converting the list to a set
unique_numbers = set(list_num)

# Find the highest number
highest_number = max(unique_numbers)

# Print the results
print("list number:", list_num)
print("Unique numbers:", unique_numbers)
print("Highest number:", highest_number)

# ------------------------------------------------------------
"""
Explanation:
Remove Duplicates: Convert list_num to a set using set(), which automatically removes duplicate values.

Find Highest Number: Use the max() function to determine the highest number in the set.

Output Results: Print both the unique numbers and the highest number for clarity.
"""

# ---------------------------------------------------------------------------------------
"""
your_list = [3, 4, 6, 10, 12, 15, 16]
friend_list = [1, 5, 8, 11, 14]

O/p = Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 16]
merge_lists(your_list, friend_list)
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


your_list = [3, 4, 6, 10, 12, 15, 16]
friend_list = [1, 5, 8, 11, 14]

un_list = your_list + friend_list
print(un_list)
sort_list = sorted(un_list)
print(sort_list)

# ----------------------------------------------------------------
list_in = [2, 7, 11, 15]
 # target) = 9

sum_list1 = list_in[0]
sum_list2 = list_in[2]

target = sum_list1 + sum_list2
print(sum_list1)
print(sum_list2)
print(target)




def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2