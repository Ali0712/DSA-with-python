# 189. Rotate Array (rotate array to the right by k steps)

'''
Notes:
arr = [1,2,3,4,5,6,7]
rotate right means: [7,1,2,3,4,5,6] shift all elements to the right by 1 and move the last element to the first
rotate left means: [2,3,4,5,6,7,1] shift all elements to the left by 1 and move the first element to the last

Also note that if k is greater than the length of the array, then k = k % len(arr)
e.g. arr = [1,2,3,4,5,6,7] and k = 3, then k = 3 % 7 = 3
if k = 10, then k = 10 % 7 = 3

'''

def rotate_right_by1(nums):
    temp = nums[-1]
    for i in range(len(nums)-1, 0, -1):
        nums[i] = nums[i-1]
    nums[0] = temp
    return nums

# test cases
# print(rotate_right_by1([1,2,3,4,5,6,7]))



# 2nd approach , better approach
def rotate_right2(nums, k):
    '''this function rotates the array to the right by k steps using reverse method'''
    k = k % len(nums)

    reverse(nums, 0, len(nums)-k-1)
    reverse(nums, len(nums)-k, len(nums)-1)
    reverse(nums, 0, len(nums)-1)

    return nums
    

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# test cases
# print(rotate_right2([1,2,4,5,6,7], 3))
# print(rotate_right2([-1,-100,3,99,4,5,7,2], 2))
# print(rotate_right2([1,2,3,4,5,6,7], 1))

# Rotate array to the left by k steps

def rotate_left_by_1(nums):
    temp = nums[0]
    for i in range(len(nums)-1):
        nums[i] = nums[i+1]
    nums[-1] = temp
    return nums

# test cases
# print(rotate_left_by_1([1,2,3,4,5,6,7]))

def rotate_left(nums, k):
    k = k % len(nums)

    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    reverse(nums, 0, len(nums)-1)

    return nums


print(rotate_left([1,2,3,4,5,6,7], 2))
