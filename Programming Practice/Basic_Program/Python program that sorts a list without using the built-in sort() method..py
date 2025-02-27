def bubble_sort(arr):
    n = len(arr)

    for i in range(0,n,1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

unsorted_list = [23,67,3,1,56,33,90,67,39]
bubble_sort(unsorted_list)
print("sorted list:\n", unsorted_list)




#set


set_line1 = {2,4,6,6,7,4,3,3,6}
set_line2 = {2,4,6,6,7,4,3,3,6}
set_line1.add(5)
set_line1.remove(2 )
print(set_line1)
