# 53. Maximum Subarray

# using Kadane's algorithm
def max_subarray(arr):
    max_sum = arr[0]
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        # making current_sum 0 if it is negative because it will not contribute to the maximum sum, it will only decrease the sum
        if current_sum < 0:
            current_sum = 0

    return max_sum

    # max_sum = -99999
    # current_sum = 0
    # for i in range(len(arr)):
    #     current_sum = max(arr[i], current_sum + arr[i])
    #     max_sum = max(max_sum, current_sum)
    # return max_sum


# test cases
# print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
# print(max_subarray([1])) # 1
print(max_subarray([-5,-4,-1,-7,-8])) # 23
# print(max_subarray([])) # 0

# if we want to return the subarray
def max_subarray_return_array(arr):
    max_sum = 0
    current_sum = 0
    start, end = 0, 0

    for i in range(len(arr)):
        if current_sum == 0:
            start = i
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            end = i+1
        if current_sum < 0:
            current_sum = 0

    return arr[start:end]

# print(max_subarray_return_array([-2,1,-3,4,-1,2,1,-5,4])) # 6
# print(max_subarray([1])) # 1
# print(max_subarray_return_array([5,4,-1,7,8])) # 23
# print(max_subarray_return_array([])) # 0

# gfg problem Max sum in sub-arrays 
# Given an array Arr, with indexes running from 0 to N-1, select any two indexes, i and j such that i<=j-1. From subarray Arr[i...j], find the two smallest numbers and add them, you will get score for that subarray. Your task is to return maximum score possible in the given array Arr.
# this problem is just wanted to find the max sum of two consecutive elements

def max_sum_subarray(arr):
    maxsum = 0
    for i in range(len(arr)-1):
        maxsum = max(maxsum, arr[i] + arr[i+1])
    return maxsum

# using divide and conquer
def max_subarray2(arr):
    def divide_conquer(arr, left, right):
        if left == right:
            return arr[left]
        mid = (left + right) // 2
        left_sum = divide_conquer(arr, left, mid)
        right_sum = divide_conquer(arr, mid + 1, right)
        cross_sum = cross_subarray(arr, left, right, mid)
        return max(left_sum, right_sum, cross_sum)

    def cross_subarray(arr, left, right, mid):
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += arr[i]
            left_sum = max(left_sum, current_sum)

        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += arr[i]
            right_sum = max(right_sum, current_sum)

        return left_sum + right_sum

    return divide_conquer(arr, 0, len(arr) - 1)

# test cases
# print(max_subarray2([-2,1,-3,4,-1,2,1,-5,4])) # 6
# print(max_subarray2([1])) # 1
# print(max_subarray2([5,4,-1,7,8])) # 23