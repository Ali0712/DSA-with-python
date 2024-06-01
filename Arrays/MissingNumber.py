# 268. Missing Number

def missing_number(arr):
    n = len(arr)
    expected_sum = n * (n+1) // 2
    actual_sum = 0
    for i in arr:
        actual_sum += i
    
    return expected_sum - actual_sum

# test cases
print(missing_number([3,0,1])) # 2
print(missing_number([0,1])) # 2
print(missing_number([9,6,4,2,3,5,7,0,1])) # 8

# using XOR
def missing_number_xor(arr):
    xor1 = 0
    xor2 = 0
    for i in range(len(arr)):
        xor1 ^= arr[i]
        xor2 ^= i + 1
    return xor1 ^ xor2

# test cases
print(missing_number_xor([3,0,1])) # 2
print(missing_number_xor([0,1])) # 2
print(missing_number_xor([9,6,4,2,3,5,7,0,1])) # 8

# brute force approach
def missing_number2(arr):
    n = len(arr)
    for i in range(n+1):
        if i not in arr:
            return i