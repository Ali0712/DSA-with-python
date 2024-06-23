
def subarray_with_xor_k(arr, k):
    pre = {0:1}
    count = 0
    xor = 0
    for i in arr:
        xor ^= i
        count += pre.get(xor ^ k, 0)
        pre[xor] = pre.get(xor, 0) + 1
    return count


# test cases
print(subarray_with_xor_k([4,2,2,6,4], 6)) # 4
print(subarray_with_xor_k([5,6,7,8,9], 5)) # 2
print(subarray_with_xor_k([1,2,3], 2)) # 1