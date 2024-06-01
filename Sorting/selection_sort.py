'''
Steps:
1. Find the smallest element in the array
2. Swap it with the first element
3. Then find the second smallest element in the array
4. Swap it with the second element
5. Continue this process until the entire array is sorted

Time Complexity: 
    Best Case: O(n^2)
    Average Case: O(n^2)
    Worst Case: O(n^2)
Space Complexity: O(1)
Stability: Not stable, as it does not maintain the relative order of equal elements. In other words, if two elements are equal according to the sorting criterion, they remain in the same relative order in the sorted output as they were in the input.

In-place: Yes, it does not require any extra space

Selection Sort is not suitable for large datasets as its average and worst case complexities are of Ο(n2), where n is the number of items.
'''

def selection_sort(arr):
    # n = len(arr)
    # for i in range(n):
    #     min_index = i
    #     for j in range(i+1, n):
    #         if arr[j] < arr[min_index]:
    #             min_index = j
    #     # swap
    #     arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # return arr
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# test cases
print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([5, 2, 3, 1]))
print(selection_sort([1, 2, 3, 2, 4 , -5, 4, 5, 1]))
print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 4, 3, 2, 1]))
