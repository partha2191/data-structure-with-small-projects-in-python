# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
# Time Complexity: O(N2)
# Auxiliary Space: O(1)

def bubble_sort(arr) : # length of 10
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr;

# Take list as an input from the users
unsorted_array = [9,8,7,6,5,4,3,2,1]
print("Unsorted Array:", end=" ")
print(unsorted_array)

sortedArray = bubble_sort(unsorted_array)
print("Sorted Array:", end=" ")
print(sortedArray)

