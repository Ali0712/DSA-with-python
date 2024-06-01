'''
Steps:
1. Start from the first element and compare it with the second element
2. If the first element is greater than the second element, swap them
3. Continue this process until the entire array is sorted

Time Complexity: 
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
Space Complexity: O(1)
Stability: Stable
In-place: Yes, it does not require any extra space

Bubble Sort is not suitable for large datasets as its average and worst case complexities are of Ο(n2), where n is the number of items.
'''

def bubble_sort(arr):
    # n = len(arr)
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #         if arr[j] > arr[j+1]:
    #             # swap
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # return arr
    n = len(arr) 
    isSwap = False
    for i in range(n-1, 0, -1):  
        for j in range(i):   
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwap = True
        if not isSwap:
            break
    return arr


# test cases
print(bubble_sort([64, 25, 12, 22, 11]))
print(bubble_sort([5, 2, 3, 1]))
print(bubble_sort([1, 2, 3, 2, 4 , -5, 4, 5, 1]))
print(bubble_sort([1, 2, 3, 4, 5]))
