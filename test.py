# 1. aaabbcdddc  print # a3b2c1d3c1
#
#
# str = ""
#
# for i in str():
#
"""
your_list = [3, 4, 6, 10, 12, 15, 16]
friend_list = [1, 5, 8, 11, 14]

O/p = Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 16]
e_lists(your_list, friend_list)
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


def bu_sort(arr_list):
    n = len (arr_list)
    for i in range (n):
        for j in range (0, n-i-1):
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
    return arr_list

your_list = [3, 4, 6, 10, 12, 15, 16]
friend_list = [1, 5, 8, 11, 14]

un_list = your_list+friend_list
sorted_list = bu_sort(un_list)
print(sorted_list)




list_in = [2, 7, 11, 15]
 # target) = 9

sum_list1 = list_in[0]
sum_list2 = list_in[2]

target = sum_list1 + sum_list2
print(sum_list1)
print(sum_list2)
print(target)

