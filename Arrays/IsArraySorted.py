# 1752. Check if Array Is Sorted and Rotated

def check(arr):
    '''this function checks if the array is sorted and rotated or not'''
    
    count = 0
    for i in range(len(arr)):
        if arr[i] > arr[(i+1)%len(arr)]: # this condition was given in the question
            count += 1
    return count <= 1

'''
Explanation:
1. We will iterate through the array and check if the current element is greater than the next element.
2. If it is greater, we will increment the count.
3. If the count is less than or equal to 1, then the array is sorted and rotated.
4. If the count is greater than 1, then the array is not sorted and rotated.

'''
# test cases
print(check([3,4,5,1,2]))
print(check([2,1,3,4]))
print(check([1,2,3]))

def check2(arr):
    l = 0
    f = 1
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            l = i+1
        else:
            f = 0
            break
    if f:
        return True
    last = arr[-1]
    for k in range(l+1, len(arr)-1):
        if arr[k] > arr[k+1]:
            return False
        last = arr[k+1]

    if arr[0] < last:
        return False
    for j in range(l):
        if arr[j] > arr[j+1]:
            return False
    
    return True

def is_sorted(arr):
    '''this function checks if the array is sorted or not'''
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


# test cases
# print(is_sorted([2,43,5,7,2,65,9,3,1]))
# print(is_sorted([1,4,6,8,9]))
