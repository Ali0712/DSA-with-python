
# this is the optimized approach if array contains both positive and negative numbers
def len_of_longest_subarray(arr, k):
    '''Given an array of integers, find the length of the longest subarray with sum equal to k.'''
    max_len = 0
    curr_sum = 0
    prev = {}

    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == k:
            max_len = max(max_len, i+1)
        
        rem = curr_sum - k
        if rem in prev:
            length = i - prev[rem]
            max_len = max(length, max_len)
        
        if curr_sum not in prev:
            prev[curr_sum] = i
    
    return max_len

# test cases

# print(len_of_longest_subarray([10, 5, 2, 7, 1, 9], 15)) # 4
# print(len_of_longest_subarray([10, 5, 2, 7, 1, 9], 20)) # 0
# print(len_of_longest_subarray([9,3,6,4,7,2,-2,-2], 9)) # 5 
# print(len_of_longest_subarray([9,3,0,0,-3,0,4,-3,6,5], 9)) # 8

# brute force approach
def len_of_longest_subarray2(arr, k):

    n = len(arr)
    max_len = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                max_len = max(max_len, j-i+1)
    return max_len


# now if we have only positive numbers in the array, we can use the sliding window approach, also be referred to as two pointer approach
def len_of_longest_subarray3(arr, k):
    n = len(arr)
    curr_sum = 0
    max_len = 0
    left, right = 0, 0

    while right < n:
        curr_sum += arr[right]

        while curr_sum > k and left < right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == k:
            max_len = max(max_len, right - left + 1)

        right += 1
    
    return max_len


# test cases
print(len_of_longest_subarray3([10, 5, 2, 7, 1, 9], 15)) # 4
print(len_of_longest_subarray3([10, 5, 2, 7, 1, 9], 20)) # 0
print(len_of_longest_subarray3([9,3,6,4,7,3,2,1,0,3], 9)) # 5
