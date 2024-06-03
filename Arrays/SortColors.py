# 75. Sort Colors

# using Dutch National Flag Algorithm
def sort_colors(arr):
    low, high = 0, len(arr) - 1
    mid = 0
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr


# using counter approach
def sort_colors2(arr):
    counter = {}
    res = []
    for i in arr:
        if i == 0:
            counter['red'] = counter.get('red', 0) + 1
        elif i == 1:
            counter['white'] = counter.get('white', 0) + 1
        else:
            counter['blue'] = counter.get('blue', 0) + 1
    
    for i in range(counter.get('red', 0)):
        res.append(0)
    for i in range(counter.get('white', 0)):
        res.append(1)
    for i in range(counter.get('blue', 0)):
        res.append(2)
    
    return res

# test cases
print(sort_colors([2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(sort_colors([2,0,1])) # [0,1,2]
print(sort_colors([0])) # [0]
print(sort_colors([1])) # [1]
print(sort_colors([0,2,1])) # [0,1,2]
print(sort_colors([1,2,0])) # [0,1,2]
print(sort_colors([1,0,2])) # [0,1,2]
print(sort_colors([2,1,0])) # [0,1,2]
print(sort_colors([2,0,1,1,0,2])) # [0,0,1,1,2,2]
print(sort_colors([2,0,2,1,1,0,2,1,0])) # [0,0,0,1,1,1,2,2,2]
'''
Dutch National Flag Algorithm:
1. Initialize three pointers low, mid and high. low and mid are pointing to the start of the array and high is pointing to the end of the array.
2. Traverse the array from start to end using the mid pointer.
3. If the mid pointer is pointing to 0, swap the mid element with the low element and increment both low and mid pointers.
4. If the mid pointer is pointing to 1, increment the mid pointer.
5. If the mid pointer is pointing to 2, swap the mid element with the high element and decrement the high pointer.
6. Continue this process until the mid pointer is less than or equal to the high pointer.

Time complexity: O(n)

diagram:
0 -- low -1,   low --- mid -1,  mid --- high,   high +1  -- n-1 
all zeroes,      all ones,      unsorted part,     all twos
    '''