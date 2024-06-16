# 560. Subarray Sum Equals K

def subarray_with_sumK(arr, k):
    pre = {0:1}
    count = 0
    sum = 0
    for i in arr:
        sum += i
        count += pre.get(sum - k, 0)
        pre[sum] = pre.get(sum, 0) + 1
    return count



def subarray_with_sumK_bruteforce(arr, k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                count += 1
    return count

def subarray_with_sumK_prefixsum(arr, k):
    count = 0
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if prefix_sum[j] - prefix_sum[i] == k:
                count += 1
    return count


# test cases
print(subarray_with_sumK([1,1,1], 2)) # 2
print(subarray_with_sumK([1,2,3], 3)) # 2
print(subarray_with_sumK([1,2,3,4], 5)) # 1
print(subarray_with_sumK([1,2,3,4], 10)) # 1
print(subarray_with_sumK([1,2,3,4], 8)) # 0
print(subarray_with_sumK([1,2,-3,4,2,1,4,-3,2,1], 4)) # 7