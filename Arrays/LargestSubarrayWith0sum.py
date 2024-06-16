
def largest_subarray_withsum_0(arr):
    maxlen = 0
    curr_sum = 0
    prev = {}
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            maxlen = max(maxlen, i+1)
        if curr_sum in prev:
            maxlen = max(maxlen, i-prev[curr_sum])
        
        else:
            prev[curr_sum] = i
    return maxlen

# test cases
print(largest_subarray_withsum_0([15, -2, 2, -8, 1, 7, 10, 23])) # 5
print(largest_subarray_withsum_0([1, 2, 3])) # 0
print(largest_subarray_withsum_0([1, 2, 3, -3, -4, 2, -2, 1])) # 8
print(largest_subarray_withsum_0([1, 2, 3, -3, -4, 2, -2, 1, 0])) # 9