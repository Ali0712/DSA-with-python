# 2149. Rearrange Array Elements by Sign mean first positive then negative, then positive and so on

# Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance.
# also no of positive is equal to no of negative
def rearrange_elements(arr):
    arranged = []
    i,j=0,0
    n = len(arr)
    # while i < n and j < n:
    count = 0
    while count < n//2:
        while arr[i] < 0:
            i += 1
        while arr[j] > 0:
            j += 1
        arranged.append(arr[i])
        arranged.append(arr[j])
        i += 1
        j += 1
        count += 1

    return arranged

# another approach
def rearrange_elements2(arr):
    i, j = 0, 1
    arranged = [0] * len(arr)
    for k in arr:
        if k > 0:
            arranged[i] = k
            i += 2
        else:
            arranged[j] = k
            j += 2
    return arranged


print(rearrange_elements([3,2,-4,2,-5,-7]))
print(rearrange_elements([3,-4,-6,-9,5,1]))
print(rearrange_elements2([3,4,6,-9,-5,-1,3,-8]))


