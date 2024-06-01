
def union(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j] and arr1[i] != arr1[i-1]:
            res.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j] and arr2[j] != arr2[j-1]:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        if arr1[i] != arr1[i-1]:
            res.append(arr1[i])
            i += 1
    while j < len(arr2):
        if arr2[j] != arr2[j-1]:
            res.append(arr2[j])
            j += 1

    return res

# optimized union function but dont know how it is optimal
def union2(arr1, arr2):
    res = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not res or arr1[i] != res[-1]:
                res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            if not res or arr1[i] != res[-1]:
                res.append(arr1[i])
            i += 1
        else:
            if not res or arr2[j] != res[-1]:
                res.append(arr2[j])
            j += 1

    while i < len(arr1):
        if not res or arr1[i] != res[-1]:
            res.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not res or arr2[j] != res[-1]:
            res.append(arr2[j])
        j += 1

    return res


def intersection(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return res

    


# test cases
# print(union([1,2,3,4,5], [2,3,4,5,6]))
# print(union([1,2,3,4], [6,7,8,9,10]))
# print(union([-2,-1,0,1,2], [-1,0,1,2,3]))
# print(union([-7,8], [-8 ,-3 ,8]))

print(intersection([1,2,2,3,3,3,4,5], [2,3,3,4,5,6]))
print(intersection([1,2,3,4], [6,7,8,9,10]))
print(intersection([-2,-1,0,1,2], [-1,0,1,2,3]))
print(intersection([-7,8], [-8 ,-3 ,8]))