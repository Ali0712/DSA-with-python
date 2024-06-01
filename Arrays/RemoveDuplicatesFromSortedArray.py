# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    
    if len(nums) == 0:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1
    
print(removeDuplicates([2,3,3,3,3,4,5,5,6,6,6,6,6,9,9,12]))
print(removeDuplicates([1,1,2]))
print(removeDuplicates([1,1,1]))
print(removeDuplicates([1,2,3,4,5,6,7,8,9,10]))

# 2nd approach

def remove_duplicates(arr):
    '''this function removes the duplicates from a sorted array and return the length of array'''
    
    # for i in range(len(arr)-1):
    #     if arr[i] == arr[i+1] :
    #         arr.pop(i)
    # return arr

    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr.pop(i)
        else:
            i += 1

    return len(arr)


# test cases
# print(remove_duplicates([2,3,3,3,3,4,5,5,6,6,6,6,6,9,9,12]))
# print(remove_duplicates([1,1,2]))
# print(remove_duplicates([1,1,1]))
# print(remove_duplicates([1,2,3,4,5,6,7,8,9,10]))