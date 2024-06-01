'''
Steps:
1. Choose a pivot element from the array
2. Partition the array such that all elements with values less than the pivot come before the pivot and all elements with values greater than the pivot come after it
3. Recursively apply the above steps to the sub-arrays on the left and right of the pivot
4. Continue this process until the entire array is sorted

Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n^2)
Space Complexity: O(log n)
Stability: Not stable
In-place: Yes, it does not require any extra space

Quick Sort is suitable for large datasets as its average and best case complexities are of Ο(n log n), where n is the number of items.
'''

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j



def quick_sort(arr):
    def quick(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick(arr, low, pivot_index-1)
            quick(arr, pivot_index+1, high)
    
    quick(arr, 0, len(arr)-1)
    return arr



# test cases
print(quick_sort([4, 6, 2, 5 ,7, 9, 1 ,3]))
print(quick_sort([5, 2, 3, 1]))
print(quick_sort([1, 2, 3, 2, 4 , -5, 4, 5, 1]))
print(quick_sort([1, 2, 3, 4, 5]))


# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low + 1
#     j = high

#     while True:
#         while i <= j and arr[i] <= pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break

#     arr[low], arr[j] = arr[j], arr[low]
#     return j

# def quick_sort(arr):
#     def _quick_sort(arr, low, high):
#         if low < high:
#             pivot_index = partition(arr, low, high)
#             _quick_sort(arr, low, pivot_index - 1)
#             _quick_sort(arr, pivot_index + 1, high)

#     _quick_sort(arr, 0, len(arr) - 1)

#     return arr

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)
