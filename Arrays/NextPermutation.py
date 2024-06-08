# 31. Next Permutation

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while j >= 0 and arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr


# test cases
print(next_permutation([1, 2, 3]))  # [1, 3, 2]
print(next_permutation([3, 2, 1]))  # [1, 2, 3]
print(next_permutation([1, 1, 5]))  # [1, 5, 1]
print(next_permutation([1]))  # [1]
print(next_permutation([1, 2]))  # [2, 1]


'''
Steps:
1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
2. Find the largest index l greater than k such that a[k] < a[l].
3. Swap the value of a[k] with that of a[l].
4. Reverse the sequence from a[k + 1] up to and including the final element a[n].


'''