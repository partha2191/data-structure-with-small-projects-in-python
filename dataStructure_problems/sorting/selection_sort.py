# Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
# Non-recursive array
# Time Complexity: O(N2)
# Auxiliary Space: O(1)

def selection_sort(arr): # 5 4 3 2 1
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n): # 4 3 2 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Take list as an input from the users
unsorted_array = [9,8,7,6,5,4,3,2,1]
print("Unsorted Array:", end=" ")
print(unsorted_array)

sortedArray = selection_sort(unsorted_array)
print("Sorted Array:", end=" ")
print(sortedArray)

