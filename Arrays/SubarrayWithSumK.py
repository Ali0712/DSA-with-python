# 560. Subarray Sum Equals K

def subarray_with_sumK(arr, k):
    count = 0
    sum = 0
    d = {}
    d[0] = 1
    for i in range(len(arr)):
        sum += arr[i]
        if sum - k in d:
            count += d[sum - k]
        d[sum] = d.get(sum, 0) + 1
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


# two pointer approach
def subarray_with_sumK_twopointer(arr, k):
    count = 0
    total_sum = 0
    left = 0
    right = 0
    while right < len(arr):
        total_sum += arr[right]
        while total_sum > k:
            total_sum -= arr[left]
            left += 1
        if total_sum == k:
            count += 1
        right += 1
    return count

