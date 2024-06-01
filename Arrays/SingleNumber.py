# 136. Single Number

def single_number(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

# test cases
print(single_number([2,2,1])) # 1
print(single_number([4,1,2,1,2])) # 4
print(single_number([1])) # 1
print(single_number([1,2,3,4,3,2,1])) # 4
print(single_number([1,2,3,4,3,2,1,4,5])) # 5