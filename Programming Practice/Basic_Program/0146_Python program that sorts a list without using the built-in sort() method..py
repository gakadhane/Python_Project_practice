# Explanation:
# Function Definition: This defines the bubble_sort function, which takes a list arr as input.
def bubble_sort(arr):
    n = len(arr)  # Get the Length of the List: Here, we determine the length of the list and store it in n.

    for i in range(0, n, 1):
                     # Outer Loop (Passes): This loop runs n times, indicating each pass through the list. The 1 indicates a step of 1.
        for j in range(n - i - 1):
                  # Inner Loop (Comparisons): This loop handles the comparisons within each pass.
                  # With each pass, the largest element "bubbles up" to its correct position, so we compare only up to the last unsorted element (n - i - 1).
            if arr[j] > arr[j + 1]:
                  # Comparison and Swap:Here, adjacent elements are compared. If arr[j] is greater than arr[j + 1].
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                      # they are swapped. This process continues until the largest element in the unsorted portion is moved to its correct position.


unsorted_list = [23, 67, 3, 1, 56, 33, 90, 67, 39]
                   # Sorting the List: We create an unsorted_list, then call the bubble_sort function to sort it.
bubble_sort(unsorted_list)
print("sorted list:\n", unsorted_list)  # Print the Sorted List: Finally, we print the sorted list.

# Result:
# The code sorts the unsorted_list in ascending order using the bubble sort algorithm. Here’s what happens step-by-step:
# Pass 1: [23, 67, 3, 1, 56, 33, 67, 39, 90]
# Pass 2: [23, 3, 1, 56, 33, 67, 39, 67, 90]
# Pass 3: [3, 1, 23, 33, 56, 39, 67, 67, 90]
# Pass 4: [1, 3, 23, 33, 39, 56, 67, 67, 90]
# Pass 5: [1, 3, 23, 33, 39, 56, 67, 67, 90]
# And so on, until the list is fully sorted.
# In the end, unsorted_list becomes [1, 3, 23, 33, 39, 56, 67, 67, 90].


# set


set_line1 = {2, 4, 6, 6, 7, 4, 3, 3, 6}
set_line2 = {2, 4, 6, 6, 7, 4, 3, 3, 6}
set_line1.add(5)
set_line1.remove(2)
print(set_line1)
