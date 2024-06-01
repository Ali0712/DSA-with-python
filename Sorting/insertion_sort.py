'''
Steps:
1. Start from the second element and compare it with the previous elements
2. If the second element is smaller than the first element, swap them
3. Continue this process until the entire array is sorted

Time Complexity:
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
Space Complexity: O(1)
Stability: Stable
In-place: Yes, it does not require any extra space

Insertion Sort is suitable for small datasets as its average and worst case complexities are of Ο(n2), where n is the number of items.
'''

def insertion_sort(arr):
    # n = len(arr)
    # for i in range(1, n):
    #     key = arr[i]
    #     j = i - 1
    #     while j >= 0 and key < arr[j]:
    #         arr[j+1] = arr[j]
    #         j -= 1
    #     arr[j+1] = key
    # return arr
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


# test cases
print(insertion_sort([64, 25, 12, 22, 11]))
print(insertion_sort([5, 2, 3, 1]))
print(insertion_sort([1, 2, 3, 2, 4 , -5, 4, 5, 1]))
print(insertion_sort([1, 2, 3, 4, 5]))

'''
Explanation:
The insertion sort algorithm is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

let us consider an example:
arr = [64, 25, 12, 22, 11]
In the first iteration, j = 0
Then while loop will run until j > 0 and arr[j] < arr[j-1], which is False
Next iteration, j = 1, and while loop will run until j > 0 and arr[j] < arr[j-1] = 25<64, which is True
So, arr[j-1] = 64, arr[j] = 25, so swap them
arr = [25, 64, 12, 22, 11]

'''