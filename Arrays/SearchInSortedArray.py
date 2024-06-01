
def binary_search(arr, k):
    n = len(arr)
    left, right = 0, n-1

    while left <= right:
        mid = (left + right) // 2

        if k == arr[mid]:
            return mid

        elif k < arr[mid]:
            right = mid-1
        else:
            left = mid + 1
    return -1


# test cases
print(binary_search([1,3,5,6], 5)) # 2
print(binary_search([1,3,4,5,6,7,8], 2)) # -1
print(binary_search([1,3,5,6,7,8,9,12,13], 7)) # 4
print(binary_search([1,3,5,6,7,8,9,12,13], 13)) # 8
