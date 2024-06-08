# 128. Longest Consecutive Sequence

# 1 approach
def longest_consecutive(arr):
    n = len(arr)
    i = 0
    max_len = 0
    for i in range(n):
        if arr[i]-1 not in arr:
            leng = 1
            j = arr[i]
            while j<n and j + 1 in arr:
                leng += 1
                j += 1
            max_len = max(leng, max_len)
    return max_len

# optimal approach
def longest_consecutive(arr):
    n = len(arr)
    nums = set(arr)
    max_len = 0
    for num in nums:
        if num - 1 not in nums:
            leng = 1
            j = num
            while j + 1 in nums:
                leng += 1
                j += 1
            max_len = max(leng, max_len)
    return max_len


# test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(longest_consecutive([1]))  # 1