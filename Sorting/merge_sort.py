'''
Steps:
1. Divide the array into two halves
2. Recursively sort the two halves
3. Merge the two halves

Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n log n)
Space Complexity: O(n)
Stability: Stable
In-place: No

Merge Sort is suitable for large datasets as its average and worst case complexities are of Ο(n log n), where n is the number of items.
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r+=1

    while l < len(left):
        merged.append(left[l])
        l += 1
    while r < len(right):
        merged.append(right[r])
        r+=1

    return merged



# test cases
print(merge_sort([64, 25, 12, 22, 11]))
print(merge_sort([5, 2, 3, 1]))
print(merge_sort([1, 2, 3, 2, 4 , 5, 4, -5, 1]))
print(merge_sort([1, 2, 3, 4, 5]))


